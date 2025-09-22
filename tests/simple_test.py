#!/usr/bin/env python3
"""
Simple test to demonstrate the training with high-quality questions
"""

import os
import pickle
from contextlib import nullcontext
import torch
import tiktoken
from model import GPTConfig, GPT

def simple_test():
    """Simple test of the model"""
    
    # Load the model
    model_dir = 'models'
    ckpt_path = os.path.join(model_dir, 'ckpt.pt')
    
    if not os.path.exists(ckpt_path):
        print("No trained model found. Please wait for training to complete.")
        return
    
    print(f"Loading model from {ckpt_path}")
    
    # Load checkpoint
    device = 'cpu'
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
    
    print(f"Model loaded! Parameters: {sum(p.numel() for p in model.parameters())/1e6:.2f}M")
    
    # Test questions from your training file
    test_questions = [
        "<Q>Is it legal to run scans on random servers?</Q>\n<A>",
        "<Q>What is a safe example of a generic command template for web server scanning?</Q>\n<A>",
        "<Q>How should command autocompletions handle sensitive info?</Q>\n<A>"
    ]
    
    print("\n" + "="*60)
    print("TESTING WITH HIGH-QUALITY TRAINING QUESTIONS")
    print("="*60)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\nTest {i}:")
        q_text = question.split('</Q>')[0].replace('<Q>', '')
        print(f"Question: {q_text}")
        
        # Encode prompt
        start_ids = enc.encode(question, allowed_special={"<|endoftext|>"})
        x = torch.tensor(start_ids, dtype=torch.long, device=device)[None, ...]
        
        # Generate
        with torch.no_grad():
            y = model.generate(x, 100, temperature=0.6, top_k=50)
            response = enc.decode(y[0].tolist())
        
        # Extract answer
        if '<A>' in response:
            answer_part = response.split('<A>')[-1]
            if '</A>' in answer_part:
                answer_part = answer_part.split('</A>')[0]
            print(f"Answer: {answer_part.strip()}")
        else:
            print(f"Answer: {response[len(question):].strip()}")
        
        print("-" * 40)

if __name__ == "__main__":
    simple_test()