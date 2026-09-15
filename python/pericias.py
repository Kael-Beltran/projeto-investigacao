from banco import conectar


def listar():
    banco = conectar()

    dados = banco.execute("""
        SELECT * FROM pericias
    """).fetchall()

    banco.close()

    print("\n--- PERÍCIAS ---")

    for pericia in dados:
        print(pericia)


def pesquisar():
    id = input("Digite o ID da perícia: ")

    banco = conectar()

    pericia = banco.execute("""
        SELECT * FROM pericias
        WHERE id = ?
    """, (id,)).fetchone()

    banco.close()

    if pericia:
        print("\n--- PERÍCIA ENCONTRADA ---")
        print(pericia)
    else:
        print("Perícia não encontrada.")