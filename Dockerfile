FROM python:3.8.1-buster

RUN adduser --disabled-login moo
USER moo

WORKDIR /home/moo

ENV FLASK_APP=moo.py

COPY --chown=moo *.py requirements.txt /home/moo/

RUN pip install -r requirements.txt

COPY --chown=moo app app

EXPOSE 8888

CMD python -m flask create-db && python -m flask run -p 8888 -h 0.0.0.0
