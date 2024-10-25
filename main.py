import json
import sys

from Src.Scrapers.wikis.Scraper import Scraper
from Src.Scrapers.links.Links import Links
from Src.Core.FileWriter import FileWriter
from Src.Core.Config import stash
from Src.Core.functions import get_urls


def wiki(predefined_url = None):
  url = predefined_url or sys.argv[2]
  path = url.split("/" )[-1]

  scraper = Scraper(url)
  scraper.scrape()

  fileWriter = FileWriter(f"Wikis/{path}.json", stash.resolve("full_wiki"))
  fileWriter.write()


def wikis():
  for url in get_urls("Urls/all.json"):
    wiki(url)


def links():
  url = sys.argv[2]

  links = Links(url)
  links.scrape()

  writer = FileWriter("Urls/all.json", stash.resolve("links"))
  writer.write()

def write2db():
  from Src.Core.DatabaseWriter import DatabaseWriter
  databaseWriter = DatabaseWriter("production", "wikis")
  databaseWriter.write()

if __name__ == "__main__":
  action = sys.argv[1]
  if action == "--wikis":
    wikis()
  elif action == "--wiki":
    wiki()
  elif action == "--links":
    links()
  elif action == "--write2db":
    write2db()


