import pandas as pd
import json

df = pd.read_csv('../data.csv')

grouped = df.groupby('age')
print(df.info())
result = []
for age, group in grouped:
    group['salary'] = group['salary'].astype(str).str.replace(',', '.').astype(float).round(3)
    people = (
        group
        .drop(columns=['age'])
        .assign(ok=group['salary'] > 90000)
        .to_dict(orient='records')
    )

    result.append({
        "age": age,
        "people": people
    })

print(json.dumps(result, indent=2))

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(result, indent=2))
