import json
import ssl
from jwcrypto import jwk, jws
from werkzeug.contrib.cache import SimpleCache
from datetime import datetime
from flask import request
import jwt
from six.moves.urllib.request import urlopen
from box import Box
from error import AxiomsError
from options import URL_LIB_SSL_IGNORE
from flask import current_app as app

cache = SimpleCache()


def has_bearer_token(request_obj):
    header_name = 'Authorization'
    token_prefix = 'bearer'
    auth_header = request_obj.headers.get(header_name, None)
    if auth_header is None:
        raise AxiomsError({"code": "missing_authorization_header",
                           "description": "Missing Authorization Header"}, 401)
    try:
        bearer, _, token = auth_header.partition(' ')
        if bearer.lower() == token_prefix and token != "":
            return token
        else:
            raise AxiomsError({"code": "invalid_authorization_bearer",
                               "description": "Invalid Authorization Bearer"}, 401)
    except (ValueError, AttributeError):
        raise AxiomsError({"code": "invalid_authorization_header",
                           "description": "Invalid Authorization Header"}, 401)

def has_valid_token(token):
    kid = jwt.get_unverified_header(token)['kid']
    key = get_key_from_jwks_json(app.config["AXIOMS_DOMAIN"], kid)
    payload = check_token_validity(token, key)
    if payload and app.config["AXIOMS_AUDIENCE"] in payload.aud: # pylint: disable=maybe-no-member
        request.auth_jwt = payload
        return True
    else:
        raise AxiomsError({"code": "invalid_access_token",
                           "description": "Invalid access token"}, 401)

def check_token_validity(token, key):
    payload = get_payload_from_token(token, key)
    now = datetime.utcnow().timestamp()
    if payload and (now <= payload.exp):
        return payload
    else:
        return False

def get_payload_from_token(token, key):
    jwstoken = jws.JWS()
    jwstoken.deserialize(token)
    try:
        jwstoken.verify(key)
        return Box(json.loads(jwstoken.payload))
    except jws.InvalidJWSSignature:
        return None

def check_scopes(provided_scopes, required_scopes):
    if not required_scopes:
        return True

    token_scopes = set(provided_scopes.split())
    scopes = set(required_scopes)
    return len(token_scopes.intersection(scopes)) > 0

def get_key_from_jwks_json(tenant, kid):
    fetcher = CacheFetcher()
    data = fetcher.fetch("https://"+tenant+"/oauth2/.well-known/jwks.json", 600)
    return jwk.JWKSet().from_json(data).get_key(kid)

class CacheFetcher:
    def fetch(self, url, max_age=300):
        # Redis cache
        cached = cache.get('jwks'+url)
        if cached:
            return cached
        # Retrieve and cache
        if URL_LIB_SSL_IGNORE:
            context = ssl._create_unverified_context()
            data = urlopen(url, context=context).read()
        else:
            data = urlopen(url).read()
        cache.set('jwks'+url, data, timeout=max_age)
        return data
