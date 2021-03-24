from __future__ import annotations

from typing import Optional, Callable

from google.cloud import secretmanager
from google.oauth2 import service_account

from secretstore.exceptions import InvalidInputError


class SecretStore:
    def __init__(self, credentials: Optional[dict] = None) -> None:
        """
        :param credentials: Service account key info. The service account should have permissions to access the secrets.
            For example, the `roles/secretmanager.secretAccessor` role. If no credentials are provided, it will attempt
            to ascertain the credentials from the environment.
        """
        self._credentials = None
        if credentials:
            self._credentials = service_account.Credentials.from_service_account_info(credentials)
        self._client = secretmanager.SecretManagerServiceClient(credentials=self._credentials)
        self._resp: Optional[object] = None
        self._key: Optional[str] = None
        self._resource_id: Optional[str] = None

    @property
    def resp(self):
        return self._resp

    @resp.setter
    def resp(self, req):
        try:
            self._resp = req()
        except Exception as e:
            raise InvalidInputError(e)

    @property
    def key_data(self):
        if self.resp:
            return self.resp.payload.data.decode("utf-8")

    def resource_id(self, resource_id: str) -> SecretStore:
        """
        :param resource_id: In the format 'projects/*/secrets/*/versions/*'
        """
        self._resource_id = resource_id
        return self

    def fetch(self):
        self.resp = self._fetch_secret()

    def _fetch_secret(self) -> Callable:
        def deferred_request():
            return self._client.access_secret_version(name=self._resource_id)

        return deferred_request
