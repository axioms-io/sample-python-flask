# sample-python-flask
Flask APIs Sample using Axioms. Secure your Flask APIs using Axioms Authentication and Authorization.

## Prerequisite

* Python 3.7+

## Running sample locally
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

Run flask

```
flask run
```