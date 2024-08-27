import requests
from ..auth.credential import authenticated_only
from ..auth.credential import CredentialServer

MODEL_METRICS = {
    'classification': ['accuracy', 'precision', 'recall', 'f1_score', 'roc_auc'],
    'regression': ['mse', 'rmse', 'mae', 'r2_score'],
    'clustering': ['silhouette_score', 'davies_bouldin_score', 'adjusted_rand_index'],
    'ranking': ['ndcg', 'mean_reciprocal_rank', 'precision_at_k', 'average_precision'],
    'generative': ['inception_score', 'frechet_inception_distance', 'perceptual_loss']
}

class MetricUtility:
    """
        Add evaluation metrics for various types of models to mitlab server

        Attributes:
            credential_manager (class): credential manager for authenticatication
    """
    
    def __init__(self,
                 credential_manager: CredentialServer,
                 protocal,
                 host,
                 port,
                 api_prefix,
                 api_version,
                ):
        """

            Initialization for the File Utility

            Args:
                credential_manager (class): credential manager for authenticatication
                protocal (str): the protocal of file server
                host (str): the host of file server
                port (str): the port of file server
                api_prefix (str): the api prefix of file server
                api_version (str): the api version of file server
        """
        self.credential_manager = credential_manager if credential_manager is not None else ValueError(
            "credential_manager cannot be empty")
        self.protocal = protocal if protocal is not None else ValueError(
            "protocal cannot be empty")
        self.host = host if host is not None else (
            "host cannot be empty")
        self.port = port if port is not None else ValueError(
            "port cannot be empty")
        self.api_prefix = api_prefix if protocal is not None else ValueError(
            "api_prefix cannot be empty")
        self.api_version = api_version if protocal is not None else ValueError(
            "api_version cannot be empty")

    def _validate_type(self,value,expect_type):
        """
        Validate the type of a given value.

        Args:
            value: The value to check.
            expected_type: The type that value is expected to be.
    
        Returns:
            bool: True if the value matches the expected type.

        Raises:
            TypeError: If the value does not match the expected type.
        """

        if isinstance(value, expect_type):
            return True
        else:
            raise TypeError(f"Expected type {expect_type.__name__}, but got type {type(value).__name__}")


    def _validate_metric(self, model_type:str , metric:dict):
        """
        Validate that all keys in the given metrics dictionary are valid for the specified model type.

        Args:
            model_type (str): The type of the model (e.g., 'classification', 'regression').
            metrics (dict): A dictionary where keys are metrics to validate.

        Returns:
            bool: True if all keys in the metrics dictionary are valid for the model type.
    
        Raises:
            ValueError: If the model_type is not valid or if any key in the metrics dictionary is not valid.
        """

        if model_type not in MODEL_METRICS:
            raise ValueError(f"Invalid model_type '{model_type}'. Allowed types are {', '.join(MODEL_METRICS.keys())}.")

        for metric_key in metric.keys():
            if metric_key not in MODEL_METRICS[model_type]:
                raise ValueError(f"Invalid metric '{metric_key}' for model_type '{model_type}'. Allowed metrics are {', '.join(MODEL_METRICS[model_type])}.")
    
        return True

    @authenticated_only
    def upload_accuracy( self , model_uid:str , model_accuracy:float ):
        """
            Create generalize model metrics according to the model type.

            Args:
                model_uid(str):Model's unique id.
                model_accuracy(float):model performance.

            Return:
                function status string.

        """
        
        try:
            
            self._validate_type(model_uid,str)
            self._validate_type(model_accuracy,float)
            #print(f"http://{self.host}:{self.port}/{self.api_prefix}/{self.api_version}/ModelMetadataWriter/update")
            response = requests.post(
                url=f"http://{self.host}:{self.port}/{self.api_prefix}/{self.api_version}/ModelAccuracyManager/create",
                json={
                    "model_uid": model_uid,
                    "model_accuracy":model_accuracy
                    },
            )

            if response.status_code == 200:
                return "Create performance successfully."
            else:
                return f"""Fail to create performance.error code:{response.status_code}"""

        except Exception as e:
            return str(e)


    # @authenticated_only
    # def create_model_metrics( self , model_type:str , model_uid:str , metric:dict ):
    #     """
    #         Create generalize model metrics according to the model type.

    #         Args:
    #             model_type(str):Allow type:classification,regression,clustering,ranking,generative.
    #             model_uid(str):Model's unique id.
    #             metric(dictionary):Only accept platform-defined model metrics.

    #     """
        
        
    #     try:

    #         self._validate_metric( model_type=model_type , metric=metric )
            
    #         response = requests.post(
    #             url=f"{self.protocal}://{self.host}:{self.port}/{self.api_prefix}/{self.api_version}/pipeline_operation/ModelAccuracyManager/create",
    #             payload={
    #                 "model_uid": model_uid,
    #                 "model_accuracy":metric
    #                 },
    #         )

    #         if response.status_code == 200:
    #             return "Create performance successfully"
    #         else:
    #             return "Create performance failed"

    #     except Exception as e:
    #         return str(e)




