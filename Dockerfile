FROM python:alpine3.10

WORKDIR /usr/src/app

EXPOSE 8080

COPY . .

RUN python3 generate.py words.json output_words.json

RUN python3 -m pip install flask

CMD [ "python3", "flask/main.py" ]
