FROM python:alpine3.17

RUN apk update && apk upgrade \
    && apk add zsh gcc libxml2-dev libxslt-dev \
    && apk add --no-cache bash git openssh \
    && rm -rf /var/cache/apk/*

