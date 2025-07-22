from setuptools import setup, find_packages

setup(
    name="modelflow",
    version="0.1.0",
    description="Auto-generate HuggingFace model skeletons with deployment configs",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "transformers",
        "jinja2",
        "fastapi",
        "uvicorn"
    ],
    entry_points={
        "console_scripts": [
            "modelflow=modelflow.__main__:main"
        ]
    },
    python_requires=">=3.7",
) 