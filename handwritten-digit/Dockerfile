FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 8081

COPY . .

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
