If you have the aws cli and aws SAm please skip to step three of cloning the repository.

### Please follow the guidelines...

### 1. Install AWS cli
    PLease follow the instructions : https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

### 2. Install Sam Cli
    PLease follow the instructions : https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html

### 3. Clone the repository and work from a different branch
    git clone git@github.com:bamboohealth/cfn-stacks.git

### 4. Copy the collwing commands in to the terminal. Please take note of the ecr repo created for it would be needed in the next step.
    chmod 777 lambda-build.sh
    ./lambda-build.sh

### 5. Sign into AWS and locate the ECR and follow the instructions. Take a note of the ECR Image URI as is it needed in the last step

### 6. Open a new terminal in the CFN-Stacks folder and make sure youre in the correct aws account by running the ASP Command and the desired account label.

### 7. Paste the follwing commands into your terminal. It would ask you to 
    sam build
    sam deploy --stack-name cfn-audit-stack -g

