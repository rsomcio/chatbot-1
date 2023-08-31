import sqlite3
import json

# Create a connection to the SQLite database
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Create the 'context' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS context (
        keyword TEXT PRIMARY KEY,
        context TEXT
    )
''')

with open('data.json', 'r') as json_file:
    json_data = json.load(json_file)

# Sample data to populate the table
sample_data = [(entry.get("keyword", ""),entry.get("context", ""))for entry in json_data]


# Insert sample data into the table
for keyword, context in sample_data:
    cursor.execute('INSERT INTO context (keyword, context) VALUES (?, ?)', (keyword, context))

# Commit changes and close the connection
conn.commit()
conn.close()
