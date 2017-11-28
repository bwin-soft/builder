FROM registry.cn-shenzhen.aliyuncs.com/bwin/tomcat_7_jdk8:deb_1.1

COPY nginx.conf /etc/nginx/nginx.conf
ADD static /home/static
COPY trade.war /usr/local/tomcat/webapps/trade.war

CMD ["/service.sh"]
