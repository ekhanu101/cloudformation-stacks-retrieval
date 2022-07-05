!/bin/bash
### MAke sure youre in the correct AWS account before you proceed any further###
aws ecr get-login-password --region us-east-1 > docker-login.sh
chmod 777 docker-login.sh

###Creating a repo in AWS ECR###
aws ecr create-repository --repository-name cfn-stack-audit

###Build Dcoker image###
docker build -t cfn-stack-audit .
docker images
docker run cfn-stack-audit