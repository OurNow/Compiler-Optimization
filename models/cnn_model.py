import torch
import torch.nn as nn

class CompilerOptimizerCNN(nn.Module):
    def __init__(self, vocab_size, embedding_dim, num_classes):
        super(CompilerOptimizerCNN, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.conv = nn.Conv1d(embedding_dim, 64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool1d(kernel_size=2)
        self.fc = nn.Linear(64 * (50 // 2), num_classes)  # Adjust based on sequence length

    def forward(self, x):
        x = self.embedding(x)  # Shape: (batch_size, sequence_length, embedding_dim)
        x = x.permute(0, 2, 1)  # Shape: (batch_size, embedding_dim, sequence_length)
        x = self.conv(x)  # Shape: (batch_size, 64, sequence_length)
        x = self.pool(x)  # Shape: (batch_size, 64, sequence_length // 2)
        x = x.view(x.size(0), -1)  # Flatten for fully connected layer
        return self.fc(x)  # Shape: (batch_size, num_classes)

