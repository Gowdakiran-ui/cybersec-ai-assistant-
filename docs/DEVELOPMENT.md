# Development Guide

## Getting Started

### Prerequisites
- Python 3.8+
- PyTorch 2.0+
- 8GB+ RAM recommended
- CUDA GPU (optional, for faster training)

### Installation
```bash
git clone <repository>
cd nanoGPT
pip install -r requirements.txt
```

## Development Workflow

### 1. Data Collection
```bash
# Scrape new cybersecurity data
python scripts/data_scraper.py

# Verify scraped data
ls data/raw_data/
```

### 2. Data Preparation
```bash
# Process data for training
python data/prepare_cybersecurity.py

# Check processed data
ls data/processed_data/
```

### 3. Model Training
```bash
# Fast training (for testing)
python train.py training_configs/train_cybersecurity_fast.py

# Standard training (recommended)
python train.py training_configs/train_cybersecurity.py

# Enhanced training (best quality)
python train.py training_configs/train_cybersecurity_enhanced.py
```

### 4. Testing
```bash
# Quick test
python tests/simple_test.py

# Comprehensive test
python tests/test_cybersecurity_bot.py

# Training questions test
python tests/test_training_questions.py test
```

## File Structure Guidelines

### Core Files (Root Directory)
- `model.py`: Core GPT implementation (don't modify unless necessary)
- `train.py`: Training script (stable, well-tested)
- `sample.py`: Text generation (for inference)
- `configurator.py`: Configuration system

### Data Management (`data/`)
- `raw_data/`: Original scraped content
- `processed_data/`: Tokenized training data
- `train_questions.txt`: High-quality Q&A pairs
- `prepare_cybersecurity.py`: Data processing pipeline

### Scripts (`scripts/`)
- `data_scraper.py`: Web scraping functionality
- `setup_cybersecurity_bot.py`: Complete setup pipeline

### Testing (`tests/`)
- Test files for different aspects of the system
- Should be runnable independently
- Include both unit and integration tests

### Configuration (`training_configs/`)
- Different training scenarios
- Hyperparameter tuning
- Model size variants

### Models (`models/`)
- Trained model checkpoints
- Model metadata and configs

### Documentation (`docs/`)
- User guides and API documentation
- Architecture explanations
- Development guidelines

## Adding New Features

### New Training Data
1. Add content to `data/train_questions.txt`
2. Or modify scraper in `scripts/data_scraper.py`
3. Run `python data/prepare_cybersecurity.py`
4. Retrain model

### New Model Configurations
1. Copy existing config from `training_configs/`
2. Modify parameters as needed
3. Test with small dataset first
4. Document changes

### New Tests
1. Add test files to `tests/`
2. Follow existing naming convention
3. Include both positive and negative cases
4. Test safety features

## Best Practices

### Code Quality
- Follow PEP 8 style guidelines
- Add type hints where possible
- Include docstrings for functions
- Handle errors gracefully

### Data Safety
- Never commit sensitive data
- Use placeholders in examples
- Sanitize scraped content
- Respect robots.txt and rate limits

### Model Safety
- Test refusal mechanisms
- Validate safety responses
- Monitor for harmful outputs
- Include ethical guidelines

### Performance
- Profile training performance
- Monitor memory usage
- Optimize data loading
- Use appropriate batch sizes

## Troubleshooting

### Common Issues

#### CUDA Out of Memory
- Reduce batch_size in config
- Use smaller model (fewer layers/embedding size)
- Enable gradient checkpointing

#### Slow Training
- Use GPU if available
- Increase batch_size (if memory allows)
- Reduce model size for testing

#### Poor Quality Responses
- Increase training iterations
- Use larger model
- Improve training data quality
- Adjust learning rate

#### Path Issues
- Use relative paths in configs
- Check file exists before processing
- Handle Windows/Linux path differences

### Debugging

#### Enable Verbose Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

#### Monitor Training
- Watch loss curves
- Check validation performance
- Save intermediate checkpoints

#### Test Incrementally
- Start with small datasets
- Use fast training configs
- Verify each component works

## Contributing

### Pull Request Process
1. Fork the repository
2. Create feature branch
3. Add tests for new features
4. Update documentation
5. Submit pull request

### Code Review Checklist
- [ ] Code follows style guidelines
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Safety features tested
- [ ] Performance impact considered

### Release Process
1. Update version numbers
2. Test on clean environment
3. Update changelog
4. Tag release
5. Create release notes