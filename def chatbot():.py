from transformers import GPT2LMHeadModel, GPT2Tokenizer

def chatbot():
    print("Hello! I'm your chatbot. Ask me anything, or type 'exit' to end the conversation.")

    # Load pre-trained GPT-2 model and tokenizer
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day.")
            break
        
        response = generate_response(user_input, model, tokenizer)
        print("Chatbot:", response)

def generate_response(input_text, model, tokenizer):
    # Tokenize input text
    input_ids = tokenizer.encode(input_text, return_tensors="pt")

   
