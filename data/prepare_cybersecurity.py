#!/usr/bin/env python3
"""
Prepare cybersecurity data for GPT training
Converts scraped data into the format needed by nanoGPT
"""

import os
import json
import pickle
import numpy as np
from typing import List, Dict
import tiktoken
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CybersecurityDataPrep:
    def __init__(self, data_dir="data/raw_data", output_dir="data/processed_data"):
        self.data_dir = data_dir
        self.output_dir = output_dir
        self.encoder = tiktoken.get_encoding("gpt2")
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Special tokens for cybersecurity context
        self.special_tokens = {
            'command_start': '<CMD>',
            'command_end': '</CMD>',
            'script_start': '<SCRIPT>',
            'script_end': '</SCRIPT>',
            'nmap_start': '<NMAP>',
            'nmap_end': '</NMAP>',
            'guide_start': '<GUIDE>',
            'guide_end': '</GUIDE>',
            'question_start': '<Q>',
            'question_end': '</Q>',
            'answer_start': '<A>',
            'answer_end': '</A>'
        }
    
    def load_scraped_data(self) -> Dict:
        """Load scraped cybersecurity data"""
        json_file = os.path.join(self.data_dir, 'cybersecurity_data.json')
        
        if not os.path.exists(json_file):
            logger.error(f"Scraped data file not found: {json_file}")
            return {}
            
        with open(json_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def create_conversational_data(self, data: Dict) -> List[str]:
        """Convert scraped data into conversational Q&A format"""
        conversations = []
        
        # Penetration testing Q&A
        for item in data.get('penetration_testing', []):
            content = item['content']
            if len(content) > 20:
                # Create Q&A pairs
                qa_pairs = [
                    f"{self.special_tokens['question_start']}How do I perform this penetration testing technique?{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{self.special_tokens['command_start']}{content}{self.special_tokens['command_end']}{self.special_tokens['answer_end']}",
                    f"{self.special_tokens['question_start']}What's a good penetration testing command for this scenario?{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{content}{self.special_tokens['answer_end']}",
                    f"{self.special_tokens['question_start']}Show me a penetration testing example{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{content}{self.special_tokens['answer_end']}"
                ]
                conversations.extend(qa_pairs)
        
        # Linux commands Q&A
        for item in data.get('linux_commands', []):
            content = item['content']
            if len(content) > 10:
                qa_pairs = [
                    f"{self.special_tokens['question_start']}What's the Linux command for this?{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{self.special_tokens['command_start']}{content}{self.special_tokens['command_end']}{self.special_tokens['answer_end']}",
                    f"{self.special_tokens['question_start']}How do I do this in Linux?{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{content}{self.special_tokens['answer_end']}",
                    f"{self.special_tokens['question_start']}Give me a Linux command{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{content}{self.special_tokens['answer_end']}"
                ]
                conversations.extend(qa_pairs)
        
        # Nmap commands Q&A
        for item in data.get('nmap_commands', []):
            content = item['content']
            if 'nmap' in content.lower() and len(content) > 10:
                qa_pairs = [
                    f"{self.special_tokens['question_start']}What's a good nmap command for scanning?{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{self.special_tokens['nmap_start']}{content}{self.special_tokens['nmap_end']}{self.special_tokens['answer_end']}",
                    f"{self.special_tokens['question_start']}How do I scan with nmap?{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{content}{self.special_tokens['answer_end']}",
                    f"{self.special_tokens['question_start']}Show me an nmap example{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{content}{self.special_tokens['answer_end']}"
                ]
                conversations.extend(qa_pairs)
        
        # Bash scripts Q&A
        for item in data.get('bash_scripts', []):
            content = item['content']
            if len(content) > 50:
                qa_pairs = [
                    f"{self.special_tokens['question_start']}Write a bash script for cybersecurity{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{self.special_tokens['script_start']}{content}{self.special_tokens['script_end']}{self.special_tokens['answer_end']}",
                    f"{self.special_tokens['question_start']}Show me a security script{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{content}{self.special_tokens['answer_end']}"
                ]
                conversations.extend(qa_pairs)
        
        return conversations
    
    def load_training_questions(self, questions_file="data/train_questions.txt") -> List[str]:
        """Load high-quality training questions from file"""
        questions = []
        
        # Check if questions file exists
        if not os.path.exists(questions_file):
            logger.warning(f"Training questions file not found: {questions_file}")
            return questions
            
        logger.info(f"Loading training questions from {questions_file}")
        
        try:
            with open(questions_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse the Q&A pairs
            lines = content.split('\n')
            current_user = None
            current_bot = None
            
            for line in lines:
                line = line.strip()
                if line.startswith('User:'):
                    current_user = line[5:].strip()  # Remove 'User:' prefix
                elif line.startswith('Bot:'):
                    current_bot = line[4:].strip()   # Remove 'Bot:' prefix
                    
                    # Create Q&A pair when we have both
                    if current_user and current_bot:
                        qa_pair = f"{self.special_tokens['question_start']}{current_user}{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{current_bot}{self.special_tokens['answer_end']}"
                        questions.append(qa_pair)
                        
                        # Reset for next pair
                        current_user = None
                        current_bot = None
            
            logger.info(f"Loaded {len(questions)} high-quality training questions")
            return questions
            
        except Exception as e:
            logger.error(f"Error loading training questions: {e}")
            return questions
    def add_cybersecurity_prompts(self) -> List[str]:
        """Add common cybersecurity prompts and responses"""
        prompts = [
            f"{self.special_tokens['question_start']}How do I start a penetration test?{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}Start with reconnaissance using nmap: {self.special_tokens['command_start']}nmap -sS -O <target_ip>{self.special_tokens['command_end']} (authorized lab only){self.special_tokens['answer_end']}",
            
            f"{self.special_tokens['question_start']}What are the phases of penetration testing?{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}1. Reconnaissance 2. Scanning 3. Enumeration 4. Vulnerability Assessment 5. Exploitation 6. Post-exploitation 7. Reporting (only on authorized systems){self.special_tokens['answer_end']}",
            
            f"{self.special_tokens['question_start']}How do I check for open ports?{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}{self.special_tokens['command_start']}nmap -p- <target_ip>{self.special_tokens['command_end']} or {self.special_tokens['command_start']}netstat -tulpn{self.special_tokens['command_end']} (lab use only){self.special_tokens['answer_end']}",
            
            f"{self.special_tokens['question_start']}How do I find hidden directories on a web server?{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}Use tools like: {self.special_tokens['command_start']}dirb http://<target>{self.special_tokens['command_end']} or {self.special_tokens['command_start']}gobuster dir -u http://<target> -w /usr/share/wordlists/dirb/common.txt{self.special_tokens['command_end']} (authorized testing only){self.special_tokens['answer_end']}",
            
            f"{self.special_tokens['question_start']}How do I escalate privileges in Linux?{self.special_tokens['question_end']}\n{self.special_tokens['answer_start']}Check for: 1. SUID binaries: {self.special_tokens['command_start']}find / -perm -u=s -type f 2>/dev/null{self.special_tokens['command_end']} 2. Sudo privileges: {self.special_tokens['command_start']}sudo -l{self.special_tokens['command_end']} 3. Cron jobs: {self.special_tokens['command_start']}cat /etc/crontab{self.special_tokens['command_end']} (defensive analysis only){self.special_tokens['answer_end']}",
        ]
        
        return prompts
    
    def prepare_training_data(self):
        """Prepare data for GPT training"""
        logger.info("Loading scraped data...")
        data = self.load_scraped_data()
        
        if not data:
            logger.error("No data found. Please run the scraper first.")
            return
        
        logger.info("Creating conversational data...")
        conversations = self.create_conversational_data(data)
        
        logger.info("Adding cybersecurity prompts...")
        prompts = self.add_cybersecurity_prompts()
        
        logger.info("Loading high-quality training questions...")
        training_questions = self.load_training_questions()
        
        # Combine all data (prioritize training questions by putting them first)
        all_text = training_questions + conversations + prompts
        
        # Join all conversations with newlines
        full_text = '\n'.join(all_text)
        
        logger.info(f"Total conversations: {len(all_text)}")
        logger.info(f"Total characters: {len(full_text)}")
        
        # Encode the text
        logger.info("Encoding text...")
        encoded = self.encoder.encode(full_text)
        
        logger.info(f"Total tokens: {len(encoded)}")
        
        # Split into train/validation (90/10 split)
        split_idx = int(0.9 * len(encoded))
        train_data = encoded[:split_idx]
        val_data = encoded[split_idx:]
        
        # Save as numpy arrays
        train_file = os.path.join(self.output_dir, 'train.bin')
        val_file = os.path.join(self.output_dir, 'val.bin')
        
        np.array(train_data, dtype=np.uint16).tofile(train_file)
        np.array(val_data, dtype=np.uint16).tofile(val_file)
        
        # Save metadata
        meta = {
            'vocab_size': self.encoder.n_vocab,
            'special_tokens': self.special_tokens,
            'train_tokens': len(train_data),
            'val_tokens': len(val_data),
            'total_tokens': len(encoded)
        }
        
        meta_file = os.path.join(self.output_dir, 'meta.pkl')
        with open(meta_file, 'wb') as f:
            pickle.dump(meta, f)
        
        # Save raw text for reference
        text_file = os.path.join(self.output_dir, 'raw_training_data.txt')
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write(full_text)
        
        logger.info(f"Training data saved to {self.output_dir}")
        logger.info(f"Train tokens: {len(train_data)}")
        logger.info(f"Validation tokens: {len(val_data)}")

def main():
    prep = CybersecurityDataPrep()
    prep.prepare_training_data()

if __name__ == "__main__":
    main()