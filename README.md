# Django Backend

A super-fast boilerplate building backend by Django.
This provides the system with REST API and Admin Site.

## Quick Start

### Requirements

#### Local

* Python3.10
* Pipenv

#### Deployment

* AWS Resources
* DockerHub Account

### Setup

Clone this repogitory.

Replace `example.com` with your custom domain on `nginx/project.conf`.

Add `.env` and prepare environment variables on it.
Minimum example:
```shell
DEBUG="True"
SECRET_KEY="<secret_key>"
```

Change the default value on `project/env.py` as needed.

Access `https://cognito-idp.<AWS_COGNITO_REGION>.amazonaws.com/<AWS_COGNITO_CLIENT_ID>/.well-known/jwks.json` and save it as `jwks.json`.

Install packages.

```shell
$ pipenv install
```

## Environment Variables

### For Django App

These variables should be set on `.env` as needed.
For more information please see:
  * https://docs.djangoproject.com/en/4.0/ref/settings/
  * https://django-environ.readthedocs.io/en/latest/

#### `DATABASE_URL`

Main database URL.

If blank is set or the value is invalid,
the program doesn't work as you expected.

Default: sqlite3

Format: `https://<host_name>`

#### `DEBUG`

Flag to enable debugging.

Default: False

#### `READONLY_DATABASE_URL`

Reader database URL.

If the value is invalid,
the program doesn't work as you expected.

if `READONLY_DATABASE_URL` is set,
use it as a reader URL and use `DATABASE_URL` as a writer URL.

Default: blank

#### `SECRET_KEY`

The secret key is a required variable.
Use for the BASIC authentication.

You can generate random secret key with

```shell
pipenv run python manage.py shell

>> from django.core.management.utils import get_random_secret_key
>> get_random_secret_key()
```

#### `SERVICE_CLIENT_URL`

The service client (site or app) URL.
The API allows CORS access from this site (when `DEBUG` is not True).

Default: `http://localhost`
Format: `https://<host_name>`

#### `SERVICE_SITE_URL`

The service (admin) site URL.
The backend system trusts CSRF token from this site.

Default: `http://localhost`
Format: `https://<hostname>`

#### `AWS_ACCESS_KEY_ID`

It is an access key ID of an AWS IAM user for programs.
When you use AWS cloud, this is required and is used for S3, SES, and Cognito.
You should set proper roles and policies for the user.

Default: blank

#### `AWS_SECRET_ACCESS_KEY`

The secret key of an AWS IAM user with `AWS_ACCESS_KEY_ID`.
It is required if `AWS_ACCESS_KEY_ID` exists.

Default: blank

#### `AWS_S3_BUCKET`

AWS S3 bucket name.

Default: blank

#### `AWS_S3_CUSTOM_DOMAIN`

AWS S3 accessible domain (hostname).
Set the alias domain, if you use AWS CloudFront.

Default: blank

#### `DEFAULT_EMAIL`

Programs send email from this email with AWS SES.
If it is blank, use `django.core.mail.backends.console.EmailBackend`.

Default: blank

#### `AWS_COGNITO_POOL_ID`

AWS Cognito pool ID use for authentication.

Default: blank

#### `AWS_COGNITO_CLIENT_ID`

AWS Cognito client ID use for authentication.

Default: blank

### For Deployment

These variables are required when deploying.
Please set on your deploying system.

#### `AWS_ACCOUNT_ID`

Your AWS Account ID.

#### `CPU`

The number of CPU units used by the AWS ECS task.

#### `DOCKER_HUB_ID`

The user ID for logging in DockerHub.

#### `DOCKER_HUB_PASSWORD`

The password for logging in DockerHub.

#### `GUNICORN_WORKERS`

The number of gunicorn workers.
It is recommended to set about (CPU_CORES_NUM * 2 + 1).

#### `JWKS_JSON`

The jwks json data for AWS Cogntio authentication.
Access `https://cognito-idp.<AWS_COGNITO_REGION>.amazonaws.com/<AWS_COGNITO_CLIENT_ID>/.well-known/jwks.json` and copy it.

#### `MEMORY`

The amount (in MiB) of memory used by the AWS ECS task.

#### `NGINX_IMAGE_REPO_NAME`

The AWS ECR repogitory name for the nginx containers.

#### `NGINX_LOG_GROUP`

The AWS CloudWatchLogs log group name watching the nginx containers.

#### `UBUNTU_IMAGE_REPO_NAME`

The AWS ECR repogitory name for the ubuntu containers.

#### `UBUNTU_LOG_GROUP`

The AWS CloudWatchLogs log group name watching the ubuntu containers.

#### `TASK_EXECUTION_ROLE_NAME`

The AWS ECS task execution role name.

#### `TASK_FAMILY_NAME`

The AWS ECS taskdefinition family name.

#### `TASK_ROLE_NAME`

The AWS ECS task role name.

## Features

### Code Checkers

```shell
$ pipenv run flake8 .
$ pipenv run isort .
$ pipenv run black .
$ pipenv run mypy .
$ pipenv run pytest .
```

### Subdomain Support

API: `api.*.example.com`
Admin Site: `admin.*.example.com`

### S3 + CloudFront filestorage

It enables to put and read the static or media files on AWS S3.

### Cognito Authentication

It enables to authenticate with AWS Cognito.


### SES Mail sending

It enables to send mail with AWS SES.

### Others

* Custom base model
* Custom user model ...etc
