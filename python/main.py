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

    else:
        print("Opção inválida.")