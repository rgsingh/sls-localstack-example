#!/usr/bin/env zsh

~/bin/stop-all-containers.sh && ~/bin/rm-all-containers.sh

docker image prune -a

docker volume prune

docker-compose up -d

docker tag sls-localstack-example_act-ubuntu localhost:5000/ubuntu-builder

docker push localhost:5000/ubuntu-builder

docker rmi localhost:5000/ubuntu-builder
