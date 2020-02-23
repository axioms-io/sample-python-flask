# sample-python-flask
Flask APIs Sample using [Axioms](https://axioms.io). Secure your Express APIs using Axioms authentication and authorization.

## Prerequisite

* Python 3.7+
* An [Axioms](https://axioms.io) client which can obtain access token after user's authentication and authorization and include in `Authorization` header of all API request sent to Node/Express application server.

## Setup
Clone this repository,

```
git clone https://github.com/axioms-io/sample-python-flask.git
cd sample-python-flask
```

Create virtualenv,

```
python3 -m venv venv
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