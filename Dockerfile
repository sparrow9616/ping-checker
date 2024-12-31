FROM python:3.10
RUN apt-get update -y && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
RUN pip3 install --no-cache-dir -U -r requirements.txt

COPY . .

CMD ["python", "main.py"]

