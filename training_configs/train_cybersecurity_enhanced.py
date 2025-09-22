# Enhanced training configuration for cybersecurity chatbot with high-quality questions
# Optimized for learning from curated training questions

# I/O
out_dir = 'out-cybersecurity-enhanced'
eval_interval = 100  # Evaluate frequently
log_interval = 5     # Log frequently to track progress
eval_iters = 30      # More evaluation iterations
eval_only = False
always_save_checkpoint = True
init_from = 'scratch'

# wandb logging
wandb_log = False
wandb_project = 'cybersecurity-chatbot'
wandb_run_name = 'cybersec-gpt-enhanced'

# data
dataset = 'processed_data'
gradient_accumulation_steps = 2  # Small accumulation for quality data
batch_size = 3  # Small batch size for focused learning
block_size = 384  # Medium context length

# model - balanced model for quality learning
n_layer = 6  # More layers for better learning
n_head = 6   # More attention heads
n_embd = 384 # Good embedding size
dropout = 0.1  # Some dropout for generalization
bias = False

# adamw optimizer
learning_rate = 2e-4  # Lower learning rate for careful training
max_iters = 2000     # More iterations for better learning
weight_decay = 1e-1
beta1 = 0.9
beta2 = 0.95
grad_clip = 1.0

# learning rate decay settings
decay_lr = True
warmup_iters = 200   # Good warmup period
lr_decay_iters = 2000
min_lr = 2e-5

# DDP settings
backend = 'nccl'

# system
device = 'cpu'
dtype = 'float32'
compile = False