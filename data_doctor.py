import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Alice", None],
    "Age": [20, 21, 20, 22]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

df = df.drop_duplicates()
df = df.fillna("Unknown")

print("\nCleaned Data")
print(df)