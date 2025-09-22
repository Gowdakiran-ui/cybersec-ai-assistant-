#!/usr/bin/env python3
"""
Test script for the cybersecurity chatbot
"""

import os
import pickle
from contextlib import nullcontext
import torch
import tiktoken
from model import GPTConfig, GPT

def load_model(model_dir='models'):
    """Load the trained cybersecurity model"""
    
    # Check if model exists
    ckpt_path = os.path.join(model_dir, 'ckpt.pt')
    if not os.path.exists(ckpt_path):
        print(f"No model checkpoint found at {ckpt_path}")
        print("Please train the model first using: python train.py config/train_cybersecurity.py")
        return None, None, None
    
    print(f"Loading model from {ckpt_path}")
    
    # Load checkpoint
    device = 'cpu'  # Always use CPU for inference
    checkpoint = torch.load(ckpt_path, map_location=device)
    
    # Create model
    gptconf = GPTConfig(**checkpoint['model_args'])
    model = GPT(gptconf)
    
    # Load state dict
    state_dict = checkpoint['model']
    unwanted_prefix = '_orig_mod.'
    for k,v in list(state_dict.items()):
        if k.startswith(unwanted_prefix):
            state_dict[k[len(unwanted_prefix):]] = state_dict.pop(k)
    model.load_state_dict(state_dict)
    
    model.eval()
    model.to(device)
    
    # Load encoder
    enc = tiktoken.get_encoding("gpt2")
    
    print(f"Model loaded successfully!")
    print(f"Model parameters: {sum(p.numel() for p in model.parameters())/1e6:.2f}M")
    
    return model, enc, device

def generate_response(model, encoder, device, prompt, max_new_tokens=100, temperature=0.8):
    """Generate a response from the model"""
    
    # Encode prompt
    start_ids = encoder.encode(prompt, allowed_special={"<|endoftext|>"})
    x = torch.tensor(start_ids, dtype=torch.long, device=device)[None, ...]
    
    # Generate
    ctx = nullcontext()
    with torch.no_grad():
        with ctx:
            y = model.generate(x, max_new_tokens, temperature=temperature, top_k=50)
            response = encoder.decode(y[0].tolist())
            
    return response

def interactive_chat():
    """Interactive chat with the cybersecurity bot"""
    
    print("Loading cybersecurity chatbot...")
    model, encoder, device = load_model()
    
    if model is None:
        return
    
    print("\n" + "="*50)
    print("CYBERSECURITY CHATBOT")
    print("="*50)
    print("Ask questions about penetration testing, Linux commands, nmap, etc.")
    print("Use format: <Q>Your question here</Q>")
    print("Type 'quit' to exit")
    print("="*50 + "\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            # Format input if not already formatted
            if not user_input.startswith('<Q>'):
                user_input = f"<Q>{user_input}</Q>\n<A>"
            
            print("Bot: ", end="", flush=True)
            
            # Generate response
            response = generate_response(model, encoder, device, user_input, max_new_tokens=150, temperature=0.7)
            
            # Extract just the answer part
            if '<A>' in response:
                answer_part = response.split('<A>')[-1]
                if '</A>' in answer_part:
                    answer_part = answer_part.split('</A>')[0]
                print(answer_part.strip())
            else:
                print(response[len(user_input):].strip())
            
            print()
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

def test_examples():
    """Test with predefined examples"""
    
    print("Loading cybersecurity chatbot...")
    model, encoder, device = load_model()
    
    if model is None:
        return
    
    examples = [
        "<Q>How do I scan for open ports?</Q>\n<A>",
        "<Q>Show me a reverse shell command</Q>\n<A>",
        "<Q>How do I find SUID binaries?</Q>\n<A>",
        "<Q>What's a good nmap command for stealth scanning?</Q>\n<A>",
        "<Q>How do I escalate privileges in Linux?</Q>\n<A>"
    ]
    
    print("\n" + "="*50)
    print("TESTING CYBERSECURITY CHATBOT")
    print("="*50)
    
    for i, example in enumerate(examples, 1):
        print(f"\nTest {i}:")
        print(f"Question: {example.split('</Q>')[0].replace('<Q>', '')}")
        print("Answer: ", end="", flush=True)
        
        response = generate_response(model, encoder, device, example, max_new_tokens=100, temperature=0.5)
        
        # Extract answer
        if '<A>' in response:
            answer_part = response.split('<A>')[-1]
            if '</A>' in answer_part:
                answer_part = answer_part.split('</A>')[0]
            print(answer_part.strip())
        else:
            print(response[len(example):].strip())
        
        print("-" * 30)

def main():
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_examples()
    else:
        interactive_chat()

if __name__ == "__main__":
    main()