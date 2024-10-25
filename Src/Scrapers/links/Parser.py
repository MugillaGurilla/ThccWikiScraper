from Src.Core.Config import stash

class LinkParser: 
  def parse(self):
    links = []
    for element in stash.resolve("body_content"):
      links.append("https://www.towerhamletscanoeclub.co.uk/" + element.next_element.get("href"))
    stash.bind("links", links)
  