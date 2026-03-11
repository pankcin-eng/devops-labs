FROM ubuntu:22.04

RUN apt-get update && apt-get install -y hostname && rm -rf /var/lib/apt/lists/*

COPY hello-devops.sh /usr/local/bin/hello-devops.sh
RUN chmod +x /usr/local/bin/hello-devops.sh

CMD ["/usr/local/bin/hello-devops.sh"]
