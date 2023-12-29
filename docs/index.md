- ### File Access:
    File system download and upload functionality **(authentication required)**.
    ```
    Handling the upload and download function for the file server

    Attributes:
        credential_manager (class): credential manager for authenticatication
        protocal (str): the protocal of file server
        host (str): the host of file server
        port (str): the port of file server
        api_prefix (str): the api prefix of file server
        api_version (str): the api version of file server
    
    Args: 
        file_type (str): the type of the file
        uid (str): the UID value for the file
        file (file): the file that needed to upload
    ```

    ```
    from mitlab_aiml_tools.auth.credential import CredentialServer
    from mitlab_aiml_tools.pipeline.file import FileUtility

    <!-- Initialization -->
    credential_server = CredentialServer(
          host='<Credential Server IP>',
          port='<Credential Server Port>',
          access_key=<Credential Access Key>,
          secret_key=<<Credential Secret Key>>
        )

    file_manager = FileUtility(credential_manager=credential_server)


    <!-- Usage -->

    # download file
    downloaded_file = file_manager.download(
        file_type='model',
        uid='bbde5274-3d13-4f99-8b08-23cb7639c64c'
    )

    # upload file
    file_manager.upload(
        file_type='model',
        uid='bbde5274-3d13-4f99-8b08-23cb7639c64c',
        file=<File>
    )
    ```

- ### Compress
    Responsible for file compression and decompression.
    ```
    Handling the file compression and decompression

    Attributes:
        archive_name (str): the file name that need to compress or decompress
    
    Args: 
        source_folder (str): the source folder path that need to compress
        target_folder (str): the target folder that need extract the file

    ```

    ```
    from mitlab_aiml_tools.pipeline.compress import CompressionUtility

    <!-- Initialization -->
    compress_manager = CompressionUtility(archive_name=ARCHIVE_FILE_PATH)

    <!-- Usage -->

    # Compress files
     compress_manager.compress(source_folder=SOURCE_FOLDER_PATH)

    # Decompress file
     compress_manager.decompress(target_folder=TARGET_FOLDER_PATH)
    
    ```

- ### Logging:
    Converting text logs into log files and storing them in the file system **(authentication required)**.

    ```
    Handling the conversion of string to logs file and upload logs file to file server

        Attributes:
            credential_manager (class): credential manager for authenticatication
            log_file_path (str): the logs file_path

        Args: 
            input_string (str): the input strining need to convert to logs file
    ```

    ```
    from mitlab_aiml_tools.auth.credential import CredentialServer
    from mitlab_aiml_tools.pipeline.logging import LogsConverter

    <!-- Initialization -->
    LOGS_FILE_PATH = "./tests/logs/test_logs.txt"

        credential_server = CredentialServer(
          host='<Credential Server IP>',
          port='<Credential Server Port>',
          access_key=<Credential Access Key>,
          secret_key=<<Credential Secret Key>>
        )

    logs_converter = LogsConverter(
        credential_manager=credential_server, log_file_path=LOGS_FILE_PATH)

    <!-- Usage -->

    # Covert string to log file
     logs_converter.convert(TEST_LOG_CONTENT)
    ```