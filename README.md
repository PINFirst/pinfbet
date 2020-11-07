# P1NF-Bet

## Development environment
Follow this instructions if you are a developer.

### General Prerequisites
Follow this instructions before clone the project.

### Install Python 3.8
Make sure you install python 3.8 64 bits version.

### Install virtual env

```
pip install virtualenv
```


## Database requirements
Create and setup the development database.

### Install mysql

#### Windows versions:
Download mysql from [official site of mysql](https://dev.mysql.com/downloads/mysql/) and 
include the to the path.

#### Linux version:

```
sudo apt install mysql-server
```

Finally enter in mysql using your root user and following next step from that session.

```
mysql -u root -p
```

### Create user database

Create mock admin user
```
CREATE user admin@localhost IDENTIFIED by 'admin078';
```

### Create development database
```
CREATE DATABASE pinfbetdb;
```

### Grant privileges with admin user

```
GRANT ALL PRIVILEGES on pinfbetdb.* to admin@localhost;
```

### Use database with 'admin' user
First exit from root user session:
````
exit
````
Then login with new admin user:

```
mysql -u admin -p
```
Then select the development database:
```
USE pinfbetdb;
```

## Project setup
Follow this steps into the project root folder once you clone this repository.

### Create virtual env in project root and activate

```
python -m venv .venv
``` 
#### Activate on windows:

```
.venv/Scripts/activate.bat
```

#### Activate on linux:
```
source .venv/bin/activate
```

### Install Project Dependencies

```
python -m pip install -r requirements.txt
```

## Start project

### Connect django with database
Apply the initial migrations connecting the project with the database.

```
python manage.py migrate
```

### Run server 
```
python manage.py runserver
```
If all gone right you will see the project running on [http://127.0.0.1:8000/](http://127.0.0.1:8000/)


### Create Django Admin User
Create super user to access Django admin site 

```
python manage.py createsuperuser
```

Check it by accessing  the following link [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)