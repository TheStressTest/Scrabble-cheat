FROM python:alpine3.9

WORKDIR /usr/src/app

COPY . .

RUN python3 generate.py words.json output_words.json

CMD [ "sleep", "1000" ]