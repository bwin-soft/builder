FROM registry.cn-shenzhen.aliyuncs.com/bwin/nginx_tomcat:deb_2.1

COPY nginx.conf /etc/nginx/nginx.conf
ADD static /home/static
COPY trade.war /usr/local/tomcat/webapps/trade.war

CMD ["/service.sh"]
