FROM python:3.10-buster

COPY . /root/projects/token_check/

WORKDIR /root/projects/token_check

RUN pip install pipenv
RUN mkdir .venv
RUN pipenv install

CMD /root/projects/token_check/.venv/bin/gunicorn --workers 2 --bind 0:5000 "script:token_check"
