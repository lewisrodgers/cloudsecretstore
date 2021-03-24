# Tests

End-to-end tests are included in this test suite. They are marked with the pytest decorator `@pytest.mark.webrequest`.
When executed, it attempts to send authed web requests to Google Cloud APIs. As a result, there are a few sensitive
resources that you'll need to provide as environment variables before you can successfully run the tests.

- PROJECT_ID - The ID of the project where your secrets live
- SECRET_NAME - The name of the secret
- SECRET_VERSION - The version of the secret
- KEY_DATA - The contents of the secret
- KEYFILE_PATH - The service account credentials JSON keyfile. This service account must have permissions
  like `roles/secretmanager.secretAccessor` to access secrets from Google Cloud Secret Manager.

```sh
export PROJECT_ID=PROJECT_ID
export SECRET_NAME=SECRET_NAME
export SECRET_VERSION=SECRET_VERSION
export KEY_DATA=CONTENT
export KEYFILE_PATH=path/to/service_account_keyfile.json
```
