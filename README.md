The Cloud Secret Store module fetches secrets from Google Cloud. It's an abstraction layer that wraps
the `google-cloud-secret-manager` client library.

# Quick start

## Authentication

There are a few ways of setting the credentials the service will use to authenticate with Google Cloud.

### OAuth2

Use `gcloud` to set the credentials by logging in as yourself.

```
gcloud auth application-default login
```

### Service Account

Provision a service account and keyfile. This service account should have a role
like `roles/secretmanager.secretAccessor`. Here's one way to do this with `gcloud`:

```
NAME=your_service_account_name
PROJECT_ID=your_project_id
FILE_NAME=your_filename

gcloud iam service-accounts create $NAME
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:$NAME@$PROJECT_ID.iam.gserviceaccount.com" --role="roles/secretmanager.secretAccessor"
gcloud iam service-accounts keys create $FILE_NAME.json --iam-account=$NAME@$PROJECT_ID.iam.gserviceaccount.com
```

Then, use `gcloud` to set the credentials by activating the service account. 

```
gcloud auth activate-service-account --key_file=path/to/keyfile.json
```

Continue to [docs/usage.md](docs/usage.md).
