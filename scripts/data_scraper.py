#!/usr/bin/env python3
"""
Cybersecurity Data Scraper for Chatbot Training
Scrapes penetration testing commands, Linux cheatsheets, and nmap outputs
"""

import requests
from bs4 import BeautifulSoup
import time
import random
import json
import os
import re
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Set
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CyberSecurityScraper:
    def __init__(self, output_dir="data/raw_data"):
        self.output_dir = output_dir
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        self.scraped_urls = set()
        self.data = {
            'penetration_testing': [],
            'linux_commands': [],
            'nmap_commands': [],
            'cybersecurity_guides': [],
            'bash_scripts': []
        }
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
    def delay(self, min_delay=1, max_delay=3):
        """Random delay between requests to be respectful"""
        time.sleep(random.uniform(min_delay, max_delay))
        
    def clean_text(self, text: str) -> str:
        """Clean and normalize text"""
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        # Remove special characters but keep command syntax
        text = re.sub(r'[^\w\s\-\.\$/\|\>\<\[\]\(\)\{\}\=\+\*\&\%\#\@\!\?\:\;\,]', '', text)
        return text.strip()
    
    def get_page_content(self, url: str) -> BeautifulSoup:
        """Fetch and parse page content"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def scrape_penetration_testing_commands(self):
        """Scrape penetration testing commands and techniques"""
        logger.info("Scraping penetration testing commands...")
        
        # List of cybersecurity resources
        pentest_urls = [
            "https://github.com/swisskyrepo/PayloadsAllTheThings",
            "https://book.hacktricks.xyz/",
            "https://pentestmonkey.net/cheat-sheet",
            "https://highon.coffee/blog/penetration-testing-tools-cheat-sheet/",
            "https://www.sans.org/posters/",
        ]
        
        for url in pentest_urls:
            if url in self.scraped_urls:
                continue
                
            logger.info(f"Scraping: {url}")
            soup = self.get_page_content(url)
            if not soup:
                continue
                
            # Extract code blocks and command examples
            code_blocks = soup.find_all(['code', 'pre', 'div'], class_=lambda x: x and ('code' in x.lower() or 'command' in x.lower()))
            
            for block in code_blocks:
                text = block.get_text().strip()
                if text and len(text) > 10:
                    self.data['penetration_testing'].append({
                        'source': url,
                        'content': self.clean_text(text),
                        'type': 'command'
                    })
            
            self.scraped_urls.add(url)
            self.delay()
    
    def scrape_linux_cheatsheets(self):
        """Scrape Linux command cheatsheets"""
        logger.info("Scraping Linux cheatsheets...")
        
        linux_urls = [
            "https://www.linuxtrainingacademy.com/linux-commands-cheat-sheet/",
            "https://cheatography.com/davechild/cheat-sheets/linux-command-line/",
            "https://www.commandlinefu.com/commands/browse",
            "https://github.com/LeCoupa/awesome-cheatsheets/blob/master/languages/bash.sh",
        ]
        
        for url in linux_urls:
            if url in self.scraped_urls:
                continue
                
            logger.info(f"Scraping: {url}")
            soup = self.get_page_content(url)
            if not soup:
                continue
                
            # Look for command patterns
            command_patterns = [
                r'^\s*[\w\-]+\s+[\-\w\s\.\$\{\}\/]+',  # Basic command pattern
                r'^\s*sudo\s+[\w\-\s]+',               # Sudo commands
                r'^\s*\$\s+[\w\-\s\.\$\{\}\/]+',       # Shell prompt commands
            ]
            
            # Extract text and find commands
            text_content = soup.get_text()
            lines = text_content.split('\n')
            
            for line in lines:
                line = line.strip()
                if any(re.match(pattern, line) for pattern in command_patterns):
                    if len(line) > 5 and len(line) < 200:  # Reasonable command length
                        self.data['linux_commands'].append({
                            'source': url,
                            'content': self.clean_text(line),
                            'type': 'linux_command'
                        })
            
            self.scraped_urls.add(url)
            self.delay()
    
    def scrape_nmap_examples(self):
        """Scrape nmap command examples and outputs"""
        logger.info("Scraping nmap examples...")
        
        nmap_urls = [
            "https://nmap.org/book/man-examples.html",
            "https://www.cyberciti.biz/security/nmap-command-examples-tutorials/",
            "https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/",
        ]
        
        for url in nmap_urls:
            if url in self.scraped_urls:
                continue
                
            logger.info(f"Scraping: {url}")
            soup = self.get_page_content(url)
            if not soup:
                continue
                
            # Look for nmap commands specifically
            text_content = soup.get_text()
            lines = text_content.split('\n')
            
            for line in lines:
                line = line.strip()
                if 'nmap' in line.lower() and len(line) > 10:
                    self.data['nmap_commands'].append({
                        'source': url,
                        'content': self.clean_text(line),
                        'type': 'nmap_command'
                    })
            
            self.scraped_urls.add(url)
            self.delay()
    
    def scrape_bash_scripts(self):
        """Scrape cybersecurity bash scripts"""
        logger.info("Scraping bash scripts...")
        
        script_urls = [
            "https://github.com/topics/cybersecurity-scripts",
            "https://github.com/topics/penetration-testing-scripts",
            "https://github.com/topics/bash-scripts",
        ]
        
        for url in script_urls:
            if url in self.scraped_urls:
                continue
                
            logger.info(f"Scraping: {url}")
            soup = self.get_page_content(url)
            if not soup:
                continue
                
            # Extract script content
            script_blocks = soup.find_all(['pre', 'code'])
            
            for block in script_blocks:
                text = block.get_text().strip()
                if ('#!/bin/bash' in text or 'bash' in text.lower()) and len(text) > 50:
                    self.data['bash_scripts'].append({
                        'source': url,
                        'content': self.clean_text(text),
                        'type': 'bash_script'
                    })
            
            self.scraped_urls.add(url)
            self.delay()
    
    def save_data(self):
        """Save scraped data to files"""
        logger.info("Saving scraped data...")
        
        # Save as JSON
        json_file = os.path.join(self.output_dir, 'cybersecurity_data.json')
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
        
        # Save as plain text for training
        text_file = os.path.join(self.output_dir, 'training_data.txt')
        with open(text_file, 'w', encoding='utf-8') as f:
            for category, items in self.data.items():
                f.write(f"\n# {category.upper()}\n")
                f.write("="*50 + "\n")
                for item in items:
                    f.write(f"Source: {item['source']}\n")
                    f.write(f"Type: {item['type']}\n")
                    f.write(f"Content: {item['content']}\n")
                    f.write("-"*30 + "\n")
        
        # Save category-specific files
        for category, items in self.data.items():
            category_file = os.path.join(self.output_dir, f'{category}.txt')
            with open(category_file, 'w', encoding='utf-8') as f:
                for item in items:
                    f.write(f"{item['content']}\n")
        
        # Statistics
        total_items = sum(len(items) for items in self.data.values())
        logger.info(f"Saved {total_items} items across {len(self.data)} categories")
        
        for category, items in self.data.items():
            logger.info(f"{category}: {len(items)} items")
    
    def run_full_scrape(self):
        """Run complete scraping process"""
        logger.info("Starting cybersecurity data scraping...")
        
        try:
            self.scrape_penetration_testing_commands()
            self.scrape_linux_cheatsheets()
            self.scrape_nmap_examples()
            self.scrape_bash_scripts()
            self.save_data()
            
            logger.info("Scraping completed successfully!")
            
        except KeyboardInterrupt:
            logger.info("Scraping interrupted by user")
            self.save_data()
        except Exception as e:
            logger.error(f"Error during scraping: {e}")
            self.save_data()

def main():
    scraper = CyberSecurityScraper()
    scraper.run_full_scrape()

if __name__ == "__main__":
    main()