import sqlite3
from pprint import pprint

conexao = sqlite3.connect("sistema_policial.db")
cursor = conexao.cursor()

def tabela_casos():
    casos = cursor.execute("""SELECT * FROM casos""")
    casos = cursor.fetchall()

    pprint(casos)

    return casos

#tabela_casos()

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
relatorio_casos_e_investigadores()


