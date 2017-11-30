FROM ubuntu:xenial

RUN apt-get update -qq && apt-get install -y curl apparmor && rm -rf /var/lib/apt/lists/*

RUN curl -fSL -o mysql-router.deb https://dev.mysql.com/get/Downloads/MySQL-Router/mysql-router_8.0.3-dmr-1ubuntu16.04_amd64.deb
RUN dpkg -i mysql-router.deb && rm -f mysql-router.deb

EXPOSE 7001 7002
CMD ["/usr/sbin/mysqlrouter", "--extra-config=/root/router.ini"]
