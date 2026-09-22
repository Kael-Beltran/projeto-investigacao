import investigadores
import casos
import suspeitos
import vitimas
import evidencias
import testemunhas
import pericias


while True:

    print("\n==============================")
    print("   SISTEMA DE INVESTIGAÇÃO")
    print("==============================")

    print("\n1 - Listar")
    print("2 - Pesquisar")
    print("3 - Cadastrar")
    print("4 - Atualizar")
    print("5 - Excluir")
    print("0 - Sair")

    escolha = input("\nEscolha: ")

    if escolha == "0":
        print("Programa encerrado.")
        break

    elif escolha == "1":

        while True:

            print("\n--- LISTAR ---")

            print("\n1 - Investigadores")
            print("2 - Casos")
            print("3 - Suspeitos")
            print("4 - Vítimas")
            print("5 - Evidências")
            print("6 - Testemunhas")
            print("7 - Perícias")
            print("0 - Voltar")

            tabela = input("\nEscolha: ")

            if tabela == "1":
                investigadores.listar()

            elif tabela == "2":
                casos.listar()

            elif tabela == "3":
                suspeitos.listar()

            elif tabela == "4":
                vitimas.listar()

            elif tabela == "5":
                evidencias.listar()

            elif tabela == "6":
                testemunhas.listar()

            elif tabela == "7":
                pericias.listar()

            elif tabela == "0":
                break

            else:
                print("Opção inválida.")


    elif escolha == "2":

        while True:

            print("\n--- PESQUISAR ---")

            print("\n1 - Investigadores")
            print("2 - Casos")
            print("3 - Suspeitos")
            print("4 - Vítimas")
            print("5 - Evidências")
            print("6 - Testemunhas")
            print("7 - Perícias")
            print("0 - Voltar")

            tabela = input("\nEscolha: ")

            if tabela == "1":
                investigadores.pesquisar()

            elif tabela == "2":
                casos.pesquisar()

            elif tabela == "3":
                suspeitos.pesquisar()

            elif tabela == "4":
                vitimas.pesquisar()

            elif tabela == "5":
                evidencias.pesquisar()

            elif tabela == "6":
                testemunhas.pesquisar()

            elif tabela == "7":
                pericias.pesquisar()

            elif tabela == "0":
                break

            else:
                print("Opção inválida.")


    elif escolha == "3":

        while True:

            print("\n--- CADASTRAR ---")

            print("\n1 - Investigador")
            print("2 - Caso")
            print("3 - Suspeito")
            print("4 - Vítima")
            print("5 - Evidência")
            print("6 - Testemunha")
            print("7 - Perícia")
            print("0 - Voltar")

            tabela = input("\nEscolha: ")

            if tabela == "1":
                investigadores.cadastrar()

            elif tabela == "2":
                casos.cadastrar()

            elif tabela == "3":
                suspeitos.cadastrar()

            elif tabela == "4":
                vitimas.cadastrar()

            elif tabela == "5":
                evidencias.cadastrar()

            elif tabela == "6":
                testemunhas.cadastrar()

            elif tabela == "7":
                pericias.cadastrar()

            elif tabela == "0":
                break

            else:
                print("Opção inválida.")


    elif escolha == "4":

        while True:

            print("\n--- ATUALIZAR ---")

            print("\n1 - Investigador")
            print("2 - Caso")
            print("3 - Suspeito")
            print("4 - Vítima")
            print("5 - Evidência")
            print("6 - Testemunha")
            print("7 - Perícia")
            print("0 - Voltar")

            tabela = input("\nEscolha: ")

            if tabela == "1":
                investigadores.atualizar()

            elif tabela == "2":
                casos.atualizar()

            elif tabela == "3":
                suspeitos.atualizar()

            elif tabela == "4":
                vitimas.atualizar()

            elif tabela == "5":
                evidencias.atualizar()

            elif tabela == "6":
                testemunhas.atualizar()

            elif tabela == "7":
                pericias.atualizar()

            elif tabela == "0":
                break

            else:
                print("Opção inválida.")


    elif escolha == "5":

        while True:

            print("\n--- EXCLUIR ---")

            print("\n1 - Investigador")
            print("2 - Caso")
            print("3 - Suspeito")
            print("4 - Vítima")
            print("5 - Evidência")
            print("6 - Testemunha")
            print("7 - Perícia")
            print("0 - Voltar")

            tabela = input("\nEscolha: ")

            if tabela == "1":
                investigadores.excluir()

            elif tabela == "2":
                casos.excluir()

            elif tabela == "3":
                suspeitos.excluir()

            elif tabela == "4":
                vitimas.excluir()

            elif tabela == "5":
                evidencias.excluir()

            elif tabela == "6":
                testemunhas.excluir()

            elif tabela == "7":
                pericias.excluir()

            elif tabela == "0":
                break

            else:
                print("Opção inválida.")

    else:
        print("Opção inválida.")