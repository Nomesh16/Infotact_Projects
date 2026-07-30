import pandas as pd

df = pd.read_csv("../EchoChain_20000.csv")

print("Missing values in each column:")
print(df.isnull().sum())

print("\nDuplicate rows count:")
print(df.duplicated().sum())

print("\nTotal rows:", len(df))