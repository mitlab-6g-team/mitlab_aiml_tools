import unittest
from mitlab_aiml_tools.auth.credential import CredentialServer
from mitlab_aiml_tools.pipeline.metrics import MetricUtility


######################## Credential server ########################
CREDENTIAL_SERVER_HOST = '140.118.122.246'
CREDENTIAL_SERVER_PORT = '50000'
CREDENTIAL_ACCESS_KEY = 'user1'
CREDENTIAL_SECRET_KEY = 'test'
PROTOCAL=False
API_PREFIX='entrypoint'
API_VERSION='v1.1.1'

############################ fake data ############################
MODEL_UID="e414863c-50cc-4004-9bb8-93d4bccbb6ae"
MODEL_ACCURACY=0.95

credential_server = CredentialServer(
    host=CREDENTIAL_SERVER_HOST,
    port=CREDENTIAL_SERVER_PORT,
    access_key=CREDENTIAL_ACCESS_KEY,
    secret_key=CREDENTIAL_SECRET_KEY
)

metric_manager = MetricUtility(
        credential_manager=credential_server,
    )

class TestFileUtility(unittest.TestCase):
    def test_upload_model_accuracy(self):
        response = metric_manager.upload_accuracy(
            model_uid=MODEL_UID,
            model_accuracy=MODEL_ACCURACY,
        )
        print(response)

if __name__=='__main__':
    unittest.main()