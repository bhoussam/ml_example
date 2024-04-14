FROM ubuntu:latest
LABEL authors="houssam"

ENTRYPOINT ["top", "-b"]