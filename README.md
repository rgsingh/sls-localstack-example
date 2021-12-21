
# Serverless LocalStack

## Install

    npm i

## LocalStack Deploy

    docker-compose up -d

## Serverless Deploy
    sls deploy --stage local

## Verify identity

    aws --endpoint-url=http://localhost:4566 sts get-caller-identity 

## List S3 resources

    aws --endpoint-url=http://localhost:4566 s3 ls 

## Invoke function

    sls invoke -f hello --stage local 


## Cleanup

### Remove stack (this may fail with an unknown error leaving the LocalStack container in a weird state)

    sls remove --stage local

### List containers, stop them, remove them, and remove any images

    # List, stop, and remove container
    docker ps -a
    docker stop <container ID>
    docker rm <container ID>

    # Remove images 
    docker image prune