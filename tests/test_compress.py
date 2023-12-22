import unittest
from mitlab_aiml_tools.pipeline.compress import CompressionUtility

ARCHIVE_FILE_PATH = './packet.tar.gz'
SOURCE_FOLDER_PATH = './docs'
TARGET_FOLDER_PATH = './'

compress_manager = CompressionUtility(archive_name=ARCHIVE_FILE_PATH)


class TestCompressUtility(unittest.TestCase):

    def test_compress(self):
        compress_manager.compress(source_folder=SOURCE_FOLDER_PATH)

    def test_decompress(self):
        compress_manager.decompress(target_folder=TARGET_FOLDER_PATH)


if __name__ == '__main__':
    unittest.main()
