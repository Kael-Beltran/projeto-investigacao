from banco import conectar


def listar():
    banco = conectar()

    dados = banco.execute("""
        SELECT * FROM suspeitos
    """).fetchall()

    banco.close()

    if dados:
        print("\n--- SUSPEITOS ---")

        for registro in dados:
            print(registro)
    else:
        print("Nenhum suspeito encontrado.")


def pesquisar():
    id = input("Digite o ID do suspeito: ")

    banco = conectar()

    registro = banco.execute("""
        SELECT * FROM suspeitos
        WHERE id = ?
    """, (id,)).fetchone()

    banco.close()

    if registro:
        print("\nSuspeito encontrado:")
        print(registro)
    else:
        print("Suspeito não encontrado.")