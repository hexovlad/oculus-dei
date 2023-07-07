# Usage of the application
After the application is build and deployed successfully, we can focus on the credentials and access control.

<!-- TOC -->
* [Usage of the application](#usage-of-the-application)
    * [Config files](#config-files)
<!-- TOC -->

### Config files
This is an example of Docker yaml file configuration for local deployment.
```yaml
accessTokens:  # Access tokens

accessCredentials:  # Credentials
  mongoDB:          # Credentials for mongoDB
    mongoDB_password: "Password"
    mongoDB_username: "Username"
    mongoDB_auth_db: "Admin"

  mongoDB-Express:  # Credentials for mongoDB Expess
    mongoDB-Express_username: "Username"
    mongoDB-Express_password: "Password"

deploymentParameters:  # Parameters for deployment
  mongoDB:  # Deployment parameters for mongoDB
    mongoDB_ports: 27017
```
You should replace the fields with the correct information.