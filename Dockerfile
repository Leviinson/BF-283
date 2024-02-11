FROM ubuntu:22.04

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV LANGUAGE=C.UTF-8

# django
ENV SECRET_KEY=${SECRET_KEY}

# mysql
ENV MYSQL_DATABASE=${MYSQL_DATABASE}
ENV MYSQL_HOST=${MYSQL_HOST}
ENV MYSQL_PORT=${MYSQL_INTERNAL_PORT}
ENV MYSQL_USER=${MYSQL_USER}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}

# mail service
ENV MAIL_SERVER=${MAIL_SERVER}
ENV MAIL_USERNAME=${MAIL_USERNAME}
ENV MAIL_PASSWORD=${MAIL_PASSWORD}
ENV MAIL_PORT=${MAIL_PORT}
ENV DEFAULT_FROM_EMAIL=${DEFAULT_FROM_EMAIL}

ENV TWILIO_ACCOUNT_SID=${TWILIO_ACCOUNT_SID}
ENV TWILIO_PHONE_NUMBER=${TWILIO_PHONE_NUMBER}
ENV TWILIO_AUTH_TOKEN=${TWILIO_AUTH_TOKEN}

# zoho crm
ENV ZOHO_CURRENT_USER_EMAIL=${ZOHO_CURRENT_USER_EMAIL}
ENV ZOHO_RESOURCE_PATH=${ZOHO_RESOURCE_PATH}
ENV ZOHO_LOGGER_PATH=${ZOHO_LOGGER_PATH}
ENV GRANT_TOKEN=${GRANT_TOKEN}
ENV ZOHO_CLIENT_SECRET=${ZOHO_CLIENT_SECRET}
ENV ZOHO_CLIENT_ID=${ZOHO_CLIENT_ID}

ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN DEBIAN_FRONTEND=noninteractive \
    && set -xe \
    && apt update && apt upgrade -y \
    && apt install -y build-essential \
                      pkg-config \
                      python3-pip 
RUN pip install virtualenvwrapper poetry 
WORKDIR /apps/BonnyFlowers/

RUN apt install -y zlib1g-dev \
                   libncurses5-dev \
                   libgdbm-dev \
                   libnss3-dev \
                   libssl-dev \
                   libreadline-dev \
                   libffi-dev \
                   libsqlite3-dev \
                   wget \
                   libbz2-dev \
                   tar \
                   python3-dev \
                   default-libmysqlclient-dev \
                   mysql-server

RUN cd /tmp && wget https://www.python.org/ftp/python/3.10.0/Python-3.10.0.tgz
RUN cd /tmp && tar -xf Python-3.10.0.tgz && cd Python-3.10.0 && ./configure && make -j 6 && make install

RUN poetry config virtualenvs.in-project true

RUN pip install --upgrade poetry
EXPOSE 8000