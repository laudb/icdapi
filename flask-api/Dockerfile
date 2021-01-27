FROM python:3.9

RUN apt-get update

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "runner.py runserver" ]