from banco import conectar


def listar():
    banco = conectar()
    dados = banco.execute("""
        SELECT * FROM casos
    """).fetchall()
    banco.close()

    if dados:
        print("\n--- CASOS ---")
        for registro in dados:
            print(registro)
    else:
        print("Nenhum registro encontrado.")


def pesquisar():
    id = input("Digite o ID do caso: ")
    banco = conectar()
    registro = banco.execute("""
        SELECT * FROM casos
        WHERE id = ?
    """, (id,)).fetchone()
    banco.close()

    if registro:
        print("\nCaso encontrado:")
        print(registro)
    else:
        print("Caso não encontrado.")


def cadastrar():
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    tipo_crime = input("Tipo de crime: ")
    data_abertura = input("Data de abertura: ")
    status = input("Status: ")
    investigador_id = input("ID do investigador responsável: ")

    banco = conectar()
    banco.execute("""
        INSERT INTO casos (titulo, descricao, tipo_crime, data_abertura, status, investigador_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (titulo, descricao, tipo_crime, data_abertura, status, investigador_id,))
    banco.commit()
    banco.close()
    print("Caso cadastrado com sucesso.")


def atualizar():
    id = input("Digite o ID do caso que deseja atualizar: ")
    titulo = input("Novo título: ")
    descricao = input("Nova descrição: ")
    tipo_crime = input("Novo tipo de crime: ")
    data_abertura = input("Nova data de abertura: ")
    status = input("Novo status: ")
    investigador_id = input("Novo ID do investigador responsável: ")

    banco = conectar()
    cursor = banco.execute("""
        UPDATE casos
        SET titulo = ?,
            descricao = ?,
            tipo_crime = ?,
            data_abertura = ?,
            status = ?,
            investigador_id = ?
        WHERE id = ?
    """, (titulo, descricao, tipo_crime, data_abertura, status, investigador_id, id))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Caso atualizado com sucesso.")
    else:
        print("Caso não encontrado.")


def excluir():
    id = input("Digite o ID do caso que deseja excluir: ")
    confirmar = input("Tem certeza que deseja excluir? (s/n): ").lower()

    if confirmar != "s":
        print("Exclusão cancelada.")
        return

    banco = conectar()
    cursor = banco.execute("""
        DELETE FROM casos
        WHERE id = ?
    """, (id,))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Caso excluído com sucesso.")
    else:
        print("Caso não encontrado.")
