# Trips test changelog sqlalchemy continuum

Steps to run the example:

## Create and enter the venv:

```shell script
python3 -m venv .venv
source .venv/bin/activate
```

## Install packages:

```shell script
pip install -r requirements.txt
```

## Launch postgres:

```shell script
docker-compose up -d postgres
```

## Init database:

```shell script
alembic upgrade head
```

## Run example:

```shell script
python trips/init_data.py
```