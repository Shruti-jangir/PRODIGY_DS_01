import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\shrut\Downloads\archive (7)\bangladesh_divisions_dataset.csv" 
data = pd.read_csv(file_path)

sns.set_theme(style="whitegrid")

# Plot the histogram for Fertility_Index
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x="Fertility_Index", bins=20, kde=True, color="blue")
plt.title("Distribution of Fertility Index", fontsize=16)
plt.xlabel("Fertility Index", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.tight_layout()
plt.show()
