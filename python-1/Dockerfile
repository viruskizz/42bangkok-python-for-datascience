FROM python:3.10-slim

# Update and install security patches
RUN apt-get update && \
    apt-get upgrade -y && \
    apt install -y x11-apps && \
    apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN alias=flake8

CMD [ "sleep", "infinity" ]