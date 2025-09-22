#!/usr/bin/env python3
"""
Test script specifically for the high-quality training questions
Loads and tests the model with sample questions from train_questions.txt
"""

import os
import pickle
from contextlib import nullcontext
import torch
import tiktoken
from model import GPTConfig, GPT

def load_model(model_dir='models'):
    """Load the trained cybersecurity model"""
    
    # Check if model exists, fallback to fast model if enhanced not ready
    ckpt_path = os.path.join(model_dir, 'ckpt.pt')
    if not os.path.exists(ckpt_path):
        print(f"Enhanced model not found at {ckpt_path}")
        model_dir = 'models'
        ckpt_path = os.path.join(model_dir, 'ckpt.pt')
        if not os.path.exists(ckpt_path):
            print(f"No model checkpoint found at {ckpt_path}")
            print("Please train the model first.")
            return None, None, None
    
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
    
    print(f"Model loaded successfully from {model_dir}!")
    print(f"Model parameters: {sum(p.numel() for p in model.parameters())/1e6:.2f}M")
    
    return model, enc, device

def generate_response(model, encoder, device, prompt, max_new_tokens=150, temperature=0.7):
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

def test_training_questions():
    """Test with the high-quality training questions"""
    
    print("Loading cybersecurity chatbot...")
    model, encoder, device = load_model()
    
    if model is None:
        return
    
    # Sample questions from the training set
    test_questions = [
        "What is this Cybersecurity Prompt Model trained for?",
        "Is it legal to run scans on random servers?",
        "Give me an example template for a service discovery scan (authorized lab only).",
        "How do I interpret an nmap result that shows port 22 open with an SSH server?",
        "What is a safe example of a generic command template for web server scanning?",
        "Show me a sample labeled log entry example.",
        "How should command autocompletions handle sensitive info?",
        "Example: I have a suspicious access pattern — what first steps do I take (investigative, non-intrusive)?",
        "How do I make the bot provide remediation recommendations rather than exploitation steps?"
    ]
    
    print("\n" + "="*70)
    print("TESTING CYBERSECURITY CHATBOT WITH HIGH-QUALITY QUESTIONS")
    print("="*70)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\nTest {i}/{ len(test_questions)}:")
        print(f"Question: {question}")
        print("Answer: ", end="", flush=True)
        
        # Format question with special tokens
        formatted_question = f"<Q>{question}</Q>\n<A>"
        
        response = generate_response(model, encoder, device, formatted_question, max_new_tokens=200, temperature=0.6)
        
        # Extract answer
        if '<A>' in response:
            answer_part = response.split('<A>')[-1]
            if '</A>' in answer_part:
                answer_part = answer_part.split('</A>')[0]
            print(answer_part.strip())
        else:
            print(response[len(formatted_question):].strip())
        
        print("-" * 50)

def interactive_training_questions():
    """Interactive test with training question format"""
    
    print("Loading cybersecurity chatbot...")
    model, encoder, device = load_model()
    
    if model is None:
        return
    
    print("\n" + "="*50)
    print("CYBERSECURITY CHATBOT - TRAINING QUESTIONS MODE")
    print("="*50)
    print("Ask questions about ethical cybersecurity practices.")
    print("The model has been trained on high-quality Q&A pairs.")
    print("Type 'quit' to exit")
    print("="*50 + "\n")
    
    while True:
        try:
            user_input = input("User: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            # Format with special tokens
            formatted_question = f"<Q>{user_input}</Q>\n<A>"
            
            print("Bot: ", end="", flush=True)
            
            # Generate response
            response = generate_response(model, encoder, device, formatted_question, max_new_tokens=200, temperature=0.7)
            
            # Extract answer
            if '<A>' in response:
                answer_part = response.split('<A>')[-1]
                if '</A>' in answer_part:
                    answer_part = answer_part.split('</A>')[0]
                print(answer_part.strip())
            else:
                print(response[len(formatted_question):].strip())
            
            print()
            
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

def main():
    import sys
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            test_training_questions()
        elif sys.argv[1] == 'interactive':
            interactive_training_questions()
        else:
            print("Usage: python test_training_questions.py [test|interactive]")
    else:
        print("Choose mode:")
        print("1. Test with predefined questions (python test_training_questions.py test)")
        print("2. Interactive chat (python test_training_questions.py interactive)")
        choice = input("Enter choice (1 or 2): ").strip()
        if choice == '1':
            test_training_questions()
        elif choice == '2':
            interactive_training_questions()
        else:
            print("Invalid choice. Running test mode...")
            test_training_questions()

if __name__ == "__main__":
    main()