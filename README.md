# Serverless Security Automation

There are a number of security solutions that require automated, repeatable tasks. These tasks are traditionally launched with server-based automation, such as a cron script on a dedicated server or a Jenkins instance. However, the creation of such infrastructure increases the attack surface in your environment, and requires server operations (e.g. patching, server maintenance). 

Serverless Security Automation provides a feature-rich serverless framework for security automation. It is based on the [Serverless AWS Python Scheduled Cron Example](https://github.com/serverless/examples/tree/master/aws-python-scheduled-cron) with extensions for error handling, secret management, and dependencies.

## Setup Serverless
[Install Node.js](https://nodejs.org/en/download/)

[Install Serverless](https://serverless.com/framework/docs/providers/aws/guide/installation/)

`$ npm install -g serverless`

## Deploy your first serverless instance
`$ serverless deploy`

> Note: if you are using IAM Roles with MFA, you may need to export your AWS environment variables using the [assume-role](https://github.com/remind101/assume-role/) package

>For example, `$ brew install remind101/formulae/assume-role` on Mac

>Then launch with `$ assume-role YOUR_ROLE && serverless deploy` where YOUR_ROLE is defined in your /.aws/config file

## Features

### Error Handling

Error Handling uses the [Serverless Plugin AWS Alerts](https://github.com/ACloudGuru/serverless-plugin-aws-alerts) plugin. 

`$ npm i serverless-plugin-aws-alerts`

### Python Requirements

Including Python requirements uses the [AWS Python Requirements](https://github.com/UnitedIncome/serverless-python-requirements) plugin. This also requires [Docker](https://www.docker.com/get-started) to be installed.

`$ sls plugin install -n serverless-python-requirements`


### Secret Manager

Secrets are stored using the [AWS Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html)