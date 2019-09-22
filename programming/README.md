# Nest

`Nesting flat json lists since 2019`


Note: Please switch to the project directory (that is `programming/`)
before running any of the commands below.

## Requirements

This was developed with Python 3.7 so please make sure you have it
installed an running.

The CLI `nest.py` requires no external requirements. However, the API
and tests require a few. For simplicity, all requirements are inside
`requirements.txt` file. 

You might want to run the following command in a virtualenv.

```shell
pip install -r requirements.txt
```

## Running the tests

Tests rely on pytest being installed which is included in the
`requirements.txt` file.

Running tests is as simple as running the command below:

```shell
pytest
```

Note: The `pexpect` library that is being used to test the `nest.py`
as a CLI script might not behave correctly on Windows. They should run
fine on Linux/MacOS machines though.

The three modules in this program, `nest_lib.py`, `nest_api.py` and
`nest.py` are tested with the same input/output parameters in their
respective unit tests.

The input and output content are supplied through fixture files in
`tests/fixtures/` directory. They are then read for each test with
mapping specified in `utils.COMMON_TEST_PARAMS`.


## The CLI script (Task 1)

The script `nest.py` can be run as follows:

```
cat <input_json_path> | python nest.py <nesting_key_1> <nesting_key_2> ...<nesting_key_n>
```

There exists the `input.json` file from the challenge instructions as
`tests/fixtures/input.json`. To test using that:

```
cat tests/fixtures/input.json | python nest.py currency country city
```

Running the command should spit something like this on the console.

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
  },
  ...
]
```

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

Or, you can use `curl` like this. (Looks awful, auto-generated)


```shell

curl -i -H Authorization\:\ Basic\ YWRtaW46YWRtaW4\= -XPOST http\://localhost\:8000/api/v1/nest_dicts\?nesting_keys\=currency\&nesting_keys\=country\&nesting_keys\=city -d \[\{\"country\"\:\ \"US\"\,\ \"city\"\:\ \"Boston\"\,\ \"currency\"\:\ \"USD\"\,\ \"amount\"\:\ 100\}\]
```

You should see something like this in your console:

```
HTTP/1.1 200 OK
date: Sun, 22 Sep 2019 16:14:48 GMT
server: uvicorn
content-length: 42
content-type: application/json

{"USD":{"US":{"Boston":[{"amount":100}]}}}
```
