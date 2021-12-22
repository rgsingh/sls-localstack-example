![sls-localstack-example](https://github.com/rgsingh/sls-localstack-example/actions/workflows/localstack-ci.yml/badge.svg)

## Serverless LocalStack CI with GitHub Actions

## 1) Pre-requisites for [Act](https://github.com/nektos/act)
###### (WARNING! Commands in prereqs.sh remove Docker images) See [prereqs.sh](./prereqs.sh) to manage the below steps in one script

### Create custom Ubuntu Docker image needed by Act and a local registry to push it to

    docker-compose up -d

### Push new ubuntu-builder image to local registry for use by Act

    docker tag sls-localstack-example_act-ubuntu localhost:5000/ubuntu-builder

    docker push localhost:5000/ubuntu-builder

    docker rmi localhost:5000/ubuntu-builder

## 2) Running Act 
###### (Once above Pre-requisites are performed, start here for repeatable GitHub Actions testing)
#### Deploys LocalStack, sets up environment, installs Python, runs pytest, and deploys application via Serverless Framework

    act --container-architecture linux/amd64 -P ubuntu-latest=localhost:5000/ubuntu-builder -P localstack/localstack:latest

## TODO
###### (Need to integrate this into integration test within GitHub Actions)
### AWS CLI verification
#### Verify identity

    aws --endpoint-url=http://localhost:4566 sts get-caller-identity 

#### List S3 resources

    aws --endpoint-url=http://localhost:4566 s3 ls 

#### Invoke function

    sls invoke -f greeting --stage dev 

### Cleanup

#### Remove stack (this may fail with an unknown error leaving the LocalStack container in a weird state)

    sls remove --stage local
