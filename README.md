### Project Specs

Project consists of different parts: the main application, database, etc. The application folder can be run individually if needed provided the right environment variables are available.

- Python 3.9
- Linux Ubuntu
- Docker, Dokcer-Compose
- PostgreSQL
- .env file

#### .env file

```
db_user=''
db_password=''
db_host=''
db_name=''
db_port=''
```

## Project can be setup and run in 2 ways:

## Method 1

### Set up the project

- Clone the project from its repository
- Create a virtual environment
- Install package requirements into virtual environment:
  `pip install -r [path-to]/requirements.txt`
- Get the .env file and set the respective variables
- Create the database and note the name, port, db user & password
- flask db init
- flask db migrate
- flask db upgrade

### Run the project

- python runner.py runserver

## Method 2 (incomplete)

- Clone the project from its repository
- Get the .env file and set the respective variables
- docker

### API Endpoints

| Request |   Endpoint   |                               Payload                               | Response | Status Code |
| ------- | :----------: | :-----------------------------------------------------------------: | :------: | ----------- |
| GET     |   /status    |                                  -                                  |          | 200         |
| GET     |   /records   |                                  -                                  |          | 200         |
| POST    |   /records   | `{"code":"", "desc_short":"", "desc_long":"","type":"", "year":""}` |          | 201         |
| GET     | /records/:id |                                `id`                                 |          | 200         |
| PUT     | /records/:id |                                `id`                                 |          | 201         |
| DELETE  | /records/:id |                                `id`                                 |          | 200         |

ICD-9
3-5 characters length
first-digit: alphanumeric
digit 2 - 5: numeric

---

A23, 02311

ICD-10
3-7 characters length
first-digit: alphabet
digit 2 - 3: numeric
digit 4 - 7: numeric

---

A12456

not ICD-9-CM, ICD-10-PCS

Find out more (here)[https://www.m-scribe.com/blog/the-6-major-differences-between-icd-9-and-icd-10-codes#:~:text=ICD%2D9%20codes%20can%20contain,not%20covered%20under%20ICD%2D9.] and (here)[https://www.webpt.com/blog/understanding-icd-10-code-structure/] and (here)[https://icd.who.int/icd11refguide/en/index.html]
