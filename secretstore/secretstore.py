from typing import Optional

from google.cloud import secretmanager
from google.oauth2 import service_account


class SecretStore:
    def __init__(self, credentials: Optional[dict] = None) -> None:
        """
        :param credentials: Service account key info. The service account should have permissions to access the secrets.
            For example, the `roles/secretmanager.secretAccessor` role. If no credentials are provided, it will attempt
            to ascertain the credentials from the environment.
        """
        self.credentials = None
        if credentials:
            self.credentials = service_account.Credentials.from_service_account_info(credentials)
        self.client = secretmanager.SecretManagerServiceClient(credentials=self.credentials)

    def get_key_data(self, name: str) -> str:
        """
        :param name: Resource name of the secret version in the format 'projects/*/secrets/*/versions/*'
        :return: Content of the secret
        """
        resp = self.client.access_secret_version(name=name)
        return resp.payload.data.decode("utf-8")
