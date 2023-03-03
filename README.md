# REST API using OpenAI's GPT-3

This is a REST API that uses Azure OpenAI's GPT-3 to generate responses to user messages.

## Prerequisites

To run this chatbot, you will need the following:

- Python 3.7 or higher
- An OpenAI API key
- `pip` package manager

## Installation

1. Clone this repository to your local machine.

2. Install the required libraries using `pip`:
```
pip install -r requirements.txt
```

3. Set up the environment variables in a `.env` file. You can copy the `.env.example` file and rename it to `.env`, then replace the placeholders with your own API key and bot token.

```
OPENAI_API_TYPE=azure
OPENAI_API_VERSION=2022-12-01
OPENAI_NAME=
OPENAI_API_KEY=
ENGINE=
MAX_TOKENS=
TEMPERATURE=
FREQUENCY_PENALTY=
PRESENCE_PENALTY=
TOP_P=
STOP=[]
PREPROMPT=
```

Make sure to keep the `.env` file private and do not commit it to version control.

## Usage

1. Start the bot by running the following command:
```
gunicorn wsgi:app
```
or in Docker
```
docker build -t openai-api .
docker run -d -p 80:80 --env-file .env openai-api
```

2. Send a API request, for example:
```
curl --location --request POST 'http://localhost/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "prompt": "Hi"
}'
```


## Contributing

If you'd like to contribute to this project, please open an issue or pull request on GitHub.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

