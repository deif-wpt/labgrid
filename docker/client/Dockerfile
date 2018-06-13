FROM python:3
RUN apt-get update
RUN apt-get install --assume-yes microcom

#RUN git clone https://github.com/labgrid-project/labgrid /opt/labgrid
RUN git clone -b remote_tmpdir https://github.com/deif-wpt/labgrid.git /opt/labgrid
RUN cd /opt/labgrid && python3 setup.py install

RUN echo '#!/bin/bash' > /opt/entry_script.sh
RUN echo '/bin/bash' >> /opt/entry_script.sh
RUN chmod a+x /opt/entry_script.sh
ENTRYPOINT ["/opt/entry_script.sh"]


