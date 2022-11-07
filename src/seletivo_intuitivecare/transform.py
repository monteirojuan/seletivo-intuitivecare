"""Parte 1 do Teste processo seletivo IntutiveCare

Objetivo: Extrair dados de um arquivo .pdf para um .csv.
"""
import os
import re
from zipfile import ZipFile

import tabula

from seletivo_intuitivecare import utils

path = utils.find_download_path()


def transform():
    """Realiza o objetivo do teste 2."""
    file_path = unzip()
    print("Extraindo dados do pdf.")
    tabula.convert_into(file_path, path + "Anexo I.csv", output_format="csv", pages="all")
    utils.zip_files([path + "Anexo I.csv"], path + "Teste_Juan_Monteiro.zip")
    utils.cleanup([file_path, path + "Anexo I.csv"])


def unzip():
    """Extrai pdf do Anexo I"""
    if not os.path.exists(path + "teste1.zip"):
        raise FileNotFoundError("O arquivo do teste um não foi encontrado.")

    with ZipFile(f"{path}teste1.zip") as zip_:
        files = zip_.filelist
        for file in files:
            if re.search("Anexo_I_.*\.pdf$", file.filename):
                print(f"Extraindo arquivo {file.filename}")
                return zip_.extract(file.filename, path)


if __name__ == "__main__":
    transform()
