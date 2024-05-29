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

class DataEntry(BaseModel):
    var_name: str = Field(..., description="The variable name, either 'country' or 'age_group'.")
    category: str = Field(..., description="The category associated with the var_name.")

    @validator("var_name")
    def validate_var_name(cls, v):
        if v not in valid_categories:
            raise ValueError("Invalid var_name, must be one of the valid var_names in the data.")
        return v

    @validator("category")
    def validate_category(cls, v, values):
        if "var_name" in values and v not in valid_categories[values["var_name"]]:
            raise ValueError(f"Invalid category for var_name '{values['var_name']}'")
        return v

class RequestPayload(BaseModel):
    data: List[DataEntry]

@app.post("/validate")
async def validate_data(payload: RequestPayload):
    # Validation is automatically handled by Pydantic
    return {"status": "success", "message": "Validation passed"}

@app.post("/get_factors")
async def get_factors(payload: RequestPayload):
    results = []
    for entry in payload.data:
        key = (entry.var_name, entry.category)
        factor = factor_lookup[key]
        results.append({
            "var_name": entry.var_name,
            "category": entry.category,
            "factor": factor
        })
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
