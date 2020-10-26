'''
Adriel Fernando

last update at 26/10/20 | 12:52 PM

'''

import requests
import webbrowser
import clipboard
from bs4 import BeautifulSoup
from time import sleep

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.191"}

def findLink(htmlRaw):
	lista_brainly = []
	bs = BeautifulSoup(htmlRaw, 'lxml')
	for link in bs.find_all('a', href=True):
		link = link['href']
		if 'brainly' in link:
			lista_brainly.append(link)

	return lista_brainly

def main(question):
	url = "https://www.bing.com/search?q={}%3A+*&search=&form=QBLH".format(question.replace(" ", "+"))
	r = requests.get(url, headers=header).text

	lista = findLink(r)
	'''
	for link in lista:
		webbrowser.open(link)
	'''
	if lista:
		print("Links Encontrados: {}\n----\n".format(lista))
		webbrowser.open(lista[0])

print("Aplicao Rodando!")
pesquisas = []

while True:
	sleep(0.2)
	texto = clipboard.paste()
	if ("http" not in texto):
		print("----\nPergunta: {}".format(texto))
		clipboard.copy("")
		try:
			texto = texto.split('\n')[0]
			if(texto not in pesquisas):
				main(texto)
			pesquisas.append(texto)
		except:
			pass
			#print("Texto sem formato!")
