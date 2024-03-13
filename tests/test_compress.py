import unittest
from mitlab_aiml_tools.pipeline.compress import CompressionUtility

COMPRESSED_FILE_PATH = './tests/compressed_dataset.zip'
SOURCE_FOLDER_PATH = './tests/dataset'
EXTRACT_PATH = './tests/decompressed_dataset'


class TestCompressUtility(unittest.TestCase):

    def test_compress(self):
        CompressionUtility.compress(
            source_path=SOURCE_FOLDER_PATH, compressed_file_path=COMPRESSED_FILE_PATH
        )

    def test_decompress(self):
        CompressionUtility.decompress(
            compressed_file_path=COMPRESSED_FILE_PATH, extract_path=EXTRACT_PATH
        )


if __name__ == '__main__':
    unittest.main()
