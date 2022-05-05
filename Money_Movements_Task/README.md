# Money_Movements_Task
A small money movements app

## DB setup:

```
$ psql -U postgres
postgres=# create user <username> with createdb;
postgres=# CREATE DATABASE moneymovements OWNER <username>;
postgres=# GRANT ALL PRIVILEGES ON DATABASE moneymovements TO <username>;
```

# Inside of Money_Movements_Task/ dir:

## Install dependencies & activate virtualenv

```
$ mkdir .venv
$ pipenv install
$ pipenv shell
```

## Run migrations

```
$ bash db.sh
```

## Start app:

```
$ python3 wsgi.py
```
## Open Base Url

```
http://127.0.0.1:5000/auth/login
```
## For Documentation

```
http://127.0.0.1:5000/redoc/
```