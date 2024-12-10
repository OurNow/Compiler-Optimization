import torch
from cnn_model import CompilerOptimizerCNN

# Load Model
model = CompilerOptimizerCNN(vocab_size=100, embedding_dim=128, num_classes=3)
model.load_state_dict(torch.load("compiler_optimizer.pth"))
model.eval()

# Test Data
test_inputs = torch.randint(0, 100, (10, 50))  # 10 samples

# Predict
with torch.no_grad():
    predictions = model(test_inputs)
    predicted_flags = torch.argmax(predictions, axis=1)
    print(f"Predicted Optimization Flags: {predicted_flags}")

