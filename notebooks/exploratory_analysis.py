import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create a directory for output plots
os.makedirs("results/plots", exist_ok=True)

# Load the dataset
data = pd.read_csv("data/processed/metrics.csv")
print("Dataset Head:\n", data.head())

# 1. Check for missing values
missing_values = data.isnull().sum()
print("Missing Values:\n", missing_values)

# 2. Distribution of Optimization Flags
flag_counts = data["flag"].value_counts()
print("Flag Distribution:\n", flag_counts)

# Plot the distribution of optimization flags
sns.countplot(x="flag", data=data)
plt.title("Distribution of Optimization Flags")
plt.savefig("results/plots/flag_distribution.png")
plt.clf()  # Clear the current figure

# 3. Runtime Distribution by Optimization Flag
sns.boxplot(x="flag", y="runtime", data=data)
plt.title("Runtime Distribution by Optimization Flag")
plt.ylabel("Runtime (ms)")
plt.savefig("results/plots/runtime_distribution.png")
plt.clf()

# 4. Performance Comparison for Each Program
sns.barplot(x="program", y="runtime", hue="flag", data=data)
plt.title("Program Performance by Optimization Flag")
plt.ylabel("Runtime (ms)")
plt.xticks(rotation=45)
plt.savefig("results/plots/program_performance.png")
plt.clf()

# 5. Correlation Analysis
# Encode flags as numerical values
data["flag_encoded"] = data["flag"].map({"-O1": 1, "-O2": 2, "-O3": 3})

# Calculate correlation matrix
corr_matrix = data[["flag_encoded", "runtime"]].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("results/plots/correlation_heatmap.png")
plt.clf()

# 6. Token Length Analysis (if tokenized data exists)
if os.path.exists("data/processed/tokenized_dataset.csv"):
    tokenized_data = pd.read_csv("data/processed/tokenized_dataset.csv")
    tokenized_data["token_count"] = tokenized_data["tokens"].apply(lambda x: len(x.split()))
    
    # Plot token length distribution
    sns.histplot(tokenized_data["token_count"], bins=30)
    plt.title("Token Length Distribution")
    plt.xlabel("Number of Tokens")
    plt.ylabel("Frequency")
    plt.savefig("results/plots/token_length_distribution.png")
    plt.clf()

# Save processed data for model training
data.to_csv("data/processed/training_data.csv", index=False)
print("Processed data saved to 'data/processed/training_data.csv'")

print("Exploratory analysis completed. Plots saved in 'results/plots/'.")

