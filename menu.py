from pprint import pprint
import sqlite3

conexao = sqlite3.connect("sistema_policial.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")


def buscar_dados_por_caso(id_caso, tabela_alvo):
    if tabela_alvo == "suspeitos":
        query = """
            SELECT s.nome AS suspeito, s.cpf, s.data_nascimento
            FROM suspeitos AS s
            WHERE s.caso_id = ?
        """
    elif tabela_alvo == "evidencias":
        query = """
            SELECT e.descricao AS evidencia, e.tipo, e.local_encontrada
            FROM evidencias AS e
            WHERE e.caso_id = ?
        """
    elif tabela_alvo == "testemunhas":
        query = """
            SELECT t.nome AS testemunha, t.telefone, t.depoimento
            FROM testemunhas AS t
            WHERE t.caso_id = ?
        """

    cursor.execute(query, (id_caso,))
    resultado = cursor.fetchall()

    print(f"\n--- {tabela_alvo.upper()} ENCONTRADOS ---")
    if resultado:
        pprint(resultado)
    else:
        print(f"Nenhum registro de {tabela_alvo} para este caso.")


def gerenciar_caso_especifico():
    print("\n================ CASOS DISPONÍVEIS ================")
    cursor.execute("SELECT id, titulo, tipo_crime FROM casos")
    pprint(cursor.fetchall())
    print("===================================================\n")

    id_caso = input("Digite o ID do caso que deseja investigar: ")

    cursor.execute("SELECT titulo FROM casos WHERE id = ?", (id_caso,))
    caso_existe = cursor.fetchone()

    if not caso_existe:
        print("\n❌ ID de caso inválido!")
        return

    while True:
        print("\n" + "-" * 40)
        print(f" INVESTIGANDO: {caso_existe[0].upper()} ")
        print("-" * 40)
        print("1- Ver Suspeitos")
        print("2- Ver Evidências")
        print("3- Ver Testemunhas")
        print("0- Voltar ao Menu Principal")
        print("-" * 40)

        sub_opcao = input("Escolha o que ver: ")

        if sub_opcao == "1":
            buscar_dados_por_caso(id_caso, "suspeitos")
        elif sub_opcao == "2":
            buscar_dados_por_caso(id_caso, "evidencias")
        elif sub_opcao == "3":
            buscar_dados_por_caso(id_caso, "testemunhas")
        elif sub_opcao == "0":
            break
        else:
            print("\n❌ Opção inválida!")


def cadastrar_novo_suspeito():
    print("\n--- SELECIONE O CASO RELACIONADO ---")
    cursor.execute("SELECT id, titulo FROM casos")
    pprint(cursor.fetchall())

    id_caso = input(
        "\nDigite o ID do caso ao qual este suspeito está envolvido: "
    )

    print("\n--- INFORMAÇÕES DO SUSPEITO ---")
    nome = input("Nome completo do suspeito: ")
    data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")
    cpf = input("CPF (xxx.xxx.xxx-xx): ")
    endereco = input("Endereço residencial: ")

    try:
        cursor.execute(
            """
            INSERT INTO suspeitos (nome, data_nascimento, cpf, endereco, caso_id)
            VALUES (?, ?, ?, ?, ?)
        """,
            (nome, data_nascimento, cpf, endereco, id_caso),
        )
        conexao.commit()
        print(
            f"\n Suspeito '{nome}' cadastrado com sucesso no caso {id_caso}!"
        )
    except sqlite3.IntegrityError:
        print(
            "\n Erro: Este ID de caso não existe ou o CPF digitado já está cadastrado!"
        )


while True:

    print("      SISTEMA DE INVESTIGAÇÃO POLICIAL      ")
    print("-" * 40)
    print("1- Selecionar Caso e Investigar Detalhes")
    print("2- Cadastrar Novo Suspeito")
    print("0- Sair do Sistema")
    print("-" * 40)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        gerenciar_caso_especifico()
    elif opcao == "2":
        cadastrar_novo_suspeito()
    elif opcao == "0":
        print("\n Encerrando o sistema.")
        conexao.close()
        break
    else:
        print("\n Opção inválida! Digite 1, 2 ou 0.")
