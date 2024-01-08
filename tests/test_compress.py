import unittest
from mitlab_aiml_tools.pipeline.compress import CompressionUtility

ARCHIVE_FILE_PATH = './tests/compressed_dataset.tar.gz'
SOURCE_FOLDER_PATH = './tests/dataset'
TARGET_FOLDER_PATH = './tests/decompressed_dataset'


class TestCompressUtility(unittest.TestCase):

    def test_compress(self):
        CompressionUtility.compress(
            input_path=SOURCE_FOLDER_PATH, output_path=ARCHIVE_FILE_PATH)

    def test_decompress(self):
        CompressionUtility.decompress(
            input_path=TARGET_FOLDER_PATH, output_path=TARGET_FOLDER_PATH)


if __name__ == '__main__':
    unittest.main()
