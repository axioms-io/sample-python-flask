# sample-python-flask
Flask APIs Sample using [Axioms](https://axioms.io) and [axioms-flask-py](https://github.com/axioms-io/axioms-flask-py). Secure your Flask APIs using Axioms authentication and authorization.

## Prerequisite

* Python 3.7+
* An [Axioms](https://axioms.io) client which can obtain access token after user's authentication and authorization and include obtained access token as bearer in `Authorization` header of all API request sent to Python/Flask application server.

## Setup
Clone this repository,

```
git clone https://github.com/axioms-io/sample-python-flask.git
cd sample-python-flask
```

Create virtualenv,

```
python -m venv venv
```

Then activate `virtualenv` and install requirements,

```
source venv/bin/activate
pip install -r requirements-dev.txt
```

Set environment variables,
```
export FLASK_APP=api.py
export FLASK_ENV=development
```

## Add Config
Create a `.env` file and add following configs (see `.sample-env`),

```
AXIOMS_DOMAIN=<your-axioms-slug>.axioms.io
AXIOMS_AUDIENCE=<your-axioms-resource-identifier>
```

## Run flask

```
flask run
```

## Test using Postman
Postman collection is included in this repository. Import the collection in your Postman, setup environment variables `host` (i.e. localhost:5000) and `access_token` (you can obtain from your client) and test these APIs.

## Documentation
See [documentation](https://developer.axioms.io/docs/sdks-samples/use-with-apis/python/flask-apis) for `axioms-flask-py`.

## Deploy to Heroku
You will need to provide Axioms domain and Axioms audience to complete deployment.

<a href="https://heroku.com/deploy?template=https://github.com/axioms-io/sample-python-flask">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy" width="200px">
</a>

[![Edit sample-python-flask](https://codesandbox.io/static/img/play-codesandbox.svg)](https://codesandbox.io/s/github/axioms-io/sample-python-flask/tree/master/?fontsize=14&hidenavigation=1&theme=light)