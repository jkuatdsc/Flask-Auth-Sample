
# Simple Auth

A simple flask authentication app with signup, login and logout features 

## Screenshots
<img src="https://github.com/jkuatdsc/Flask-Auth-Sample/blob/master/assets/simplelogin.png?raw=true" width="1000">
<img src="https://github.com/jkuatdsc/Flask-Auth-Sample/blob/master/assets/simplesignup.png?raw=true" width="1000">
<img src="https://github.com/jkuatdsc/Flask-Auth-Sample/blob/master/assets/simplehome.png?raw=true" width="1000">

## Getting Started

* Clone the repository
	``git clone https://github.com/jkuatdsc/Flask-Auth-Sample.git``
  
* Navigate to the project folder
	``cd Flask-Auth-Sample``
	
* Create a virtual environment
	``virtualenv venv``
	
* Activate the virtual environment
	``Source venv/bin/activate``
	
* Install dependencies from the requirements.txt file
	``pip3 install -r requirements.txt``
	
* Create a .env file
	``touch .env``

* Add environment variables to the file
	``DEBUG=True``

	``SECRET_KEY='qwertyuiop1233456476897890'``

	``SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://username:password@127.0.0.1:5432/db_name'``

* Create a database
	``psql``
    ``CREATE DATABASE database_name``

### Make migrations

* python3 manage.py db init
* python3 manage.py db upgrade
* python3 manage.py db migrate -m 'Some message'  

## Run the server
>Start the server and make
``python3 manage.py runserver``

## Flowchart

```mermaid
graph LR
A[Register] --> B[login]
B --> A
B --> C{isAuthenticated}
C -- Yes --> D[ Welcome page ]
C -- No --> B
D -- Log out --> E[logout]
E --> B
```
