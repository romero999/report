FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    build-essential \
    python3.7 \
    python3.7-dev \
    python3-distutils \
    curl

RUN ln -sf /usr/bin/python3.7 /usr/bin/python3

RUN curl https://bootstrap.pypa.io/get-pip.py -o /tmp/get-pip.py && \
    python3 /tmp/get-pip.py && \
    rm /tmp/get-pip.py

WORKDIR /root

RUN pip3 install datetime \
    unicodedata 

COPY ./sample.py sample.py

CMD ["python3", "sample.py"]
