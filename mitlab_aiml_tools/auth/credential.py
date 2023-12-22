import requests


class CredentialManager:
    """
        Handle file server client connection

        Attributes:
            endpoint (str): the endpoint for file server
            port (str): the file server port
            access_key (str): the access key for accessing file server identity
            secret_key (str): the secret key for verifying file server 
            https (bool): decide the Https SSL/HLS protocal or not
            credentials (str): the credentials for authentication

    """

    def __init__(self,
                 host,
                 port=None,
                 api_root='api',
                 api_version='v0.1',
                 api_prefix='metadata',
                 access_key=None,
                 secret_key=None,
                 https=False,
                 credentials=None):
        self.host = host
        self.port = port
        self.api_root = api_root
        self.api_version = api_version
        self.api_prefix = api_prefix
        self.access_key = access_key
        self.secret_key = secret_key
        self.credentials = credentials

        # Useless now
        self.https = https

        self._verify(access_key=access_key, secret_key=secret_key)

    def _verify(self, access_key: str, secret_key: str):
        try:
            VALIDATOR_TYPE = 'AccountValidator'
            api_url = f'{"https" if self.https else "http"}://{self.host}{f":{self.port}" if self.port else ""}/{self.api_root}/{self.api_version}/{self.api_prefix}/{VALIDATOR_TYPE}/login'
            res = requests.post(
                url=api_url,
                json={"account_name": access_key,
                      "account_password": secret_key})
            if res.status_code == 200:
                self.credentials = res.json()
        except Exception as error:
            return str(error)

    def _return_token(self, token):
        return token
