import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Sales": [200, 450, 300, 150, 500],
    "Profit": [50, 120, 80, 30, 150]
}

df = pd.DataFrame(data)

print("Top Rows:")
print(df.head())

print("\nHighest Sales:", df["Sales"].max())

print("\nMissing Values:")
print(df.isnull().sum())