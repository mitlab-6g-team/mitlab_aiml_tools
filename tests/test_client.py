import unittest
from mitlab_aiml_tools.auth.credential import CredentialServer

HOST = "140.118.122.164"
PORT = '34801'
HTTPS = False

ACCESS_KEY = 'user_1'
SECRET_KEY = 'test'


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
