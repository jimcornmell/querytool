FROM mysql

COPY example_data.sql /docker-entrypoint-initdb.d/

ENV MYSQL_DATABASE example
ENV MYSQL_ROOT_PASSWORD pa55word
ENV MYSQL_USER user
ENV MYSQL_PASSWORD pa55word

VOLUME ["/var/lib/mysql"]
ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 3306
CMD ["mysqld"]
