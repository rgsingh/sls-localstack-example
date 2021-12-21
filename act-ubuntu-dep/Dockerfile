# Used by act to avoid "::error::Version <python-version> with arch x64 not found" error
# Once deployed, run `act -P ubuntu-latest=ubuntu-builder` assuming Docker image is tagged as `ubuntu-builder`
FROM ubuntu:20.04

RUN apt-get update \
    && apt-get upgrade -y \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    curl \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*