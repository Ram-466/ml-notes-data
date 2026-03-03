import pandas as pd

# Create DataFrame manually
data = {
    "name": ["Ram", "Aisha", "John"],
    "age": [24, 29, 31],
    "salary": [60000, 75000, 50000]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nColumns:", df.columns)
print("Shape:", df.shape)

print("\nSelect 'age' column:")
print(df["age"])

print("\nFilter age > 25:")
print(df[df["age"] > 25])
