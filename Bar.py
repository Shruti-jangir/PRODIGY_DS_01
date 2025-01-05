import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\shrut\Downloads\archive (7)\bangladesh_divisions_dataset.csv"  
data = pd.read_csv(file_path)

sns.set_theme(style="whitegrid")

# Plot the bar chart for Soil_Type
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x="Soil_Type", palette="viridis")
plt.title("Distribution of Soil Types", fontsize=16)
plt.xlabel("Soil Type", fontsize=14)
plt.ylabel("Count", fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
