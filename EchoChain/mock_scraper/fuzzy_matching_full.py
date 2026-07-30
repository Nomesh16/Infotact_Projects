import pandas as pd
from fuzzywuzzy import fuzz

df = pd.read_csv("../EchoChain_20000.csv")

# First 10 rows meeda test cheyyi
sample = df[["Listing_Title", "Product_Model"]].head(100)

sample["Calculated_Match_Score"] = sample.apply(
    lambda row: fuzz.ratio(str(row["Listing_Title"]), str(row["Product_Model"])), axis=1
)

print(sample)