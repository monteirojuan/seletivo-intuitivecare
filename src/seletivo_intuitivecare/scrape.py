"""Parte 1 do Teste processo seletivo IntutiveCare

Objetivo: baixar anexos (I a IV) e agrupar em um arquivo zip.
"""
import re

import requests
from bs4 import BeautifulSoup

URL = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"


def download():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for link in soup.find_all(name="a", href=True, text=re.compile("Anexo")):
        file_name = link["href"].split("/")[-1]
        file = requests.get(link["href"], stream=True)
        with open(file_name, 'wb') as fd:
            for chunk in file.iter_content(chunk_size=256):
                fd.write(chunk)


if __name__ == '__main__':
    download()
