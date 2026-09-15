from banco import conectar


def listar():
    banco = conectar()

    dados = banco.execute("""
        SELECT * FROM testemunhas
    """).fetchall()

    banco.close()

    print("\n--- TESTEMUNHAS ---")

    for testemunha in dados:
        print(testemunha)


def pesquisar():
    id = input("Digite o ID da testemunha: ")

    banco = conectar()

    testemunha = banco.execute("""
        SELECT * FROM testemunhas
        WHERE id = ?
    """, (id,)).fetchone()

    banco.close()

    if testemunha:
        print("\n--- TESTEMUNHA ENCONTRADA ---")
        print(testemunha)
    else:
        print("Testemunha não encontrada.")