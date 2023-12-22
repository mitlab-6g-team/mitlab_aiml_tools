import unittest
from mitlab_aiml_tools.auth.credential import CredentialManager

HOST = "192.168.190.150"
PORT = '40678'
API_ROOT = 'api'
API_VERSION = 'v0.1'
API_PREFIX = 'metadata'
HTTPS = False

ACCESS_KEY = 'test'
SECRET_KEY = 'test12345'


class TestCredentialManager(unittest.TestCase):

    def test_init(self):
        credential_manager = CredentialManager(
            host=HOST,
            port=PORT,
            api_root=API_ROOT,
            api_version=API_VERSION,
            api_prefix=API_PREFIX,
            access_key=ACCESS_KEY,
            secret_key=SECRET_KEY,
            https=HTTPS
        )
        print(credential_manager.credentials)


if __name__ == '__main__':
    unittest.main()
