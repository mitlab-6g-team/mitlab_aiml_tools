import os
import zipfile


class CompressionUtility:
    """
        Handling the file compression and decompression
    """

    @classmethod
    def compress(cls, source_path: str, zip_file_path: str):
        """
            Compress all the file in the folder

            Args:
                source_path (str): the input path that need to compress
                zip_file_path (str): the compressed file output path

            Returns:
                (Success): "Compress successfully"
                (Exception): <Error Message>  
        """
        try:
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                if os.path.isdir(source_path):
                    for root, dirs, files in os.walk(source_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(
                                file_path, os.path.dirname(source_path))
                            zipf.write(file_path, arcname)
                elif os.path.isfile(source_path):
                    zipf.write(source_path, os.path.basename(source_path))
                else:
                    raise FileNotFoundError(f"Path not exist: {source_path}")
            return "Compress successfully"
        except Exception as error:
            return str(error)

    @classmethod
    def decompress(cls, zip_file_path: str, extract_path: str):
        """
            Decompress file to folder

            Args:
                zip_file_path (str): the zip file that need to decompress
                extract_path (str): the decompressed file output path

            Returns:
                (Success): "Decompress successfully"
                (Exception): <Error Message>  
        """
        try:
            if not os.path.isfile(zip_file_path):
                raise FileNotFoundError(f"zip file not exist: {zip_file_path}")

            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            return "Decompress successfully"
        except Exception as error:
            return str(error)
