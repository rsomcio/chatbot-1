# Simple Technical Assistant

### Prerequisites

```
brew install sqlite
```

### Load sample data (data.json)

```
python load-data.py
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
