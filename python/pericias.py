from banco import conectar


def listar():
    banco = conectar()
    dados = banco.execute("""
        SELECT * FROM pericias
    """).fetchall()
    banco.close()

    if dados:
        print("\n--- PERICIAS ---")
        for registro in dados:
            print(registro)
    else:
        print("Nenhum registro encontrado.")


def pesquisar():
    id = input("Digite o ID do perícia: ")
    banco = conectar()
    registro = banco.execute("""
        SELECT * FROM pericias
        WHERE id = ?
    """, (id,)).fetchone()
    banco.close()

    if registro:
        print("\nPerícia encontrado:")
        print(registro)
    else:
        print("Perícia não encontrado.")


def cadastrar():
    tipo = input("Tipo: ")
    descricao = input("Descrição: ")
    resultado = input("Resultado: ")
    perito_responsavel = input("Perito responsável: ")
    data_pericia = input("Data da perícia: ")
    evidencia_id = input("ID da evidência: ")
    caso_id = input("ID do caso: ")

    banco = conectar()
    banco.execute("""
        INSERT INTO pericias (tipo, descricao, resultado, perito_responsavel, data_pericia, evidencia_id, caso_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (tipo, descricao, resultado, perito_responsavel, data_pericia, evidencia_id, caso_id,))
    banco.commit()
    banco.close()
    print("Perícia cadastrado com sucesso.")


def atualizar():
    id = input("Digite o ID do perícia que deseja atualizar: ")
    tipo = input("Novo tipo: ")
    descricao = input("Nova descrição: ")
    resultado = input("Novo resultado: ")
    perito_responsavel = input("Novo perito responsável: ")
    data_pericia = input("Nova data da perícia: ")
    evidencia_id = input("Novo ID da evidência: ")
    caso_id = input("Novo ID do caso: ")

    banco = conectar()
    cursor = banco.execute("""
        UPDATE pericias
        SET tipo = ?,
            descricao = ?,
            resultado = ?,
            perito_responsavel = ?,
            data_pericia = ?,
            evidencia_id = ?,
            caso_id = ?
        WHERE id = ?
    """, (tipo, descricao, resultado, perito_responsavel, data_pericia, evidencia_id, caso_id, id))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Perícia atualizado com sucesso.")
    else:
        print("Perícia não encontrado.")


def excluir():
    id = input("Digite o ID do perícia que deseja excluir: ")
    confirmar = input("Tem certeza que deseja excluir? (s/n): ").lower()

    if confirmar != "s":
        print("Exclusão cancelada.")
        return

    banco = conectar()
    cursor = banco.execute("""
        DELETE FROM pericias
        WHERE id = ?
    """, (id,))
    banco.commit()
    banco.close()

    if cursor.rowcount > 0:
        print("Perícia excluído com sucesso.")
    else:
        print("Perícia não encontrado.")
