from banco import conectar


def listar():
    banco = conectar()

    dados = banco.execute("""
        SELECT * FROM investigadores
    """).fetchall()

    banco.close()

    print("\n--- INVESTIGADORES ---")

    for investigador in dados:
        print(investigador)


def pesquisar():
    id = input("Digite o ID do investigador: ")

    banco = conectar()

    investigador = banco.execute("""
        SELECT * FROM investigadores
        WHERE id = ?
    """, (id,)).fetchone()

    banco.close()

    if investigador:
        print("\n--- INVESTIGADOR ENCONTRADO ---")
        print(investigador)
    else:
        print("Investigador não encontrado.")