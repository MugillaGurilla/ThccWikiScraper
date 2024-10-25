import json 
import re

def get_urls(file):
  file = open(file)
  urls = json.load(file)
  return urls

def slugify(text):
  return re.sub(r'[^a-zA-Z0-9 ]', '', text).lower().strip().replace(" ", "-").replace("-+", "-")
