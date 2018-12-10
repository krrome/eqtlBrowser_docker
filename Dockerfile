FROM tiangolo/uwsgi-nginx-flask:python3.6
MAINTAINER Roman Kreuzhuber 

RUN pip install pymongo==3.4.0 mongoengine==0.16.1 pyyaml &&\
	cd /etc &&\
	mkdir eqtl_browser &&\
	cd eqtl_browser &&\
	git clone https://github.com/krrome/eqtlBrowser.git

#COPY eqtlBrowser /etc/eqtl_browser/eqtlBrowser

RUN  pip install -e /etc/eqtl_browser/eqtlBrowser


# restructure the project or create a symlink to the app as it is desired by this image
COPY ./uwsgi.ini /app/uwsgi.ini
RUN rm /app/main.py && ln -s /etc/eqtl_browser/eqtlBrowser/ebrowse /app/app

#ENV STATIC_PATH /app/app/static