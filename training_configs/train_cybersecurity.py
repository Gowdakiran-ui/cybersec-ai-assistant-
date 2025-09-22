# Configuration for training cybersecurity chatbot
# Based on train_gpt2.py but optimized for cybersecurity domain

# I/O
out_dir = 'out-cybersecurity'
eval_interval = 500
log_interval = 10
eval_iters = 100
eval_only = False
always_save_checkpoint = True
init_from = 'scratch'  # 'scratch' or 'resume' or 'gpt2*'

# wandb logging
wandb_log = False  # Set to True if you want to use Weights & Biases
wandb_project = 'cybersecurity-chatbot'
wandb_run_name = 'cybersec-gpt'

# data
dataset = 'processed_data'
gradient_accumulation_steps = 4  # Reduced for CPU training
batch_size = 4  # Smaller batch size for CPU
block_size = 512  # Reduced context length for CPU

# model - smaller model for CPU training
n_layer = 4  # Much smaller for CPU training
n_head = 4   # Reduced further
n_embd = 256 # Reduced further for CPU
dropout = 0.1  # Higher dropout for better generalization on smaller dataset
bias = False

# adamw optimizer
learning_rate = 3e-4  # Slightly lower learning rate
max_iters = 50000    # Fewer iterations for domain-specific training
weight_decay = 1e-1
beta1 = 0.9
beta2 = 0.95
grad_clip = 1.0

# learning rate decay settings
decay_lr = True
warmup_iters = 1000   # Reduced warmup
lr_decay_iters = 50000  # Should match max_iters
min_lr = 3e-5  # Minimum learning rate

# DDP settings
backend = 'nccl'

# system
device = 'cpu'  # Changed to CPU since CUDA is not available
dtype = 'float32'  # Use float32 for CPU training
compile = False  # Disable compilation for CPU