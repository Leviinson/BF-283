# ZohoCRM API

- [Installation](#install)
- [Containers](#containers)

## Install

### Sensitive data

1. .env file must be created locally and filled with sensitive info:

```bash
Django      SECRET_KEY

Zoho        ZOHO_CLIENT_ID
            ZOHO_CLIENT_SECRET
            GRANT_TOKEN
            ZOHO_REDIRECT_URI
            ZOHO_CURRENT_USER_EMAIL
            ZOHO_LOGGER_PATH
            ZOHO_RESOURCE_PATH

MySQL       MYSQL_DATABASE
            MYSQL_USER
            MYSQL_PASSWORD
            MYSQL_HOST
            MYSQL_PORT
            MYSQL_ROOT_PASSWORD

SMTP_SERVER MAIL_USERNAME
            MAIL_PASSWORD
            MAIL_PORT
            MAIL_SERVER
```

### API authorization tokens

1. GRANT_TOKEN have to be created in [Zoho Dev Console](https://api-console.zoho.eu/) for Self-Client application and placed in .env file either.

2. Scope for GRANT_TOKEN obtaining is ZohoCRM.settings.ALL,ZohoCRM.modules.ALL,ZohoCRM.coql.READ

3. Triggering mentioned above URL creates access and refresh tokens and place them in storage.

4. **Model** **ZohoOAuth** class for tokens data storage is placed in zoho_token/models.py;

   **ZohoOAuthHandler**, **ZohoOAuthInitializer** are placed in zoho_token/utils.py;

   **set_zoho_token** **CLI** is placed in zoho_token/management/commands/set_zoho_tokens.py.

5. For successfull receiving first tokens data using GRANT_TOKEN:
    - place new GRANT_TOKEN in .env file (for receiving it use
      ZohoCRM.modules.ALL,ZohoCRM.settings.ALL.ZohoCRM.coql.READ scope for all permissions);
    - make sure last changes in .env file had taken into account;
    - execute command: 
    
    `sudo docker compose --env-file .env up`

---

## Containers


## MySQL Docker Image

To build MySQL image for our application - you have to download docker and it utility docker-compose.

## Usage

### Building the Image

To build the Docker image, navigate to the directory containing the "docker-compose.yml".

The next variables from .env file in root directory of the project will be used:

- MYSQL_DATABASE
- MYSQL_USER
- MYSQL_PASSWORD
- MYSQL_ROOT_PASSWORD
- MYSQL_HOST
- MYSQL_PORT

---

### Installing questions


1. To make some operations with created mysql db use commands in terminal:

    `sudo docker exec -it bf-mysql-1.0 mysql`

2. To install pre-commit hooks functionality for development run command
    - pre-commit install
   This will install configuration file .pre-commit-config.yaml settings in
    .git/hooks/pre-commit

### Running the Container

To run the MySQL container, you can use the following command:

```bash
docker-compose --env-file ../.env up -d
```

Now the MySQL server inside the container will be accessible on port specified in .env file with variable MYSQL_EXTERNAL_PORT.

## Adding content to Zoho CRM.

1. Adding new country we should check config.constants.Constants.LANGUAGE_IDENTIFIERS_DICT
    for presence country identifier.

## Maintainance

### Caching

1. All caching operations are implemented in data_getters modules, that are represented in
    project services package and app_services packages. Because of that all caching time
    settings can be found and changed there.
2. If there is a need to add caching to some fetching data, it must be performed in described
    above data_getters modules.
