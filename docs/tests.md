# Tests

End-to-end tests are included in this test suite. They are marked with the pytest decorator `@pytest.mark.webrequest`.
When executed, it attempts to send authed web requests to Google Cloud APIs. As a result, there are a few sensitive
resources that you'll need to provide as environment variables before you can successfully run the tests.

```sh
# The ID of the project where your secrets live
export PROJECT_ID=PROJECT_ID

# The name of the secret
export SECRET_NAME=SECRET_NAME

# The version of the secret
export SECRET_VERSION=SECRET_VERSION

# The contents of the secret
export KEY_DATA=CONTENT

# The service account credentials JSON keyfile. This service account must have permissions
# like `roles/secretmanager.secretAccessor` to access secrets from Google Cloud Secret Manager.
export KEYFILE_PATH=path/to/service_account_keyfile.json
```
