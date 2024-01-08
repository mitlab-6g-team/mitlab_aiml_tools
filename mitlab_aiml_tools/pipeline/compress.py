import zipfile
import os


class CompressionUtility:
    """
        Handling the file compression and decompression
    """

    @classmethod
    def compress(cls, input_path: str, output_path: str):
        """
            Compress all the file in the folder

            Args:
                input_path (str): the input folder path that need to compress
                output_path (str): the compressed file output path

            Returns:
                (Success): "Compress successfully"
                (Exception): <Error Message>  
        """
        try:
            with zipfile.ZipFile(input_path, 'w') as zip_file:
                for foldername, subfolders, filenames in os.walk(output_path):
                    for filename in filenames:
                        file_path = os.path.join(foldername, filename)
                        arcname = os.path.relpath(file_path, output_path)
                        zip_file.write(file_path, arcname)
            return "Compression successfully"
        except Exception as error:
            return str(error)

    @classmethod
    def decompress(cls, input_path: str, output_path: str):
        """
            Decompress file to folder

            Args:
                input_path (str): the input folder path that need to decompress
                output_path (str): the decompressed file output path

            Returns:
                (Success): "Decompress successfully"
                (Exception): <Error Message>  
        """
        try:
            with zipfile.ZipFile(input_path, 'r') as zip_file:
                zip_file.extractall(output_path)
        except Exception as error:
            return str(error)
