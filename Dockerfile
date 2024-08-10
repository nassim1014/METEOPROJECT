FROM confluentinc/cp-zookeeper:7.4.0

# Add necessary utilities
RUN yum update -y && yum install -y nmap-ncat

# Update Zookeeper configuration to allow ruok command
RUN echo "4lw.commands.whitelist=*" >> /etc/kafka/zookeeper.properties