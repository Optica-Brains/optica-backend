# Optica Deliveries Backend

**Optica Deliveries Backend** This is a backend for the Optica APIs General

## REQUIREMENTS
### Prerequisites
* Python3.5 and above
* Python Django==3.0.2
* PostgreSQL
* Then install the various packages from requirements.txt `pip install -r requirements.txt`
* Create environment variables

## ENVIRONMENT VARIABLES
```
[VERSION]
OPTICAAPI_VERSION=v1.0.0

[DEV_DB]
PRIMARY_DB=
PRIMARY_DB_USER=
PRIMARY_DB_USER_PASSWORD=
PRIMARY_DB_HOST=localhost
PRIMARY_DB_PORT=5432

[PROD_DB]
SECONDARY_DB=
SECONDARY_USER=
SECONDARY_USER_PASSWORD=
SECONDARY_HOST=localhost
SECONDARY_PORT=5432

[ADMIN]
ADMIN_NAME=Optica Brains
ADMIN_EMAIL_ADDRESS=optica@example.com

[EMAIL_DETAILS]
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
SECURITY_EMAIL_SENDER=

[ENVIRONMENT_DETAILS]
ENVIRONMENT_NAME=Optica Brains

[COMMON_API_CREDS]
KEY=
COMMON_API_KEY=
COMMON_API_SECRET=

```

Meta
----
Author:
   * **Joseph Wambua ** - *Initial work* - [mutuajoseph](https://github.com/mutuajoseph)


Status:
    maintained, and is currently in development

Version:
    v1.0.0

Django Version:
    v1.9, v1.10, v1.11, v2.0, v2.1, 3.0 and greater

Python Version:
    3.5, 3.6, 3.7 (tested); 2.7, 3.4 (assumed)



Usage
-----
This is the backend system responsible for exposing the APIs to the frontend system.

## License
This project is licensed under the MIT License

Documentation
-------------
You can see the documentation over at **Read the Docs**

Resources
-------------
* https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f
* https://docs.djangoproject.com/en/3.0/
* https://www.django-rest-framework.org/
* https://www.postgresql.org/
* https://django-oauth-toolkit.readthedocs.io/en/latest/
* https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/rest-framework.html