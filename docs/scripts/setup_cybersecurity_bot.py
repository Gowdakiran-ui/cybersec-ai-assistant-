#!/usr/bin/env python3
"""
Complete pipeline to scrape cybersecurity data and prepare for training
"""

import os
import sys
import subprocess
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_command(command, cwd=None):
    """Run a command and log output"""
    logger.info(f"Running: {command}")
    try:
        result = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            logger.error(f"Command failed: {result.stderr}")
            return False
        logger.info(f"Command output: {result.stdout}")
        return True
    except Exception as e:
        logger.error(f"Error running command: {e}")
        return False

def main():
    logger.info("Starting cybersecurity chatbot data preparation pipeline...")
    
    # Step 1: Install requirements
    logger.info("Installing requirements...")
    if not run_command("pip install -r requirements.txt"):
        logger.error("Failed to install requirements")
        return
    
    # Step 2: Run the scraper
    logger.info("Scraping cybersecurity data...")
    if not run_command("python scripts/data_scraper.py"):
        logger.error("Failed to scrape data")
        return
    
    # Step 3: Prepare training data
    logger.info("Preparing training data...")
    if not run_command("python data/prepare_cybersecurity.py"):
        logger.error("Failed to prepare training data")
        return
    
    # Step 4: Start training
    logger.info("Starting model training...")
    train_command = "python train.py training_configs/train_cybersecurity.py"
    logger.info(f"To start training, run: {train_command}")
    logger.info("Training will take several hours depending on your hardware.")
    logger.info("Monitor the training in the 'out-cybersecurity' directory.")
    
    # Ask user if they want to start training immediately
    response = input("Do you want to start training now? (y/n): ")
    if response.lower().strip() == 'y':
        logger.info("Starting training...")
        run_command(train_command)
    else:
        logger.info("Training command ready. Run when you're ready to train.")
    
    logger.info("Pipeline completed!")

if __name__ == "__main__":
    main()