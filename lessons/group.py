import pandas as pd
import json

df = pd.read_csv('../data.csv')

# print(df)

grouped = df.groupby('age')

result = []
for age, group in grouped:
    people = group.drop(columns=['age']).to_dict(orient='records')
    result.append({
        "age": age,
        "people": people
    })





print(json.dumps(result, indent=2))