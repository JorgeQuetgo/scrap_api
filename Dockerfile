FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV WORKDIR /usr/src/app


WORKDIR ${WORKDIR}

ADD ./ ./

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
