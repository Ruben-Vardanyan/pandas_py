import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "duration2": [150, 140, 145],
}
df = pd.DataFrame(data)

print(df.iloc[0, 1])
print(df.loc[0, "duration2"])
