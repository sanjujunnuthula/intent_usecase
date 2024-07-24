FROM ubuntu:latest
LABEL authors="sjunnuth"

ENTRYPOINT ["top", "-b"]