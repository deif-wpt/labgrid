FROM python:3.6

# Tools 
RUN apt-get update && \
    apt-get install microcom -y
    
# install labgrid latest master
RUN git clone https://github.com/deif-wpt/labgrid.git /opt/labgrid
RUN pip install -e /opt/labgrid

RUN echo "stty rows 33 cols 204" >> /etc/bash.bashrc

WORKDIR /opt/labgrid
CMD ["/bin/bash"]
