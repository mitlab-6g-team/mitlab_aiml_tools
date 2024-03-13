import unittest
from mitlab_aiml_tools.auth.credential import CredentialServer
from mitlab_aiml_tools.pipeline.logging import LogsConverter

# Credential server
CREDENTIAL_SERVER_HOST = '192.168.190.150'
CREDENTIAL_SERVER_PORT = '40678'
CREDENTIAL_ACCESS_KEY = 'test'
CREDENTIAL_SECRET_KEY = 'test12345'

# Test data
LOG_FILE_PATH = "./tests/log/test_log.txt"
TEST_LOG_CONTENT = "[INFO] time: 2023-11-23 12:14:04, module: pipeline_task, actor: PreprocessingTaskWorker, function: start, payload: {'preprocessing_pipeline_uid': '2979d7a4-7b98-49c2-b6b2-2bf0d6b5c1e9'}"

credential_server = CredentialServer(
    host=CREDENTIAL_SERVER_HOST,
    port=CREDENTIAL_SERVER_PORT,
    access_key=CREDENTIAL_ACCESS_KEY,
    secret_key=CREDENTIAL_SECRET_KEY
)

log_converter = LogsConverter(
    credential_manager=credential_server, log_file_path=LOG_FILE_PATH)


class TestLogsConverter(unittest.TestCase):
    def test_convert(self):
        res = log_converter.covert(TEST_LOG_CONTENT)
        print(res)


if __name__ == '__main__':
    unittest.main()
