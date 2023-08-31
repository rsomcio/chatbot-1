# Simple Technical Assistant

This is a simple chatbot based on the OpenAI API.

### Prerequisites

```
brew install sqlite
```

### Load sample data (data.json)

```
python load-data.py
```

### Add API keys to constants.py file

Grab your api keys from [OpenAI API Keys](https://platform.openai.com/account/api-keys).

```
APIKEY = "<your OpenAI API key>"
```

### Install flask and run

```
python3.11 -m venv env
pip install flask
python main.py
```

### Testing

```
curl --location 'localhost:5000/chat' \
--header 'Content-Type: application/json' \
--data '{
"prompt": "How many bedrooms does the house on 123 Main Street have?"
}'

```

References

[OpenAI Chat API](https://platform.openai.com/docs/api-reference/chat/create)
