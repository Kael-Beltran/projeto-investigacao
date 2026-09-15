import sqlite3

# 1. Conecta ao arquivo (se não existir, o Python cria o arquivo .db vazio)
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# 2. Você escreve o CREATE TABLE aqui no código Python!
cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT
    )
""")
cursor.execute(
    "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
    ("Carlos Silva", "carlos@email.com")
)
cursor.execute("SELECT * FROM usuarios")

# 3. Salva as alterações e fecha
conexao.commit()
conexao.close()

