"""Parte 1 do Teste processo seletivo IntutiveCare

Objetivo: baixar anexos (I a IV) e agrupar em um arquivo zip.
"""
import os
import re

import requests
from bs4 import BeautifulSoup

URL = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"


def scrape():
    """Realiza o objetivo do teste 1."""
    path = find_download_foder()
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for link in soup.find_all(name="a", href=True, text=re.compile("Anexo")):
        file_name = link["href"].split("/")[-1]
        request = requests.get(link["href"], stream=True)
        save(request, path + file_name)


def save(request: requests.Response, file_path: str):
    """Salva o resultado de uma requisição."""
    with open(file_path, 'wb') as fd:
        for chunk in request.iter_content(chunk_size=256):
            fd.write(chunk)


def find_download_foder():
    """Determina onde salvar os arquivos."""
    if os.path.exists("public"):
        return "public/"
    if os.path.exists("../../public"):
        return "../../public/"
    return "./"


if __name__ == '__main__':
    scrape()
