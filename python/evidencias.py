from banco import conectar


def listar():
    banco = conectar()

    dados = banco.execute("""
        SELECT * FROM evidencias
    """).fetchall()

    banco.close()

    if dados:
        print("\n--- EVIDÊNCIAS ---")

        for registro in dados:
            print(registro)
    else:
        print("Nenhuma evidência encontrada.")


def pesquisar():
    id = input("Digite o ID da evidência: ")

    banco = conectar()

    registro = banco.execute("""
        SELECT * FROM evidencias
        WHERE id = ?
    """, (id,)).fetchone()

    banco.close()

    if registro:
        print("\nEvidência encontrada:")
        print(registro)
    else:
        print("Evidência não encontrada.")