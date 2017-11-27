FROM registry.cn-shenzhen.aliyuncs.com/bwin/nginx_tomcat:deb_1.0

COPY nginx.conf /etc/nginx/nginx.conf
ADD static /home/static
COPY trade.war /usr/local/tomcat/webapps/trade.war

CMD ["/service.sh"]
