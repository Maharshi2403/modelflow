import argparse
import os
from jinja2 import Environment, FileSystemLoader
from modelflow.modelConfig.Model import Model

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "templates")

def render_template(template_name, context, output_path):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(template_name)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(template.render(context))

def main():
    parser = argparse.ArgumentParser(description="ModelFlow CLI")
    parser.add_argument("generate", nargs="?", help="Generate model skeleton")
    parser.add_argument("--modelid", type=str, required=True, help="Model ID (used for folder name)")
    parser.add_argument("--base_model", type=str, default="PreTrainedModel", help="Base model class")
    parser.add_argument("--base_tokenizer", type=str, default="PreTrainedTokenizer", help="Base tokenizer class")
    parser.add_argument("--output_dir", type=str, default=None, help="Output directory (default: modelid)")
    # Add more arguments as needed

    args = parser.parse_args()

    if args.generate:
        output_dir = args.output_dir or args.modelid
        os.makedirs(output_dir, exist_ok=True)
        
        model = Model(args.modelid)
        model_config = model.model_data()
        # Context for templates
        context = {
            "model_name": args.modelid,
            "model_data": model_config,
            "project_name": args.output_dir,
            
            # Add more context fields as needed
        }
        



        # Generate files from templates
        render_template("model.py.j2", context, os.path.join(output_dir, "Model.py"))
        render_template("requirements.txt.j2", context, os.path.join(output_dir, "requirements.txt"))
        render_template("api.py.j2", context, os.path.join(output_dir, "api.py"))
        render_template("Dockerfile.j2", context, os.path.join(output_dir, "Dockerfile"))
        render_template("dockerignore.j2", context, os.path.join(output_dir, ".dockerignore"))
        render_template("model_log.j2", context, os.path.join(output_dir, "model_log"))
        render_template(".env.j2", context, os.path.join(output_dir, ".env"))
        render_template(".gitignore.j2", context, os.path.join(output_dir, ".gitignore"))
        render_template("Readme.txt.j2", context, os.path.join(output_dir, "Readme.txt"))
        

        print(f"Generated model skeleton in: {output_dir}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 