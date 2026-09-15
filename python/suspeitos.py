from banco import conectar


def listar():
    banco = conectar()

    dados = banco.execute("""
        SELECT * FROM suspeitos
    """).fetchall()

    banco.close()

    print("\n--- SUSPEITOS ---")

    for suspeito in dados:
        print(suspeito)


def pesquisar():
    id = input("Digite o ID do suspeito: ")

    banco = conectar()

    suspeito = banco.execute("""
        SELECT * FROM suspeitos
        WHERE id = ?
    """, (id,)).fetchone()

    banco.close()

    if suspeito:
        print("\n--- SUSPEITO ENCONTRADO ---")
        print(suspeito)
    else:
        print("Suspeito não encontrado.")