import json

class Provider():

    def __init__(self, name, url, url_harmony, description=""):
        self.name = name #.............................. The name of provider
        self.url = url #................................ The url of provider
        self.url_harmony = url_harmony #................ The url of provider in cloudharmony
        self.description = description #................ The description of provider
        self.services = [] #............................ The services of provider
    
    def __str__(self):
        return f"Name: {self.name}\nURL: {self.url}\nDescription: {self.description}\nLink Harmony: {self.link_harmony}"

    def saveJson(self):
        pass

    def saveCSV(self):
        pass