# -*- coding: utf-8 -*-

import requests as r
from bs4 import BeautifulSoup


def sinonimos(palavra):
  site = f'https://www.sinonimos.com.br/{palavra}/'
  content = r.get(site)
  soup = BeautifulSoup(content.text, "html.parser")
  sentidos = soup.find_all("div", {'class':'s-wrapper'})
  resposta = {}

  for sentido in sentidos:
    texto_setido = sentido.find_all("div", {'class':'sentido'})
    resposta[texto_setido[0].text.replace(':', '')] = [a.text for a in sentido.find_all("a", {'class':'sinonimo'})]

  return resposta




