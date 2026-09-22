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
        print("Nenhum registro encontrado.")


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


def cadastrar():
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    caso_id = input("ID do caso: ")

    banco = conectar()
    banco.execute("""
        INSERT INTO suspeitos (nome, data_nascimento, cpf, endereco, caso_id)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, data_nascimento, cpf, endereco, caso_id,))
    banco.commit()
    banco.close()
    print("Suspeito cadastrado com sucesso.")


def atualizar():
    id = input("Digite o ID do suspeito que deseja atualizar: ")
    nome = input("Novo nome: ")
    data_nascimento = input("Nova data de nascimento: ")
    cpf = input("Novo CPF: ")
    endereco = input("Novo endereço: ")
    caso_id = input("Novo ID do caso: ")

    banco = conectar()
    cursor = banco.execute("""
        UPDATE suspeitos
        SET nome = ?,
            data_nascimento = ?,
            cpf = ?,
            endereco = ?,
            caso_id = ?
        WHERE id = ?
    """, (nome, data_nascimento, cpf, endereco, caso_id, id))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Suspeito atualizado com sucesso.")
    else:
        print("Suspeito não encontrado.")


def excluir():
    id = input("Digite o ID do suspeito que deseja excluir: ")
    confirmar = input("Tem certeza que deseja excluir? (s/n): ").lower()

    if confirmar != "s":
        print("Exclusão cancelada.")
        return

    banco = conectar()
    cursor = banco.execute("""
        DELETE FROM suspeitos
        WHERE id = ?
    """, (id,))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Suspeito excluído com sucesso.")
    else:
        print("Suspeito não encontrado.")
