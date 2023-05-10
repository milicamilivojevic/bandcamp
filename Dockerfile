FROM python:3.10-alpine

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.14/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.14/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add libffi-dev
RUN apk add mpc1-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc xvfb libc-dev linux-headers postgresql-dev \
    && apk add libffi-dev
RUN apk add chromium chromium-chromedriver

RUN pip3 install -U pip
ENV bandcamp .
RUN mkdir /bandcamp
WORKDIR /bandcamp
ADD requirements.txt /bandcamp/
RUN pip3 install -r requirements.txt
ADD . /bandcamp/
WORKDIR /bandcamp/bandcamp
CMD ["scrapy", "crawl", "selenium", "-o", "output.json"]