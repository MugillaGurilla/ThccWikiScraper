import requests
from bs4 import BeautifulSoup
from Src.Core.Config import stash

class Fetcher:
  def __init__(self, url):
    self.url = url

  def fetch(self, selector):
    response = requests.get(self.url)
    soup = BeautifulSoup(response.content, 'html.parser')
    body_content = soup.select(selector)
    stash.bind("body_content", body_content)
