class Stash:
  def __init__(self):
    self.stash = {}

  def bind(self, key, value):
    self.stash[key] = value

  def resolve(self, key):
    return self.stash[key]

