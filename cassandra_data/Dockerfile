FROM cassandra:3.1

COPY entrypoint-wrap.sh /entrypoint-wrap.sh
COPY schema.cql /schema.cql
ENTRYPOINT ["/entrypoint-wrap.sh"]
CMD ["cassandra", "-f"]