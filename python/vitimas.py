from banco import conectar


def listar():
    banco = conectar()

    dados = banco.execute("""
        SELECT * FROM vitimas
    """).fetchall()

    banco.close()

    if dados:
        print("\n--- VÍTIMAS ---")

        for registro in dados:
            print(registro)
    else:
        print("Nenhuma vítima encontrada.")


def pesquisar():
    id = input("Digite o ID da vítima: ")

    banco = conectar()

    registro = banco.execute("""
        SELECT * FROM vitimas
        WHERE id = ?
    """, (id,)).fetchone()

    banco.close()

    if registro:
        print("\nVítima encontrada:")
        print(registro)
    else:
        print("Vítima não encontrada.")