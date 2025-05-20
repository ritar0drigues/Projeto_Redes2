FROM python:3.10-slim

WORKDIR /app

COPY host.py /app/host.py 


RUN apt-get update && apt-get install -y \
    iproute2 \
    net-tools \
    iputils-ping \
    traceroute  

CMD ["python", "host.py"]