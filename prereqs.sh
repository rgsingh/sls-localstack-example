#!/usr/bin/env zsh

# Uncomment to stop containers
#docker stop $(docker ps -a -q)

# Uncomment to remove containers
#docker rm $(docker ps -a -q)

# Uncomment to prune all images
#docker image prune -a

# Uncomment to prune volumes
#docker volume prune

docker-compose up -d

docker tag sls-localstack-example_act-ubuntu localhost:5000/ubuntu-builder

docker push localhost:5000/ubuntu-builder

docker rmi localhost:5000/ubuntu-builder
