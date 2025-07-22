from huggingface_hub import login, HfApi, hf_hub_download
import json

# Initialize the Hugging Face API
api = HfApi()
model_id = "parler-tts/parler-tts-mini-multilingual-v1.1"  # Example model ID

# Option 1: Download tokenizer configuration file
tokenizer_config_path = hf_hub_download(repo_id=model_id, filename="tokenizer_config.json")
with open(tokenizer_config_path, "r", encoding="utf-8") as f:
    tokenizer_config = json.load(f)
    print(f"Tokenizer_config: {tokenizer_config}")
    

# Option 2: List all files in the model repository to find tokenizer-related files
files = api.list_repo_files(repo_id=model_id)
tokenizer_files = [f for f in files if "tokenizer" in f or f in ["vocab.txt", "merges.txt"]]
print("Tokenizer-related files:", tokenizer_files)


class Tokenizer:
    def __init__(self, MODEL_NAME):
        self.model_name = MODEL_NAME
        
