FROM ubuntu:18.04
# ...
RUN apt-get update && apt-get install -y \
    software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-pip
RUN python3.7 -m pip install pip
RUN apt-get update && apt-get install -y \
    python3-distutils \
    python3-setuptools
RUN python3.7 -m pip install pip --upgrade pip
RUN apt-get install -y git
RUN git clone --single-branch --branch brr1 https://github.com/uma-repo/svps.git
RUN ls svps
WORKDIR /svps/uma/myflask/Flask
RUN python3 -m pip install flask
RUN python3 -m pip install mysql-connector-python
CMD [ "/usr/bin/python3", "./regflask.py"]
