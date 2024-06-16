import transformers
import torch
from transformers import AutoTokenizer

# Specify the model
model = "meta-llama/Meta-Llama-3-8B-Instruct"

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained(model)

# Load the text generation pipeline
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

def chat_with_llama3():
    print("Chat with Llama-3. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Ending chat.")
            break
        sequences = pipeline(
            user_input,
            do_sample=True,
            top_k=10,
            num_return_sequences=1,
            eos_token_id=tokenizer.eos_token_id,
            truncation=True,
            max_length=400,
        )
        for seq in sequences:
            print(f"Llama-3: {seq['generated_text']}")

# Start the chat loop
chat_with_llama3()
