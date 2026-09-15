from banco import conectar


def listar():
    banco = conectar()

    dados = banco.execute("""
        SELECT * FROM vitimas
    """).fetchall()

    banco.close()

    print("\n--- VÍTIMAS ---")

    for vitima in dados:
        print(vitima)


def pesquisar():
    id = input("Digite o ID da vítima: ")

    banco = conectar()

    vitima = banco.execute("""
        SELECT * FROM vitimas
        WHERE id = ?
    """, (id,)).fetchone()

    banco.close()

    if vitima:
        print("\n--- VÍTIMA ENCONTRADA ---")
        print(vitima)
    else:
        print("Vítima não encontrada.")