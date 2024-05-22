import unittest
from mitlab_aiml_tools.auth.credential import CredentialServer

HOST = "192.168.190.150"
PORT = '50000'
HTTPS = False

ACCESS_KEY = 'test'
SECRET_KEY = 'test12345'


class TestCredentialManager(unittest.TestCase):

    def test_init(self):
        credential_manager = CredentialServer(
            host=HOST,
            port=PORT,
            access_key=ACCESS_KEY,
            secret_key=SECRET_KEY,
            https=HTTPS
        )
        print(credential_manager.credentials)


if __name__ == '__main__':
    unittest.main()
