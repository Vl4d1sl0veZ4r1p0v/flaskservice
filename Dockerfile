FROM ubuntu:xenial-20210429

ENV LISTEN_PORT=5000
EXPOSE 5000

RUN apt-get update -y
RUN apt-get install -y python3.5 python3-pip build-essential

COPY . /app
WORKDIR /app

RUN python3 -m pip install --upgrade "pip < 21.0"
RUN python3 -m pip install -r requirements.txt

CMD ["python3", "main.py"]
