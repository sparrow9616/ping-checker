FROM python:3.10
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
COPY . /app/
COPY .env /app/.env
WORKDIR /app/
RUN chmod 777 -R /app
RUN pip3 install -r requirements.txt
CMD bash start

