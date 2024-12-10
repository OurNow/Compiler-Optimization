import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from cnn_model import CompilerOptimizerCNN

# Dummy Dataset
inputs = torch.randint(0, 100, (100, 50))  # 100 samples, 50 tokens each
labels = torch.randint(0, 3, (100,))  # 3 optimization flags

dataset = TensorDataset(inputs, labels)
train_loader = DataLoader(dataset, batch_size=10, shuffle=True)

# Model and Training Setup
model = CompilerOptimizerCNN(vocab_size=100, embedding_dim=128, num_classes=3)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training Loop
for epoch in range(5):
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        print(f"Input shape: {inputs.shape}")  # Debugging
        outputs = model(inputs)
        print(f"Output shape: {outputs.shape}")  # Debugging
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item()}")

# Save Model
torch.save(model.state_dict(), "compiler_optimizer.pth")

