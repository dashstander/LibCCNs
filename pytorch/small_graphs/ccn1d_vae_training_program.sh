# Compile the library
cd ../ccn_lib/
sh compile.sh
cd ../small_graphs

# Number of epochs
epochs=1024

# Learning rate
learning_rate=1e-2

# Architecture
input_size=16
output_size=32
message_sizes=16,16
message_mlp_sizes=16

# Activation
activation=sigmoid
# activation=relu

# Multi-threading
nThreads=10

# Batch size
batch_size=4

# Dataset's directory
data_dir=../../data

# Dataset: Graph-kernel benchmark
# data_name=MUTAG
# data_name=DD
# data_name=ENZYMES
# data_name=NCI1
# data_name=NCI109
data_name=PTC

# t-SNE visualization
tsne=1

# Fold
fold=0

# Training program
python3 ccn1d_vae_training_program.py --data_dir=$data_dir --data_name=$data_name --epochs=$epochs --learning_rate=$learning_rate --input_size=$input_size --output_size=$output_size --message_sizes=$message_sizes --message_mlp_sizes=$message_mlp_sizes --nThreads=$nThreads --activation=$activation --tsne=$tsne --fold=$fold