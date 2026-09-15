from pprint import pprint
import sqlite3

conexao = sqlite3.connect("sistema_policial.db")
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")


def listar_e_buscar_suspeitos():
    print("\n CASOS DISPONÍVEIS NO BANCO ")
    cursor.execute("SELECT id, titulo, tipo_crime FROM casos")
    todos_os_casos = cursor.fetchall()
    pprint(todos_os_casos)


    id_escolhido = input(
        "Olhe a lista acima e digite o ID do caso que deseja investigar: "
    )

    caso_suspeitos = cursor.execute(
        """
        SELECT c.titulo AS caso, s.nome AS suspeito, s.cpf
        FROM suspeitos AS s
        INNER JOIN casos AS c ON s.caso_id = c.id
        WHERE c.id = ?
    """,
        (id_escolhido,),
    )

    resultado = caso_suspeitos.fetchall()

    if resultado:
        print(f"\n SUSPEITOS DO CASO ID {id_escolhido} ")
        pprint(resultado)
    else:
        print(
            "\n Nenhum suspeito cadastrado para este caso ou o ID digitado é inválido."
        )


def cadastrar_novo_suspeito():
    print("\n SELECIONE O CASO RELACIONADO ")
    cursor.execute("SELECT id, titulo FROM casos")
    casos = cursor.fetchall()
    pprint(casos)

    id_caso = input(
        "\nDigite o ID do caso ao qual este suspeito está envolvido: "
    )

    print("\n INFORMAÇÕES DO SUSPEITO ")
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
            "\n❌ Erro: Este ID de caso não existe ou o CPF digitado já está cadastrado!"
        )


while True:
    print("\n" + "=" * 40)
    print("      SISTEMA DE INVESTIGAÇÃO POLICIAL      ")
    print("=" * 40)
    print(" Ver Casos e Listar Suspeitos")
    print(" Cadastrar Novo Suspeito")
    print(" Sair do Sistema")
    print("=" * 40)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_e_buscar_suspeitos()
    elif opcao == "2":
        cadastrar_novo_suspeito()
    elif opcao == "0":
        print("\n Encerrando o sistema e fechando o banco de dados. Até logo!")
        conexao.close()
        break
    else:
        print("\n❌ Opção inválida! Digite 1, 2 ou 0.")
