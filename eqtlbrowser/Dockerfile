FROM krrome/conda3.7-uwsgi-nginx-flask-mongo
MAINTAINER Roman Kreuzhuber


#### Finally install the eQTLbrowser
RUN cd /etc/eqtl_browser &&\
	git clone https://github.com/krrome/eqtlBrowser.git &&\
	pip install -e /etc/eqtl_browser/eqtlBrowser


# restructure the project or create a symlink to the app as it is desired by this image
COPY ./uwsgi.ini /app/uwsgi.ini
RUN rm /app/main.py && ln -s /etc/eqtl_browser/eqtlBrowser/ebrowse /app/app

# 
COPY ./run_mongodb.sh /app/prestart.sh

#ENV STATIC_PATH /app/app/static