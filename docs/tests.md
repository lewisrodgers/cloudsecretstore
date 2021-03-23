# Tests

End-to-end tests are included in this test suite. They are marked with the pytest decorator `@pytest.mark.webrequest`.
When executed, it attempts to send authed web requests to Google Cloud APIs. As a result, there are a few sensitive
resources that you'll need to provide as environment variables before you can successfully run the tests.

- KEYFILE_PATH - The service account credentials JSON keyfile. This service account must have permissions
  like `roles/secretmanager.secretAccessor` to access secrets from Google Cloud Secret Manager.
- SECRET_RESOURCE_ID - The `SecretVersion` resource ID. See the following reference for steps on creating secrets and
  versions in Secret Manager: https://cloud.google.com/secret-manager/docs/creating-and-accessing-secrets
- SECRET_KEY_DATA - The contents of the secret. 

```shell
export KEYFILE_PATH=path/to/service_account_keyfile.json
export SECRET_RESOURCE_ID=projects/PROJECT_ID/secrets/SECRET_NAME/versions/VERSION
export SECRET_KEY_DATA=CONTENT
```

