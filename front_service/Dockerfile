FROM registry.cn-shenzhen.aliyuncs.com/bwin/nginx_tomcat:1.1

COPY nginx.conf /etc/nginx/nginx.conf
ADD static /home/static
COPY trade.war /usr/local/tomcat/webapps/ROOT.war 

CMD ["/service.sh"]
