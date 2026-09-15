from banco import conectar


def listar():
    banco = conectar()

    dados = banco.execute("""
        SELECT * FROM evidencias
    """).fetchall()

    banco.close()

    print("\n--- EVIDÊNCIAS ---")

    for evidencia in dados:
        print(evidencia)


def pesquisar():
    id = input("Digite o ID da evidência: ")

    banco = conectar()

    evidencia = banco.execute("""
        SELECT * FROM evidencias
        WHERE id = ?
    """, (id,)).fetchone()

    banco.close()

    if evidencia:
        print("\n--- EVIDÊNCIA ENCONTRADA ---")
        print(evidencia)
    else:
        print("Evidência não encontrada.")