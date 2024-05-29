from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from typing import List, Dict, Any
import json

app = FastAPI()

# Load the data.json file
with open('data.json', 'r') as file:
    data_file = json.load(file)

# Create a lookup dictionary for factors
factor_lookup = {}
for entry in data_file["data"]:
    key = (entry["var_name"], entry["category"])
    factor_lookup[key] = entry["factor"]

# Infer valid categories from factor_lookup
valid_categories = {}
for var_name, category in factor_lookup.keys():
    if var_name not in valid_categories:
        valid_categories[var_name] = []
    if category not in valid_categories[var_name]:
        valid_categories[var_name].append(category)

@app.post("/validate")
async def validate_data():
    # Validation is automatically handled by Pydantic
    pass

@app.post("/get_factors")
async def get_factors(payload):
    results = []
    for entry in payload.data:
        key = (entry.var_name, entry.category)
        factor = factor_lookup.get(key)
        if factor is None:
            raise HTTPException(status_code=404, detail=f"Factor not found for {entry.var_name} - {entry.category}")
        results.append({
            "var_name": entry.var_name,
            "category": entry.category,
            "factor": factor
        })
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
