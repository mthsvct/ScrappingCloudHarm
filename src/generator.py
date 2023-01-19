from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image
import requests
import os
import pandas as pd
from provider import Provider


class Generator():
    
    def __init__(self, url):
        self.url = url
        self.html = None
        self.providers = []
        self.blocks = []

        self.sequence()
    
    def sequence(self):
        self.getProvidersOfHarmony()
        self.getProviders()

    def getProvidersOfHarmony(self):
        self.html = urlopen(self.url)
        bs = BeautifulSoup(self.html, 'html.parser')
        self.blocks = bs.find_all('div', {'class': 'provider_block'})

        pass

    def getProviders(self):
        for i in self.blocks:
            name = self.getName(i)
            link = self.getLink(i)
            description = self.getDescription(i)
            url_harmony = self.getUrlHarmony(i)
            self.providers.append(Provider(name, link, description))
    
    # Retorna o nome do provedor.
    def getName(self, block):
        return block.find('header').find('h3').text

    # Retorna o link do provedor.
    def getLink(self, block):
        return block.find('article').find_all('p', {'class': 'prov_links'})[0].find('a', {'class': 'text_square'})['href']

    # Retorna a descricao do provedor.
    def getDescription(self, block):
        return block.find('article').find_all('p', {'class': 'readMore'})[0].text

    def getUrlHarmony(self, block):
        init = 'https://cloudharmony.com'
        link =  block.find('article').find_all('p', {'class': 'prov_links'})[0].find_all('a', {'class': 'text_square'})[1]['href']
        print(init+link)
        return init + link

a = Generator('https://cloudharmony.com/directory')
