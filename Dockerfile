FROM ubuntu:latest

RUN apt-get -y update

RUN apt-get install python3 python3-pip -y

COPY ./app /app

WORKDIR /app

COPY ./requirements.txt /var/www/requirements.txt

RUN pip3 install /var/www/requirements.txt

CMD ["python app/main.py"]
