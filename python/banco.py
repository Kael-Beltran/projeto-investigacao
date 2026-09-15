import sqlite3
import os


def conectar():
    caminho = os.path.join(
        os.path.dirname(__file__),
        "..",
        "sistema_policial.db"
    )

    return sqlite3.connect(caminho)