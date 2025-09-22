# Fast training configuration for cybersecurity chatbot
# Optimized for very quick training to get a working model

# I/O
out_dir = 'out-cybersecurity-fast'
eval_interval = 100  # Evaluate more frequently
log_interval = 5     # Log more frequently
eval_iters = 20      # Fewer evaluation iterations
eval_only = False
always_save_checkpoint = True
init_from = 'scratch'

# wandb logging
wandb_log = False
wandb_project = 'cybersecurity-chatbot'
wandb_run_name = 'cybersec-gpt-fast'

# data
dataset = 'processed_data'
gradient_accumulation_steps = 1  # No gradient accumulation for speed
batch_size = 2  # Very small batch size
block_size = 256  # Even smaller context length

# model - tiny model for very fast training
n_layer = 2  # Minimal layers
n_head = 2   # Minimal heads
n_embd = 128 # Minimal embedding size
dropout = 0.0  # No dropout for speed
bias = False

# adamw optimizer
learning_rate = 1e-3  # Higher learning rate for faster convergence
max_iters = 1000     # Very few iterations for quick test
weight_decay = 1e-2   # Lower weight decay
beta1 = 0.9
beta2 = 0.95
grad_clip = 1.0

# learning rate decay settings
decay_lr = True
warmup_iters = 50    # Very short warmup
lr_decay_iters = 1000
min_lr = 1e-4

# DDP settings
backend = 'nccl'

# system
device = 'cpu'
dtype = 'float32'
compile = False