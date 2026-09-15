import investigadores
import casos
import suspeitos
import vitimas
import evidencias
import testemunhas
import pericias


while True:

    print("""
==============================
   SISTEMA DE INVESTIGAÇÃO
==============================

1 - Listar
2 - Pesquisar
0 - Sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":

        print("""
--- LISTAR ---

1 - Investigadores
2 - Casos
3 - Suspeitos
4 - Vítimas
5 - Evidências
6 - Testemunhas
7 - Perícias
0 - Voltar
""")

        escolha = input("Escolha: ")

        if escolha == "1":
            investigadores.listar()

        elif escolha == "2":
            casos.listar()

        elif escolha == "3":
            suspeitos.listar()

        elif escolha == "4":
            vitimas.listar()

        elif escolha == "5":
            evidencias.listar()

        elif escolha == "6":
            testemunhas.listar()

        elif escolha == "7":
            pericias.listar()


    elif opcao == "2":

        print("""
--- PESQUISAR ---

1 - Investigadores
2 - Casos
3 - Suspeitos
4 - Vítimas
5 - Evidências
6 - Testemunhas
7 - Perícias
0 - Voltar
""")

        escolha = input("Escolha: ")

        if escolha == "1":
            investigadores.pesquisar()

        elif escolha == "2":
            casos.pesquisar()

        elif escolha == "3":
            suspeitos.pesquisar()

        elif escolha == "4":
            vitimas.pesquisar()

        elif escolha == "5":
            evidencias.pesquisar()

        elif escolha == "6":
            testemunhas.pesquisar()

        elif escolha == "7":
            pericias.pesquisar()


    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")