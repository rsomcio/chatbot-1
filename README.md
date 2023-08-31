# Simple Technical Assistant

This is a simple chatbot based on the OpenAI API.

### Prerequisites

```
brew install sqlite
```

```
python3.11 -m venv env
. env/bin/activate
pip install -r requirements.txt
```

### Load sample data (data.json)

```
python load-sample-data.py
```

### Add API keys to constants.py file

Grab your api keys from [OpenAI API Keys](https://platform.openai.com/account/api-keys).

```
APIKEY = "<your OpenAI API key>"
```

### Install flask and run

```
python app.py
```

### Code Coveage

Run the tests below:

```
pytest tests/
```

Generate Code Coverage Report:

```
coverage run  --source . -m pytest tests/
coverage report
coverage html
```

### Testing

```
test 1:

> $ curl --location 'localhost:5000/chat' \                                                                       ⬡ 19.7.0
--header 'Content-Type: application/json' \
--data '{
    "prompt": "How many bedrooms does the house on 555 pine road have?"
}'

response:

The house on 555 Pine Road has 2 bedrooms.%


test 2:

> $ curl --location 'localhost:5000/chat' \                                                                       ⬡ 19.7.0
--header 'Content-Type: application/json' \
--data '{
    "prompt": "How much is the house on 555 pine road cost?"
}'

response:

The house on 555 Pine Road is listed for 280,000 dollars.%

test 3:

> $ curl --location 'localhost:5000/chat' \                                                                       ⬡ 19.7.0
--header 'Content-Type: application/json' \
--data '{
    "prompt": "How much is the house cost?"
}'

response:

error: no valid context found%


test 4:

> $ curl --location 'localhost:5000/chat' \                                                                       ⬡ 19.7.0
--header 'Content-Type: application/json' \
--data '{
    "prompt": "How much is the house on 987 maple court?"
}'

response:

I'm sorry, as an AI, I do not have access to real-time property listings. Please contact a real estate agent or check an online real estate website for the most accurate and up-to-date information on the price of the house at 987 Maple Court.%


test 5:

> $ curl --location 'localhost:5000/chat' \                                                                       ⬡ 19.7.0
--header 'Content-Type: application/json' \
--data '{
    "prompt": "How much is the house on 987 maple court cost?"
}'

response:

The house on 987 Maple Court is priced at 1,200,000 dollars.%

```

References

[OpenAI Chat API](https://platform.openai.com/docs/api-reference/chat/create)
