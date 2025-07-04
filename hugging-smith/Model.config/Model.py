import requests
from typing import  List

# Model class 
class Model:

    def __init__(self, MODEL_NAME):
        self.model_name = MODEL_NAME
        self.model_logs  = self.GetModelConfig()
        
        self.SetModelConfig()
        self.PrintConfigLogs()

    # Request huggingface endpoint to get model config
    def GetModelConfig(self):

        try:
            response = requests.get(f"https://huggingface.co/api/models/{self.model_name}")

            if(response.status_code == 200):
                model_logs = response.json()
                
                return model_logs
            else:
                return "Huggingface is not Accesible. Internal Error!"

        except Exception as e:
            print(f"Exception occored: {e}")
            return e
        


    # Set model config fields
    def SetModelConfig(self):
        if self.model_logs.get("tags"):
            self.tags_list = List[self.model_logs["tags"]]
        
        if self.model_logs.get("pipeline_tag"):
            self.pipeline_tags = self.model_logs["pipeline_tag"]

        if self.model_logs.get("library_name"):
            self.library_name = self.model_logs["library_name"]

        if self.model_logs.get("transformersInfo"):
            try:
                self.auto_model = self.model_logs["transformersInfo"]["auto_model"]
                self.processor = self.model_logs["transformersInfo"]["processor"]
            except Exception as e:

                print(f"Exception in Setting up transformersInfo: {e}")
        else:
            self.auto_model = "NULL"
            self.processor = "NULL"



    # Print logs info
    def PrintConfigLogs(self):
        print(f"MODEL_NAME: {self.model_name} \nTAGS_LIST: {self.tags_list} \nPIPELINE_TAGS: {self.pipeline_tags} \nLIBRARY_NAME: {self.library_name} \nAUTOMODEL_TYPE : {self.auto_model} \nPROCESSOR : {self.processor} ")

Model("black-forest-labs/FLUX.1-Kontext-dev")