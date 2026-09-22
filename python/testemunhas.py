from banco import conectar


def listar():
    banco = conectar()
    dados = banco.execute("""
        SELECT * FROM testemunhas
    """).fetchall()
    banco.close()

    if dados:
        print("\n--- TESTEMUNHAS ---")
        for registro in dados:
            print(registro)
    else:
        print("Nenhum registro encontrado.")


def pesquisar():
    id = input("Digite o ID do testemunha: ")
    banco = conectar()
    registro = banco.execute("""
        SELECT * FROM testemunhas
        WHERE id = ?
    """, (id,)).fetchone()
    banco.close()

    if registro:
        print("\nTestemunha encontrado:")
        print(registro)
    else:
        print("Testemunha não encontrado.")


def cadastrar():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    depoimento = input("Depoimento: ")
    caso_id = input("ID do caso: ")

    banco = conectar()
    banco.execute("""
        INSERT INTO testemunhas (nome, telefone, endereco, depoimento, caso_id)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, telefone, endereco, depoimento, caso_id,))
    banco.commit()
    banco.close()
    print("Testemunha cadastrado com sucesso.")


def atualizar():
    id = input("Digite o ID do testemunha que deseja atualizar: ")
    nome = input("Novo nome: ")
    telefone = input("Novo telefone: ")
    endereco = input("Novo endereço: ")
    depoimento = input("Novo depoimento: ")
    caso_id = input("Novo ID do caso: ")

    banco = conectar()
    cursor = banco.execute("""
        UPDATE testemunhas
        SET nome = ?,
            telefone = ?,
            endereco = ?,
            depoimento = ?,
            caso_id = ?
        WHERE id = ?
    """, (nome, telefone, endereco, depoimento, caso_id, id))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Testemunha atualizado com sucesso.")
    else:
        print("Testemunha não encontrado.")


def excluir():
    id = input("Digite o ID do testemunha que deseja excluir: ")
    confirmar = input("Tem certeza que deseja excluir? (s/n): ").lower()

    if confirmar != "s":
        print("Exclusão cancelada.")
        return

    banco = conectar()
    cursor = banco.execute("""
        DELETE FROM testemunhas
        WHERE id = ?
    """, (id,))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Testemunha excluído com sucesso.")
    else:
        print("Testemunha não encontrado.")
