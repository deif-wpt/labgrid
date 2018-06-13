FROM python:3

RUN git clone https://github.com/labgrid-project/labgrid /opt/labgrid
RUN cd /opt/labgrid && pip3 install -r crossbar-requirements.txt && python3 setup.py install

RUN echo '#!/bin/bash' > /opt/entry_script.sh
RUN echo 'cd /opt/labgrid && /usr/local/bin/crossbar start' >> /opt/entry_script.sh
RUN chmod a+x /opt/entry_script.sh
ENTRYPOINT ["/opt/entry_script.sh"]


