import json
import pandas as pd

df = pd.read_excel('example.xlsx', sheet_name=0)

grouped = df.groupby('Age')
result = []
updated_groups = []
for age, group in grouped:
    group["Salary"] = group["Salary"].astype(str).str.replace(',','.').astype(float)
    people = (
        group.drop(columns=['Age']).assign(ok=group["Salary"] > 50000).to_dict(orient='records')
    )

    result.append({
        "age": age,
        "people": people
    })
    updated_groups.append(group)

updated_df = pd.concat(updated_groups)

print(json.dumps(result, indent=4))


