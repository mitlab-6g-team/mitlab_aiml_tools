import zipfile
import os


class CompressionUtility:
    def __init__(self, archive_name):
        self.archive_name = archive_name

    def compress(self, source_folder):
        """
            Compress all the file in the folder
        """
        with zipfile.ZipFile(self.archive_name, 'w') as zip_file:
            for foldername, subfolders, filenames in os.walk(source_folder):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    arcname = os.path.relpath(file_path, source_folder)
                    zip_file.write(file_path, arcname)

    def decompress(self, target_folder):
        """
            De-compress file to folder
        """
        with zipfile.ZipFile(self.archive_name, 'r') as zip_file:
            zip_file.extractall(target_folder)
