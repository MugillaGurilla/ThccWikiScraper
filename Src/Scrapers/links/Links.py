from Src.Scrapers.links.Fetcher import Fetcher
from Src.Scrapers.links.Parser import LinkParser
from Src.Core.Config import stash

class Links:
  def __init__(self, url):
    self.Fetcher = Fetcher(url)
    self.Parser = LinkParser()

  def scrape(self):
    self.Fetcher.fetch(".mw-allpages-body > ul > *")
    self.Parser.parse()