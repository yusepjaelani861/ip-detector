# IP Detector API
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

IP Detector API based on MaxMind GeoIP2, this API is used to detect the location of an IP address.

## Server Requirement
- Python 3.12.2 or higher

## Installation

Production mode please using Dockerfile.

You can change the port number in the Dockerfile.

```sh
docker build -t ip-detector-api .
docker run -p 4040:4040 -d ip-detector-api
```

Development mode please using the following command.

```sh
pip install -r requirements.txt
cd app
uvicorn server.app:app --reload
```

## Usage

```
http://127.0.0.1:4040
```

## Authorization (optional)
Bearer {token}

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)