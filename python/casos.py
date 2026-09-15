from banco import conectar


def listar():
    banco = conectar()

    dados = banco.execute("""
        SELECT * FROM casos
    """).fetchall()

    banco.close()

    if dados:
        print("\n--- CASOS ---")

        for registro in dados:
            print(registro)
    else:
        print("Nenhum caso encontrado.")


def pesquisar():
    id = input("Digite o ID do caso: ")

    banco = conectar()

    registro = banco.execute("""
        SELECT * FROM casos
        WHERE id = ?
    """, (id,)).fetchone()

    banco.close()

    if registro:
        print("\nCaso encontrado:")
        print(registro)
    else:
        print("Caso não encontrado.")