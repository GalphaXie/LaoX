FROM python:3.5.2
LABEL version="1.0"
ENV PYTHONUNBUFFERED 1
RUN mkdir /code/SH_backend -p
RUN mkdir /code/logs -p
WORKDIR /code/SH_backend
ADD . /code/SH_backend
RUN pip install -r requirements.txt
RUN chmod u+x docker-entrypoint.sh
ENTRYPOINT ["/bin/bash", "docker-entrypoint.sh"]
