<<<<<<< HEAD
# Cybersecurity Chatbot - nanoGPT

A specialized GPT model trained on cybersecurity data to assist with ethical penetration testing, Linux commands, and network security analysis.

## 🏗️ Project Structure

```
nanoGPT/
├── 📁 data/                          # Data management
│   ├── 📁 raw_data/                  # Scraped cybersecurity data
│   ├── 📁 processed_data/            # Tokenized training data
│   ├── 📄 train_questions.txt        # High-quality training Q&A
│   └── 📄 prepare_cybersecurity.py   # Data preparation script
│
├── 📁 scripts/                       # Utility scripts
│   ├── 📄 data_scraper.py           # Web scraper for cybersecurity content
│   └── 📄 setup_cybersecurity_bot.py # Complete setup pipeline
│
├── 📁 tests/                         # Testing scripts
│   ├── 📄 test_cybersecurity_bot.py  # Main chatbot testing
│   ├── 📄 test_training_questions.py # Training question tests
│   └── 📄 simple_test.py            # Quick verification
│
├── 📁 training_configs/              # Training configurations
│   ├── 📄 train_cybersecurity.py     # Standard training config
│   ├── 📄 train_cybersecurity_enhanced.py # Enhanced training
│   ├── 📄 train_cybersecurity_fast.py     # Fast training config
│   └── 📄 train_gpt2.py              # Reference GPT-2 config
│
├── 📁 models/                        # Trained model checkpoints
│   └── 📄 ckpt.pt                   # Latest model checkpoint
│
├── 📁 web/                           # Web interface (NEW!)
│   ├── 📁 app/                       # Next.js application
│   ├── 📄 package.json              # Web dependencies
│   ├── 📄 README.md                 # Web interface guide
│   └── 📄 deploy.md                 # Deployment instructions
│
├── 📁 docs/                          # Documentation
│   └── 📄 README.md                 # Detailed usage guide
│
├── 📄 model.py                      # Core GPT model implementation
├── 📄 train.py                      # Training script
├── 📄 sample.py                     # Text generation script
├── 📄 configurator.py               # Configuration management
├── 📄 requirements.txt              # Python dependencies
└── 📄 LICENSE                       # MIT License
```

## 🚀 Quick Start

### 1. Setup Environment
```bash
pip install -r requirements.txt
```

### 2. Complete Pipeline (Recommended)
```bash
python scripts/setup_cybersecurity_bot.py
```

### 3. Manual Steps
```bash
# Scrape data
python scripts/data_scraper.py

# Prepare training data
python data/prepare_cybersecurity.py

# Train model
python train.py training_configs/train_cybersecurity.py

# Test the model
python tests/test_cybersecurity_bot.py
```

### 4. Web Interface (NEW!) 🌐
```bash
# Install web dependencies
cd web
npm install

# Run development server
npm run dev

# Deploy to Vercel
vercel --prod
```

## 🌐 Web Interface Features

- **Modern Cyberpunk UI**: Dark theme with glowing green terminal aesthetics
- **Real-time Chat**: Instant responses with typing indicators
- **Security Warnings**: Prominent ethical use disclaimers
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Smooth Animations**: Professional transitions and effects
- **Terminal Feel**: Authentic hacker/cybersec interface design

## 🎯 What This Bot Knows

- **Ethical Penetration Testing**: Authorized testing procedures
- **Linux Security Commands**: System analysis and hardening
- **Network Reconnaissance**: nmap scanning techniques
- **Incident Response**: Log analysis and containment
- **Security Best Practices**: Defensive cybersecurity

## 🔒 Safety Features

- **Authorization Checks**: Emphasizes permission requirements
- **Ethical Guidelines**: Refuses illegal activities
- **Safe Templates**: Uses placeholders for sensitive data
- **Defensive Focus**: Prioritizes protection over exploitation

## 📊 Training Data

- **26 High-Quality Q&A Pairs**: Curated ethical cybersecurity questions
- **258 Linux Commands**: System administration and security
- **76 nmap Commands**: Network scanning techniques
- **Scraped Content**: Legitimate cybersecurity resources

## 🧪 Testing

```bash
# Test with training questions
python tests/test_training_questions.py test

# Interactive chat
python tests/test_cybersecurity_bot.py

# Quick verification
python tests/simple_test.py
```

## ⚙️ Configuration

Training configurations are in `training_configs/`:
- `train_cybersecurity.py`: Standard training (16M parameters)
- `train_cybersecurity_enhanced.py`: Enhanced training (30M parameters)
- `train_cybersecurity_fast.py`: Fast training (7M parameters)

## 🎓 Example Usage

```
User: "How do I scan for open ports safely?"
Bot: "Template: nmap -sV -Pn <target> (authorized lab only). Replace <target> with your test system IP."

User: "Is it legal to scan random servers?"
Bot: "No. Only run scans on systems you own or have explicit written permission to test."
```

## 📁 Data Files

- **Raw Data**: `data/raw_data/` - Original scraped content
- **Processed Data**: `data/processed_data/` - Tokenized training data
- **Training Questions**: `data/train_questions.txt` - High-quality Q&A pairs

## 🛠️ Development

To add new training data:
1. Add questions to `data/train_questions.txt`
2. Run `python data/prepare_cybersecurity.py`
3. Retrain with `python train.py training_configs/train_cybersecurity_enhanced.py`

## 📜 License

MIT License - See LICENSE file for details.

## ⚠️ Legal Notice

# cybersecurity-gpt
i dont know i am still working on this when i figure out i will inform you
>>>>>>> b40373dc66991177b854a019e236cb7cf4df763f
This tool is for educational and authorized testing purposes only. Always ensure you have permission before testing on any systems you don't own.
=======
# cybersecurity-gpt
i dont know i am still working on this when i figure out i will inform you
>>>>>>> b40373dc66991177b854a019e236cb7cf4df763f
