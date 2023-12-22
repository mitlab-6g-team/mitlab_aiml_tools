import zipfile
import os


class CompressionUtility:
    """
        Handling the file compression and decompression

        Attributes:
            archive_name (str): the file name that need to compress or decompress
    """

    def __init__(self, archive_name):
        """
            Initialization for the Compression Utility

            Args:
                archive_name (str): the output file name
        """
        self.archive_name = archive_name

    def compress(self, source_folder):
        """
            Compress all the file in the folder

            Args:
                source_folder (str): the source folder path that need to compress

            Returns:
                (Success): "Compress successfully"
                (Exception): <Error Message>  
        """
        try:
            with zipfile.ZipFile(self.archive_name, 'w') as zip_file:
                for foldername, subfolders, filenames in os.walk(source_folder):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        arcname = os.path.relpath(file_path, source_folder)
                        zip_file.write(file_path, arcname)
            return "Compression successfully"
        except Exception as error:
            return str(error)

    def decompress(self, target_folder):
        """
            Decompress file to folder

            Args:
                target_folder (str): the target folder that need extract the file

            Returns:
                (Success): "Decompress successfully"
                (Exception): <Error Message>  
        """
        try:
            with zipfile.ZipFile(self.archive_name, 'r') as zip_file:
                zip_file.extractall(target_folder)
        except Exception as error:
            return str(error)
