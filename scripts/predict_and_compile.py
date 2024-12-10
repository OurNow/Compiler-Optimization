import sys
import os
import subprocess
import torch

# Add the models directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "models")))

# Import the model class
from cnn_model import CompilerOptimizerCNN

# Load Model
model = CompilerOptimizerCNN(vocab_size=100, embedding_dim=128, num_classes=3)
model.load_state_dict(torch.load("compiler_optimizer.pth"))
model.eval()

# Tokenize and Predict
def predict_flag(code):
    tokens = torch.tensor([1] * 50)  # Dummy tokenized input, replace with real tokenization
    with torch.no_grad():
        prediction = model(tokens.unsqueeze(0))  # Add batch dimension
        return torch.argmax(prediction).item()

# List of source code files to compile
code_files = ["data/raw/matrix_mul.c", "data/raw/bubble_sort.c"]

# Iterate over the source code files
for code_path in code_files:
    with open(code_path) as f:
        code = f.read()

    # Get the predicted optimization flag
    predicted_flag = ["-O1", "-O2", "-O3"][predict_flag(code)]

    # Compile using the predicted flag
    subprocess.run(["clang", predicted_flag, "-o", f"optimized_{os.path.basename(code_path).split('.')[0]}.out", code_path])
    print(f"Compiled {code_path} with {predicted_flag}")

