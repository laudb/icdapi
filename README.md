### Project Specs

- Python 3.9
- Linux Ubuntu
- Docker, Dokcer-Compose
- PostgreSQL

## Project can be setup and run in 2 ways:

## Method 1

### Set up the project

- Clone the project from its repository
- Get the .env file and set the respective variables
- Create the database and note the name, port, db user & password

- flask db init
- flask db migrate
- flask db upgrade

### Run the project

- python runner.py runserver

## Method 2

- Clone the project from its repository
- Get the .env file and set the respective variables
- docker

### API Endpoints

GET /status
GET /records
POST /records
POST /records/:id
EDIT /records/:id
DELETE /records/:id
