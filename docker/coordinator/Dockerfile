FROM python:3
RUN pip install crossbar && \
    git clone https://github.com/labgrid-project/labgrid /opt/labgrid && \
    pip install -e /opt/labgrid/ 

WORKDIR /opt/labgrid
CMD ["crossbar", "start"]
