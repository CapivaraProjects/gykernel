FROM ubuntu:16.04

MAINTAINER Vinicius Biondi <viniciusbiondi@gmail.com>

RUN apt-get update && apt-get install -y \
        build-essential \
        curl \
        git \
        libfreetype6-dev \
        libpng12-dev \
        libzmq3-dev \
        mlocate \
        pkg-config \
        python-dev \
        python-numpy \
        python-pip \
        software-properties-common \
        swig \
        zip \
        zlib1g-dev \
        libcurl3-dev \
        openjdk-8-jdk\
        openjdk-8-jre-headless \
        wget

# dependencie for tensorflow serving
RUN apt-get install libstdc++6 && \
    add-apt-repository ppa:ubuntu-toolchain-r/test && \ 
    apt-get update && \
    apt-get -y upgrade && \
    apt-get -y dist-upgrade

# clean up
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set up grpc
RUN pip install enum34 futures mock six && \
    pip install --pre 'protobuf>=3.0.0a3' && \
    pip install -i https://testpypi.python.org/simple --pre grpcio

# install tensorflow
RUN pip install tensorflow==1.7.0

# install tensorflow serving API
RUN pip install tensorflow-serving-api==1.7.0

# isntall tensorflow model server
RUN echo "deb [arch=amd64] http://storage.googleapis.com/tensorflow-serving-apt stable tensorflow-model-server tensorflow-model-server-universal" | \
        tee /etc/apt/sources.list.d/tensorflow-serving.list
RUN curl https://storage.googleapis.com/tensorflow-serving-apt/tensorflow-serving.release.pub.gpg | apt-key add -
RUN apt-get update && apt-get install -y tensorflow-model-server

# download gykernel with saved models
WORKDIR /
RUN git clone http://github.com/BiondiVini/gykernel.git

CMD ["/bin/bash"]
