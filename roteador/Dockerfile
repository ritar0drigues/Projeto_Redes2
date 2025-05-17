FROM python:3.10-slim

WORKDIR /app

COPY main.py /app/main.py
COPY classes/ /app/classes/
COPY requirements.txt /app/


RUN apt update && apt install -y \
    iproute2 \
    iputils-ping \
    net-tools \
    traceroute  # Instalar o traceroute


RUN pip install -r requirements.txt


CMD ["python", "main.py"]