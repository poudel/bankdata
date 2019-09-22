# Introduction

## Requirements

The CLI `nest.py` requires no external requirements. However, the API
and tests require a few. For simplicity, all requirements are inside
`requirements.txt` file. Install them by running:

```shell
pip install -r requirements.txt
```

## CLI (Task 1)



## API Endpoint (Task 2)

The framework [FastAPI](https://fastapi.tiangolo.com) is being used to
create the API service. To run the API we use `uvicorn` which is an
ASGI server. From the project directory, run:

```shell
uvicorn nest_api:app --reload
```

You can test the API using the Swagger UI at
[http://localhost:8000/docs](http://localhost:8000/docs).


### POST Endpoint `/api/v1/nest_dicts`

The post endpoint is a Basic auth protected endpoint. The credentials
have been hardcoded at the moment. The username and password are
`admin` and `admin` respectively. You can also use the ready made
header below:

```
{'Authorization': 'Basic YWRtaW46YWRtaW4='}
```

### Example request

If you send a request like this:

```
POST http://localhost:8000/api/v1/nest_dicts?nesting_keys=currency&nesting_keys=country&nesting_keys=city
Authorization: Basic YWRtaW46YWRtaW4=

[
  {
    "country": "US",
    "city": "Boston",
    "currency": "USD",
    "amount": 100
  }
]
```

You will receive a response like this:

```
{
  "USD": {
    "US": {
      "Boston": [
        {
          "amount": 100
        }
      ]
    }
  }
}
// POST http://localhost:8000/api/v1/nest_dicts?nesting_keys=currency&nesting_keys=country&nesting_keys=city
// HTTP/1.1 200 OK
// date: Sun, 22 Sep 2019 15:54:57 GMT
// server: uvicorn
// content-length: 42
// content-type: application/json
// Request duration: 0.006829s
```

## Running tests

After installing from `requirements.txt` file run the following
command:

```shell
pytest
```

Note: The tests should run fine on Linux/MacOS machines. The `pexpect`
library that is being used to test the `nest.py` as a CLI script might
not behave correctly in Windows.
