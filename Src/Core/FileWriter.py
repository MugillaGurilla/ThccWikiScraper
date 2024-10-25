import json 

class FileWriter: 
  def __init__(self, path, page_data):
    self.path = path
    self.page_data = page_data

  def write(self):
    with open (self.path, "w") as file:
      json.dump(self.page_data , file, indent=2)
