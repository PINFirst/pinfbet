# P1NF-Bet

# Development environment

# General Prerequisites

## Install Python 3.8
Make sure you install python 3.8 64 bits version.

## Install virtual env

```
pip install virtualenv
```

## Create virtual env in project root and activate

```
python -m venv .venv
``` 
### Activate on windows:

```
.venv/Scripts/activate.bat
```

### Activate on linux:
```
source .venv/bin/activate
```
# Database requirements

## Install mysql

```
sudo apt install mysql-server
```

## Create user database

```
CREATE user admin@localhost IDENTIFIED by 'admin078';
```

## Create development database
```
CREATE DATABASE pinfbetdb;
```

## Grant privileges with admin user

```
GRANT ALL PRIVILEGES on pinfbetdb.* to admin@localhost;
```

## Use database with 'admin' user

```
USE pinfbetdb;
```

## Install Project Dependencies

```
python -m pip install -r requirements.txt
```

# Start project

## Connect django with database

```
python manage.py migrate
```

## Run server 
```
python manage.py runserver
```

# Create Django Admin User

```
python manage.py createsuperuser
```