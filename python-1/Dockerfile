FROM python:3.10-slim

# Update and install security patches
RUN apt-get update && \
    apt-get upgrade -y && \
    apt install -y x11-apps tk8.6 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo "alias norminette=flake8" >> ~/.bashrc

CMD [ "sleep", "infinity" ]