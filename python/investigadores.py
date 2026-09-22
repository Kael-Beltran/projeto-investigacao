from banco import conectar


def listar():
    banco = conectar()
    dados = banco.execute("""
        SELECT * FROM investigadores
    """).fetchall()
    banco.close()

    if dados:
        print("\n--- INVESTIGADORES ---")
        for registro in dados:
            print(registro)
    else:
        print("Nenhum registro encontrado.")


def pesquisar():
    id = input("Digite o ID do investigador: ")
    banco = conectar()
    registro = banco.execute("""
        SELECT * FROM investigadores
        WHERE id = ?
    """, (id,)).fetchone()
    banco.close()

    if registro:
        print("\nInvestigador encontrado:")
        print(registro)
    else:
        print("Investigador não encontrado.")


def cadastrar():
    nome = input("Nome: ")
    matricula = input("Matrícula: ")
    cargo = input("Cargo: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    banco = conectar()
    banco.execute("""
        INSERT INTO investigadores (nome, matricula, cargo, telefone, email)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, matricula, cargo, telefone, email,))
    banco.commit()
    banco.close()
    print("Investigador cadastrado com sucesso.")


def atualizar():
    id = input("Digite o ID do investigador que deseja atualizar: ")
    nome = input("Novo nome: ")
    cargo = input("Novo cargo: ")
    telefone = input("Novo telefone: ")
    email = input("Novo e-mail: ")

    banco = conectar()
    cursor = banco.execute("""
        UPDATE investigadores
        SET nome = ?,
            cargo = ?,
            telefone = ?,
            email = ?
        WHERE id = ?
    """, (nome, cargo, telefone, email, id))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Investigador atualizado com sucesso.")
    else:
        print("Investigador não encontrado.")


def excluir():
    id = input("Digite o ID do investigador que deseja excluir: ")
    confirmar = input("Tem certeza que deseja excluir? (s/n): ").lower()

    if confirmar != "s":
        print("Exclusão cancelada.")
        return

    banco = conectar()
    cursor = banco.execute("""
        DELETE FROM investigadores
        WHERE id = ?
    """, (id,))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Investigador excluído com sucesso.")
    else:
        print("Investigador não encontrado.")
