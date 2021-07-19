'''
Adriel Fernando

last update at 19/07/20 | 20:51 PM

'''

import requests
from os import system
import webbrowser
import clipboard
from bs4 import BeautifulSoup
from time import sleep
from tkinter import messagebox
from tkinter import *

root = Tk()
root.geometry("0x0")

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
		#system("powershell -C Start-Process chrome.exe -ArgumentList @( '-incognito', '{}}' )".format(link))
	'''
	if lista:
		print("Links Encontrados: {}\n----\n".format(lista))
		num = len(lista)

		if(num >= 1):
			r = requests.get(lista[1], headers=header)
		elif(num >= 2):
			r = requests.get(lista[2], headers=header)
		else:
			r = requests.get(lista[0], headers=header)

		texto = r.text
		bs = BeautifulSoup(texto, 'lxml')
		resposta = bs.find_all('div', {'data-test':'answer-box-text'})
		#print(resposta)
		for i in resposta:
			#print(i.get_text())
			messagebox.showinfo("Resposta!!!", "Resposta: \n{}".format(i.get_text()))
			#print("Resposta: {}".format(i.get_text()))


print("Aplicao Rodando!")
pesquisas = []

while True:
	sleep(0.2)
	texto = clipboard.paste()
	if texto:
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


root.mainloop()
