import json
import requests
import random

negative_keyword = ["chán vl", "mệt", "mệt vl", "chịu"]
encouragements = [
    "Cố lên, diu ken đú ịt!!!",
    "Don't worry bae, everything will be fine",
    "Aww, do you need a hug?",
    "Keep moving forward"
]

def get_quotes():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote
