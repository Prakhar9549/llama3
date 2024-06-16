# llama3

Follow these steps to install the required libraries and download the model:

-> pip install huggingface-hub

-> huggingface-cli download meta-llama/Meta-Llama-3-8B-Instruct --include "original/*" --local-dir meta-llama/Meta-Llama-3-8B-Instruct

-> pip install -U transformers --upgrade

-> pip install accelerate

After installing these libraries run the llama python file using the following below command:
Before we run the script, let’s make sure we can access and interact with Hugging Face directly from the terminal. To do that, make sure you have the Hugging Face CLI installed:
-> pip install -U "huggingface_hub[cli]"

-> huggingface-cli login

Here, it will ask us for our access token which we can get from our HF account under Settings. Copy it and provide it in the command line. We are now all set to run our script.

-> python llama.py
