"""Parte 1 do Teste processo seletivo IntutiveCare

Objetivo: baixar anexos (I a IV) e agrupar em um arquivo zip.
"""
import os
import re

import requests
from bs4 import BeautifulSoup

from seletivo_intuitivecare import utils

URL = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"


def scrape():
    """Realiza o objetivo do teste 1."""
    path = find_download_path()
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    urls = [link["href"] for link in soup.find_all(name="a", href=True, text=re.compile("Anexo"))]
    files_path = download_files(urls, path)
    utils.zip_files(files_path, path + "teste1.zip")
    utils.cleanup(files_path)


def download_files(urls: list[str], path) -> list[str]:
    """Faz o download dos arquivos."""
    files = []
    for url in urls:
        file_name = path + url.split("/")[-1]
        print(f"Baixando: {url}")
        save(requests.get(url, stream=True), file_name)
        files.append(file_name)
    return files


def save(request: requests.Response, file_path: str):
    """Salva o resultado de uma requisição."""
    with open(file_path, 'wb') as fd:
        for chunk in request.iter_content(chunk_size=256):
            fd.write(chunk)


def find_download_path():
    """Determina onde salvar os arquivos."""
    if os.path.exists("public"):
        return "public/"
    if os.path.exists("../../public"):
        return "../../public/"
    return "./"


if __name__ == '__main__':
    scrape()
