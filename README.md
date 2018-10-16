# Serverless Security Automation

There are a number of security solutions that require automated, repeatable tasks. These tasks are traditionally launched with server-based automation, such as a cron script on a dedicated server or a Jenkins instance. However, the creation of such infrastructure increases the attack surface in your environment, and requires server operations (e.g. patching, server maintenance). 

This repo provides a feature-rich serverless framework for security automation. It is based on the Serverless AWS Python Scheduled Cron Example [https://github.com/serverless/examples/tree/master/aws-python-scheduled-cron] with extensions for error handling, secret management, and dependencies.