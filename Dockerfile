FROM ubuntu 

RUN apt-get update && apt-get install python3 -y && apt-get install pip -y && pip install flask \
    && pip install prometheus_client
COPY ./app.py /app.py

ENTRYPOINT python3 /app.py


