import pandas as pd
from matplotlib import pyplot as plt

# Load data
df = pd.read_excel("inventory.xlsx", sheet_name="Input")
low_stock = df[df["Current Stock"] < df["Min Threshold"]]

# Create a simple plot
plt.bar(low_stock["Product"], low_stock["Min Threshold"] - low_stock["Current Stock"])
plt.title("Urgent Reorder Needs")
plt.savefig("report.png")  # Add to PDF
