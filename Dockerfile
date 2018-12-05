FROM continuumio/miniconda3:4.5.11
MAINTAINER Roman Kreuzhuber 

RUN apt-get install -y zlib1g-dev && conda install -c anaconda mongodb pymongo --yes && pip install mongoengine json flask && pip install git+git://github.com/krrome/eqtlBrowser
