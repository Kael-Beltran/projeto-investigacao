from banco import conectar


def listar():
    banco = conectar()
    dados = banco.execute("""
        SELECT * FROM evidencias
    """).fetchall()
    banco.close()

    if dados:
        print("\n--- EVIDENCIAS ---")
        for registro in dados:
            print(registro)
    else:
        print("Nenhum registro encontrado.")


def pesquisar():
    id = input("Digite o ID do evidência: ")
    banco = conectar()
    registro = banco.execute("""
        SELECT * FROM evidencias
        WHERE id = ?
    """, (id,)).fetchone()
    banco.close()

    if registro:
        print("\nEvidência encontrado:")
        print(registro)
    else:
        print("Evidência não encontrado.")


def cadastrar():
    descricao = input("Descrição: ")
    tipo = input("Tipo: ")
    local_encontrada = input("Local encontrada: ")
    data_coleta = input("Data da coleta: ")
    caso_id = input("ID do caso: ")

    banco = conectar()
    banco.execute("""
        INSERT INTO evidencias (descricao, tipo, local_encontrada, data_coleta, caso_id)
        VALUES (?, ?, ?, ?, ?)
    """, (descricao, tipo, local_encontrada, data_coleta, caso_id,))
    banco.commit()
    banco.close()
    print("Evidência cadastrado com sucesso.")


def atualizar():
    id = input("Digite o ID do evidência que deseja atualizar: ")
    descricao = input("Nova descrição: ")
    tipo = input("Novo tipo: ")
    local_encontrada = input("Novo local: ")
    data_coleta = input("Nova data da coleta: ")
    caso_id = input("Novo ID do caso: ")

    banco = conectar()
    cursor = banco.execute("""
        UPDATE evidencias
        SET descricao = ?,
            tipo = ?,
            local_encontrada = ?,
            data_coleta = ?,
            caso_id = ?
        WHERE id = ?
    """, (descricao, tipo, local_encontrada, data_coleta, caso_id, id))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Evidência atualizado com sucesso.")
    else:
        print("Evidência não encontrado.")


def excluir():
    id = input("Digite o ID do evidência que deseja excluir: ")
    confirmar = input("Tem certeza que deseja excluir? (s/n): ").lower()

    if confirmar != "s":
        print("Exclusão cancelada.")
        return

    banco = conectar()
    cursor = banco.execute("""
        DELETE FROM evidencias
        WHERE id = ?
    """, (id,))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Evidência excluído com sucesso.")
    else:
        print("Evidência não encontrado.")
