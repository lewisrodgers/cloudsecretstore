# Usage

This module expects a set of credentials so that it can authenticate with Google Cloud. These credentials belong to a member that has
permission to access secrets from Secret Manager (e.g., Owner, Secret Manager Admin, etc.).

Import the service.

```python
from cloudsecretstore import SecretStore
```

See the "Quick start" section in the [README](../README.md) to set your application default credentials.

Initialize the service and allow it to find the credentials from the environment.

```python
secret = SecretStore()
```

Or, explicitly provide service account credentials. 

```python
path_to_creds = "path/to/keyfile.json"
secret = SecretStore(path_to_creds)
```

Then, fetch a secret...

```python
RESOURCE_ID = "projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION"
data = secret.resource_id(RESOURCE_ID).fetch()
```
