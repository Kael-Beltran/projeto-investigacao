import sqlite3
from pprint import pprint

conexao = sqlite3.connect("sistema_policial.db")
cursor = conexao.cursor()

def casos():
    casos = cursor.execute("""SELECT * FROM casos""")
    casos = cursor.fetchall()

    pprint(casos)

    return casos

#casos()

def investigadores():
    investigadores = cursor.execute("""SELECT * FROM investigadores""")
    investigadores = cursor.fetchall()

    pprint(investigadores)

    return investigadores
#investigadores()

def suspeitos():
    investigadores = cursor.execute("""SELECT * FROM suspeitos""")
    investigadores = cursor.fetchall()

    pprint(investigadores)

    return investigadores


# suspeitos()

def vitimas():
    investigadores = cursor.execute("""SELECT * FROM vitimas""")
    investigadores = cursor.fetchall()

    pprint(vitimas)

    return investigadores


#vitimas()

def evidencias():
    investigadores = cursor.execute("""SELECT * FROM evidencias""")
    investigadores = cursor.fetchall()

    pprint(investigadores)

    return investigadores


# evidencias()

def testemunhas():
    investigadores = cursor.execute("""SELECT * FROM testemunhas""")
    investigadores = cursor.fetchall()

    pprint(investigadores)

    return investigadores


# testemunhas()

def pericias():
    investigadores = cursor.execute("""SELECT * FROM pericias""")
    investigadores = cursor.fetchall()

    pprint(investigadores)

    return investigadores


# pericias()

def casos_abertos():
    casos = cursor.execute("""SELECT * FROM casos WHERE status = 'Aberto'""")
    resultado = casos.fetchall()

    pprint(resultado)

    return resultado



#casos_abertos()

def agentes_pelo_cargo():
    agentes = cursor.execute("""SELECT * FROM investigadores WHERE cargo = 'Agente de Campo'""")
    resultado = agentes.fetchall()

    pprint(resultado)

    return resultado

#agentes_pelo_cargo()

def pericias_realizadas_pelo_fabio():
    fabio = cursor.execute("""SELECT * FROM pericias WHERE perito_responsavel LIKE '%Fábio%'""")
    resultado = fabio.fetchall()

    pprint(resultado)

    return resultado
#pericias_realizadas_pelo_fabio()

def suspeitos_caso1():
    suspeitos = cursor.execute("""SELECT * FROM suspeitos WHERE caso_id = 1""")
    resultado = suspeitos.fetchall()

    pprint(resultado)

    return resultado

#suspeitos_caso1()

def relatorio_casos_e_investigadores():
    relatorio = cursor.execute("""
           SELECT casos.id, casos.titulo, investigadores.nome, investigadores.cargo
           FROM casos 
           INNER JOIN investigadores ON casos.investigador_id = investigadores.id
       """)
    resultado = relatorio.fetchall()

    pprint(resultado)

    return resultado
#relatorio_casos_e_investigadores()

def ultilizando_input():
    print("qual tabela deseja ver?")
    print("1-investigadores")
    print("2-suspeitos")
    print("3-casos")
    print("4-vitimas")
    print("5-evidencias")
    print("6-testemunhas")
    print("7-pericias")

    resposta = int(input())

    if resposta == 1:
        investigadores()
    elif resposta == 2:
        suspeitos()
    elif resposta == 3:
        casos()
    elif resposta == 4:
        vitimas()
    elif resposta == 5:
        evidencias()
    elif resposta == 6:
        testemunhas()
    elif resposta == 7:
        pericias()

#ultilizando_input()

def relatorio_suspeitos_e_casos():
    ambos = cursor.execute("""
        SELECT suspeitos.nome, suspeitos.data_nascimento, casos.titulo 
        FROM suspeitos
        INNER JOIN casos ON suspeitos.caso_id = casos.id
    """)
    resultado = ambos.fetchall()

    pprint(resultado)

    return resultado
#relatorio_suspeitos_e_casos()


def input_casos_e_suspeitos():
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
        pprint(resultado)
    else:
        print(
            "Nenhum suspeito cadastrado para este caso ou o ID digitado é inválido."
        )



input_casos_e_suspeitos()








