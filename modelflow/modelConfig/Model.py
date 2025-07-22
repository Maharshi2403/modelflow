import requests


# Model class 
class Model:

    def __init__(self, MODEL_NAME):
        self.model_name = MODEL_NAME
        self.model_logs  = self.GetModelConfig()
        
        self.SetModelConfig()
        # self.PrintConfigLogs()
        self.model_data()
        
        

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
            self.tags_list = [self.model_logs["tags"]]
        else:
            self.tags_list = "NULL"
        
        if self.model_logs.get("pipeline_tag"):
            self.pipeline_tags = self.model_logs["pipeline_tag"]
        else:
            self.pipeline_tags = "NULL"

        if self.model_logs.get("library_name"):
            self.library_name = self.model_logs["library_name"]
        else:
            self.library_name = "NULL"

        
        if self.model_logs.get("transformersInfo"):
            try:
                transformers_info = self.model_logs["transformersInfo"]
                self.auto_model = transformers_info.get("auto_model", None)  
                self.processor = transformers_info.get("processor", None)    
                if self.auto_model is None or self.processor is None:
                    print("Warning: One or both of 'auto_model' or 'processor' keys are missing in transformersInfo")
            except Exception as e:
                print(f"Exception in setting up transformersInfo: {e}")
                self.auto_model = None  
                self.processor = None   
        else:
            print("Warning: transformersInfo key not found in model_logs")
            self.auto_model = None
            self.processor = None

        if self.model_logs.get("config"):
        
            if self.library_name == 'transformers':
                self.architectures = [self.model_logs["config"]["architectures"]]
            
            
        if self.model_logs.get("usedStorage"):

            self.model_size = self.model_logs["usedStorage"]
        else:
            self.model_size = -1
   

            


    # Print logs info
    def PrintConfigLogs(self):
        print(f"MODEL_NAME: {self.model_name} \nTAGS_LIST: {self.tags_list} \nPIPELINE_TAGS: {self.pipeline_tags} \nLIBRARY_NAME: {self.library_name} \nAUTOMODEL_TYPE : {self.auto_model} \nPROCESSOR : {self.processor} \nARCHITECTURE : {self.architectures[0]} \nSIZE : {self.model_size/1024} KB/ {self.model_size/1073741824} GB")

    
    def model_list_support(self):
        

        try:

            res = requests.get("https://huggingface.co/api/models")

            if res.status_code==200:
                list = []
                count = 0
                index = 0
                for obj in res.json():
                    if(obj.get("library_name")=="transformers"):
                        list.append(obj["id"])
                        print(f"{obj["id"]} \n")
                        count = count + 1
                    index = index + 1
                print(count)
                print(index)
                
        except Exception as e:

            print(f"Exception call on model_list_support func- {e}")

    def model_data(self):
        model_config ={
            "model_name": self.model_name,
            "model_library": self.library_name,
            "tag_list": self.tags_list,
            "pipeline_tag": self.pipeline_tags,
            "auto_model": self.auto_model,
            "processor": self.processor,
            "model_size": self.model_size
        }
        return model_config

        


Model("parler-tts/parler-tts-mini-multilingual-v1.1")