FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get install python3 python3-pip -y
COPY ./app /app
WORKDIR /app
CMD ["python app/main.py"]
