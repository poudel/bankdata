from typing import List
from fastapi import FastAPI, Query, Body

from nest_lib import nest_dicts


app = FastAPI()


@app.post("/api/v1/nest_dicts")
async def nest_dicts_api(
    input_data: List[dict] = Body(..., min_length=1),
    nesting_keys: List[str] = Query(..., min_length=1),
):
    try:
        return nest_dicts(input_data, nesting_keys)
    except ValueError as err:
        return {'error': str(err)}, 422
