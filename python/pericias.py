from banco import conectar


def listar():
    banco = conectar()

    dados = banco.execute("""
        SELECT * FROM pericias
    """).fetchall()

    banco.close()

    if dados:
        print("\n--- PERÍCIAS ---")

        for registro in dados:
            print(registro)
    else:
        print("Nenhuma perícia encontrada.")


def pesquisar():
    id = input("Digite o ID da perícia: ")

    banco = conectar()

    registro = banco.execute("""
        SELECT * FROM pericias
        WHERE id = ?
    """, (id,)).fetchone()

    banco.close()

    if registro:
        print("\nPerícia encontrada:")
        print(registro)
    else:
        print("Perícia não encontrada.")