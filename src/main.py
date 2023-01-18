from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image
import requests
import os
import pandas as pd


# Se o arquivo não existir, cria um arquivo CSV com as colunas nome, link, description. 
def openCSV():
    if not os.path.exists('providers.csv'):
        with open('providers.csv', 'w') as arq:
            arq.write('name,link\n')

# Retorna o nome do provedor.
def getName(block):
    return block.find('header').find('h3').text

# Retorna a descrição do provedor.
def getDescription(block):
    return block.find('article').find_all('p', {'class': 'readMore'})[0].text

# Retorna o link do provedor.
def getLink(block):
    return block.find('article').find_all('p', {'class': 'prov_links'})[0].find('a', {'class': 'text_square'})['href']

def writeLine(name, link):
    with open('providers.csv', 'a') as arq:
        arq.write(f"{name},{link}\n")

def save_csv(blocos):
    openCSV()
    for i in blocos:
        writeLine(getName(i), getLink(i))


html = urlopen("https://cloudharmony.com/directory")
bs = BeautifulSoup(html, 'html.parser')

blocks = bs.find_all('div', {'class': 'provider_block'})

print(len(blocks))
save_csv(blocks)





