import pandas as pd

data = {
    "Study_Hours": [1,2,3,4,5,6],
    "Marks": [40,50,55,65,70,80]
}

df = pd.DataFrame(data)

print(df)
print("\nFeature: Study_Hours")
print("Label: Marks")

print("\nObservation: More study hours → higher marks.")