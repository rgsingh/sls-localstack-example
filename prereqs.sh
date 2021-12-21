#!/usr/bin/env zsh

docker stop $(docker ps -a -q)

docker rm $(docker ps -a -q)

docker image prune -a

docker volume prune

docker-compose up -d

docker tag sls-localstack-example_act-ubuntu localhost:5000/ubuntu-builder

docker push localhost:5000/ubuntu-builder

docker rmi localhost:5000/ubuntu-builder
