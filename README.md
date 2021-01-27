### Project Specs

Project consists of different parts: the main application, database, etc. The application folder can be run individually if needed provided the right environment variables are available.

- Python 3.9
- Linux Ubuntu
- Docker, Dokcer-Compose
- PostgreSQL
- .env file

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

| Request |   Endpoint   | Payload | Response | Status Code |
| ------- | :----------: | :-----: | :------: | ----------- |
| GET     |   /status    |    -    |          | 200         |
| GET     |   /records   |    -    |          | 200         |
| POST    |   /records   |  {...}  |          | 201         |
| GET     | /records/:id |   :id   |          | 200         |
| PUT     | /records/:id |   :id   |          | 201         |
| DELETE  | /records/:id |   :id   |          | 200         |
