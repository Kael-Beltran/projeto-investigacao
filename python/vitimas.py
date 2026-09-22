from banco import conectar


def listar():
    banco = conectar()
    dados = banco.execute("""
        SELECT * FROM vitimas
    """).fetchall()
    banco.close()

    if dados:
        print("\n--- VITIMAS ---")
        for registro in dados:
            print(registro)
    else:
        print("Nenhum registro encontrado.")


def pesquisar():
    id = input("Digite o ID do vítima: ")
    banco = conectar()
    registro = banco.execute("""
        SELECT * FROM vitimas
        WHERE id = ?
    """, (id,)).fetchone()
    banco.close()

    if registro:
        print("\nVítima encontrado:")
        print(registro)
    else:
        print("Vítima não encontrado.")


def cadastrar():
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    caso_id = input("ID do caso: ")

    banco = conectar()
    banco.execute("""
        INSERT INTO vitimas (nome, data_nascimento, cpf, telefone, caso_id)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, data_nascimento, cpf, telefone, caso_id,))
    banco.commit()
    banco.close()
    print("Vítima cadastrado com sucesso.")


def atualizar():
    id = input("Digite o ID do vítima que deseja atualizar: ")
    nome = input("Novo nome: ")
    data_nascimento = input("Nova data de nascimento: ")
    cpf = input("Novo CPF: ")
    telefone = input("Novo telefone: ")
    caso_id = input("Novo ID do caso: ")

    banco = conectar()
    cursor = banco.execute("""
        UPDATE vitimas
        SET nome = ?,
            data_nascimento = ?,
            cpf = ?,
            telefone = ?,
            caso_id = ?
        WHERE id = ?
    """, (nome, data_nascimento, cpf, telefone, caso_id, id))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Vítima atualizado com sucesso.")
    else:
        print("Vítima não encontrado.")


def excluir():
    id = input("Digite o ID do vítima que deseja excluir: ")
    confirmar = input("Tem certeza que deseja excluir? (s/n): ").lower()

    if confirmar != "s":
        print("Exclusão cancelada.")
        return

    banco = conectar()
    cursor = banco.execute("""
        DELETE FROM vitimas
        WHERE id = ?
    """, (id,))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Vítima excluído com sucesso.")
    else:
        print("Vítima não encontrado.")
