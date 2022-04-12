FROM  ubuntu:20.04
ENV TZ=Asia/Shanghai

RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list \
     && apt-get update \
     && apt-get -y upgrade \
     && apt-get -y dist-upgrade \
     && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
     && apt-get install tzdata \
     && apt-get -y install gcc make zlib1g zlib1g-dev openssl libpcre3 libpcre3-dev vim curl iputils-ping \
     && apt-get -y install libbz2-dev libsqlite3-dev libxml2-dev libffi-dev libssl-dev libxslt1-dev \
     && apt-get -y install wget bzip2 \
     && apt-get install -y libmysqlclient-dev  libldap2-dev libsasl2-dev libssl-dev \
     && apt-get install -y --no-install-recommends git postgresql-client \
     && apt-get clean \
     && apt-get autoclean \
     && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN wget https://www.python.org/ftp/python/3.10.2/Python-3.10.2.tar.xz \
    && tar -xvf Python-3.10.2.tar.xz \
    && cd Python-3.10.2 && ./configure --prefix=/usr/local/python3 --enable-optimizations && make && make install \
    && ln -s /usr/local/python3/bin/python3 /usr/bin/python \
    && ln -s /usr/local/python3/bin/pip3 /usr/bin/pip \
    && cd ../ \
    && rm -rf ./Python-3.10.2 \
    && rm -rf ./Python-3.10.2.tar.xz

ENV PATH="/usr/local/python3/bin:${PATH}"

RUN pip install -U pip -i http://mirrors.aliyun.com/pypi/simple \
    && pip config set global.index-url http://mirrors.aliyun.com/pypi/simple \
    && pip config set install.trusted-host mirrors.aliyun.com \
    && apt-get update \
    && apt-get install -y libmysqlclient-dev  libldap2-dev libsasl2-dev libssl-dev \
    && apt-get install -y --no-install-recommends git \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*