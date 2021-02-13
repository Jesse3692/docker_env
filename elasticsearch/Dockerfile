FROM elasticsearch:7.3.2
ENV VERSION=7.3.2
ADD elasticsearch-analysis-ik-7.3.2.zip /tmp/
# ADD https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.3.2/elasticsearch-analysis-ik-7.3.2.zip /tmp/
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin install -b file:///tmp/elasticsearch-analysis-ik-$VERSION.zip
RUN rm -rf /tmp/*