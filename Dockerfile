FROM continuumio/miniconda3:4.5.11
MAINTAINER Roman Kreuzhuber 

RUN apt-get install -y zlib && pip install pymongo mongoengine zlib json flask && pip install git+git://github.com/krrome/eqtlBrowser
