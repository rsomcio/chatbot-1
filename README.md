# Simple Technical Assistant

This is a simple chatbot based on the OpenAI API.

### Prerequisites

```
brew install sqlite
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
python3.11 -m venv env
pip install flask
python main.py
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

sample data

```
    {
        "keyword": "789 Oak Lane",
        "context": "Spacious 4-bedroom house with a large backyard, listed at 750,000 dollars."
    },
    {
        "keyword": "555 Pine Road",
        "context": "Charming cottage-style home with 2 bedrooms, available for 280,000 dollars."
    },
    {
        "keyword": "987 Maple Court",
        "context": "Modern 5-bedroom residence with luxurious amenities, price set at 1,200,000 dollars."
    },
    {
        "keyword": "222 Cedar Street",
        "context": "Beautiful 4-bedroom house with a swimming pool, offered at 890,000 dollars."
    },
```

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
```

References

[OpenAI Chat API](https://platform.openai.com/docs/api-reference/chat/create)
