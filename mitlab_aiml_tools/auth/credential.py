import requests
from mitlab_aiml_tools.pipeline.utils.config import config

class CredentialServer:
    """
    Handle credential management and authentication

    Attributes:
        host (str): the host for authentication server
        port (str): the authentication server port
        access_key (str): the access key for authentication
        secret_key (str): the secret key for authentication
        https (bool): decide the Https SSL/HLS protocol or not
        api_root (str): the root string of API
        api_version (str): the version of API
        api_prefix (str): the prefix of API
    """

    def __init__(self,
                 host, port=None,
                 access_key=None,
                 secret_key=None,
                 https=False,
                 api_version=config['AUTHENTICATE_MIDDLEWARE_SERVER_API_VERSION'],
                 api_prefix=config['AUTHENTICATE_MIDDLEWARE_SERVER_API_PREFIX'],
                 api_module_name=config['AUTHENTICATE_MIDDLEWARE_MODULE_NEME']):
        self.host = host
        self.port = port
        self.access_key = access_key
        self.secret_key = secret_key
        self.api_version = api_version
        self.api_prefix = api_prefix
        self.https = https
        self.api_module_name = api_module_name
        self._credentials = None
        self._authenticate()

    @property
    def credentials(self): return self._credentials

    def _authenticate(self):
        try:
            VALIDATOR_TYPE = 'AccountValidator'
            api_url = f'{"https" if self.https else "http"}://{self.host}{f":{self.port}" if self.port else ""}/{self.api_prefix}/{self.api_version}/{self.api_module_name}/{VALIDATOR_TYPE}/login'
            res = requests.post(
                url=api_url,
                json={"account_name": self.access_key,
                      "password": self.secret_key})
            if res.status_code == 200:
                print("great")
                self._credentials = res.json()
            else:
                raise PermissionError("Authentication failed")
        except Exception as error:
            raise PermissionError(f"Authentication error: {str(error)}")


def authenticated_only(func):
    def wrapper(self, *args, **kwargs):
        if self.credential_manager.credentials:
            return func(self, *args, **kwargs)
        else:
            raise PermissionError("Authentication required")
    return wrapper
