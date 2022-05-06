# Money_Movements_Task
A small money movements app

## Step 1:
## Install dependencies & activate virtualenv

```
$ mkdir .venv
$ pipenv install
$ pipenv shell
```
or 
```
sudo apt install python3-venv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
## Step 2:
## DB setup

```
$ psql -U postgres
postgres=# create user <username> with createdb;
postgres=# CREATE DATABASE moneymovements OWNER <username>;
postgres=# GRANT ALL PRIVILEGES ON DATABASE moneymovements TO <username>;
```


## Step 3:
## Run migrations

```
$ bash db.sh
```

## Step 4:
## Start app

```
$ python3 wsgi.py
```
## Step 5:
## Open Base Url

```
http://127.0.0.1:5000/auth/login
```
## Step 6:
## For Documentation

```
http://127.0.0.1:5000/redoc/
```

