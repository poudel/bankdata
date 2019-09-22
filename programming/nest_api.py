from typing import List
from fastapi import FastAPI, Query, Body, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED


from nest_lib import nest_dicts


app = FastAPI()
security = HTTPBasic()

USERNAME = "admin"
PASSWORD = "admin"


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != USERNAME or credentials.password != PASSWORD:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.post("/api/v1/nest_dicts")
async def nest_dicts_api(
    input_data: List[dict] = Body(..., min_length=1),
    nesting_keys: List[str] = Query(..., min_length=1),
    username: str = Depends(get_current_username),
):
    try:
        return nest_dicts(input_data, nesting_keys)
    except ValueError as err:
        return {"error": str(err)}, 422
