# Usage of the application

After the application is build and deployed successfully, we can focus on the credentials and access control.

<!-- TOC -->

* [Usage of the application](#usage-of-the-application)
    * [Config files](#config-files)
    * [Environment variables](#environment-variables)

<!-- TOC -->

### Config files

This is an example of yaml file configuration for local deployment.

```yaml
accessTokens:  # Access tokens

accessCredentials: # Credentials
  mongoDB: # Credentials for mongoDB
    mongoDB_password: "Password"
    mongoDB_username: "Username"
    mongoDB_auth_db: "Admin"

  mongoDB-Express: # Credentials for mongoDB Expess
    mongoDB-Express_username: "Username"
    mongoDB-Express_password: "Password"

deploymentParameters: # Parameters for deployment
  mongoDB: # Deployment parameters for mongoDB
    mongoDB_ports: 27017
```

You should replace the fields with the correct information.

It should be for now present in the Collector directory, so the master can access it and successfully deploy.

### Environment variables

It's important to export the environmental variables so the docker-compose can use them. Make sure the name is correct for them or deploying the
service will fail.

Feel free to add this to your **.bashrc** or .**zshrc** file.

```bash
export MONGO_DB_USER="YOUR_VALUE"
export MONGO_DB_PASS="YOUR_VALUE"
export MONGO_DB_PORT_INBOUND="YOUR_VALUE"
export MONGO_DB_PORT_OUTBOUND="YOUR_VALUE"
```