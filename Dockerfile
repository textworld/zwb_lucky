FROM registry.cn-hangzhou.aliyuncs.com/textworld/python:3.10.2

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  && apt-get install -y nginx \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /webroot/app

COPY ./home /webroot/app/home
COPY ./zwb_lucky /webroot/app/zwb_lucky
COPY ./requirements.txt ./gunicorn_config.py ./entrypoint.sh ./manage.py ./nginx_site.conf /webroot/app/
COPY ./bin/ /webroot/app/bin

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /webroot/logs && mkdir /webroot/static && mkdir /webroot/run/ && chmod +x /webroot/app/entrypoint.sh && chmod +x /webroot/app/bin/*.sh

EXPOSE 8000

STOPSIGNAL SIGQUIT

ENTRYPOINT ["/webroot/app/entrypoint.sh"]
