FROM python:3

# Tools 
RUN apt-get update && \
    apt-get install microcom -y
    
# install labgrid latest master
RUN git clone -b remote_tmpdir https://github.com/deif-wpt/labgrid.git /opt/labgrid && \
    pip install -e /opt/labgrid

RUN echo "stty rows 33 cols 204" >> /etc/bash.bashrc

WORKDIR /opt/labgrid
CMD ["/bin/bash"]
