import os
from zipfile import ZipFile


def find_download_path():
    """Determina onde salvar os arquivos."""
    if os.path.exists("public"):
        return "public/"
    if os.path.exists("../../public"):
        return "../../public/"
    return "./"


def zip_files(files: list[str], dest):
    """Agrupa arquivos em um container .zip"""
    with ZipFile(dest, "w") as zip_:
        print(f"Argupando em: {os.path.abspath(dest)}")
        for file in files:
            zip_.write(file, file.split("/")[-1])


def cleanup(files):
    """Remove os arquivos temporários."""
    for file in files:
        os.remove(file)