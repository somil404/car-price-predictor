import pandas as pd

data = {
    "Name" : ['Somil', 'Hello', 'KK'],
    "Age" : [20, 7, 23],
    "Gender" : ['M', 'M', 'F']
}

df = pd.DataFrame(data)
# df.to_csv("outputPandas.csv")
# df.to_excel("outputPandas1.xlsx", index = False)
df.to_json("outputPandas.json")
print(df)