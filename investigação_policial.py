import sqlite3

conexao = sqlite3.connect("sistema_policial.db")
cursor = conexao.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.executescript("""
    CREATE TABLE IF NOT EXISTS investigadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        matricula TEXT UNIQUE NOT NULL,
        cargo TEXT,
        telefone TEXT,
        email TEXT
    );

    CREATE TABLE IF NOT EXISTS casos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT,
        tipo_crime TEXT,
        data_abertura TEXT,
        status TEXT,
        investigador_id INTEGER,
        FOREIGN KEY (investigador_id) REFERENCES investigadores(id)
    );

    CREATE TABLE IF NOT EXISTS suspeitos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nascimento TEXT,
        cpf TEXT UNIQUE,
        endereco TEXT,
        caso_id INTEGER,
        FOREIGN KEY (caso_id) REFERENCES casos(id)
    );

    CREATE TABLE IF NOT EXISTS vitimas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data_nascimento TEXT,
        cpf TEXT UNIQUE,
        telefone TEXT,
        caso_id INTEGER,
        FOREIGN KEY (caso_id) REFERENCES casos(id)
    );

    CREATE TABLE IF NOT EXISTS evidencias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT,
        tipo TEXT,
        local_encontrada TEXT,
        data_coleta TEXT,
        caso_id INTEGER,
        FOREIGN KEY (caso_id) REFERENCES casos(id)
    );

    CREATE TABLE IF NOT EXISTS testemunhas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        endereco TEXT,
        depoimento TEXT,
        caso_id INTEGER,
        FOREIGN KEY (caso_id) REFERENCES casos(id)
    );

    CREATE TABLE IF NOT EXISTS pericias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        descricao TEXT,
        resultado TEXT,
        perito_responsavel TEXT,
        data_pericia TEXT,
        evidencia_id INTEGER,
        caso_id INTEGER,
        FOREIGN KEY (evidencia_id) REFERENCES evidencias(id),
        FOREIGN KEY (caso_id) REFERENCES casos(id)
    );
""")

dados_investigadores = [
    ("Carlos Mendes", "INSP-2024-88", "Investigador Chefe", "11977771111", "carlos.mendes@policia.gov"),
    ("Ana Rocha", "AG-2025-45", "Agente de Campo", "11977772222", "ana.rocha@policia.gov"),
    ("Roberto Lima", "INSP-2023-12", "Investigador Sênior", "11977773333", "roberto.lima@policia.gov"),
    ("Juliana Souza", "AG-2026-09", "Agente de Inteligência", "11977774444", "juliana.souza@policia.gov"),
    ("Marcos Oliveira", "INSP-2022-55", "Investigador de Homicídios", "11977775555", "marcos.oliveira@policia.gov"),
    ("Beatriz Santos", "AG-2024-31", "Perita de Campo", "11977776666", "beatriz.santos@policia.gov"),
    ("Fernando Alves", "INSP-2021-99", "Investigador de Fraudes", "11977777777", "fernando.alves@policia.gov"),
    ("Patrícia Cruz", "AG-2025-10", "Agente de Campo", "11977778888", "patricia.cruz@policia.gov"),
    ("Ricardo Fonseca", "INSP-2025-02", "Investigador Especial", "11977779999", "ricardo.fonseca@policia.gov"),
    ("Gabriela Melo", "AG-2026-88", "Agente Operacional", "11977770000", "gabriela.melo@policia.gov")
]

dados_casos = [
    ("Operação Sombra", "Furto de joias na joalheria central.", "Furto Qualificado", "2026-02-15", "Em investigação", 1),
    ("Caso Phishing", "Esquema de fraudes e estelionato online.", "Crime Cibernético", "2026-03-01", "Aberto", 2),
    ("Carga Desviada", "Roubo de carga de eletrônicos na rodovia.", "Roubo Majorado", "2026-03-10", "Em investigação", 3),
    ("Mansão Branca", "Homicídio do empresário na zona sul.", "Homicídio", "2026-04-02", "Em investigação", 5),
    ("Falsificação Real", "Esquema de clonagem de cartões e cédulas falsas.", "Estelionato", "2026-04-12", "Aberto", 7),
    ("Desaparecido", "Busca por jovem desaparecido após festa universitária.", "Desaparecimento", "2026-05-01", "Encerrado", 4),
    ("Invasão Digital", "Ataque cibernético ao sistema da prefeitura.", "Crime Virtual", "2026-05-18", "Aberto", 2),
    ("Golpe do Aluguel", "Casas fantasmas anunciadas na internet.", "Estelionato", "2026-06-02", "Em investigação", 7),
    ("Ouro Falso", "Comércio ilegal e adulteração de metais preciosos.", "Contrabando", "2026-06-15", "Aberto", 9),
    ("Silêncio da Noite", "Agressão corporal em estabelecimento comercial.", "Lesão Corporal", "2026-07-01", "Encerrado", 10)
]

dados_suspeitos = [
    ("Marcos Silva", "1992-05-14", "123.456.789-00", "Rua das Flores, 123", 1),
    ("Fabio de Souza", "1988-11-23", "987.654.321-11", "Av. Paulista, 1500", 2),
    ("Rodrigo 'Alemão'", "1985-08-02", "222.333.444-55", "Rua da Baixada, 40", 3),
    ("Lucas Antunes", "1995-12-01", "333.444.555-66", "Condomínio Alvorada, Ap 4", 4),
    ("Jeferson Lima", "1980-03-15", "444.555.666-77", "Rua do Porto, 88", 5),
    ("Matheus Guedes", "1999-07-22", "555.666.777-88", "Alamedas das Fontes, 12", 6),
    ("Alexandre Frota Jr", "1991-01-10", "666.777.888-99", "Av. Central, 900", 7),
    ("William Vieira", "1987-04-19", "777.888.999-00", "Rua sem Saída, 13", 8),
    ("César Augusto", "1975-09-09", "888.999.000-11", "Travessa da Paz, 5", 9),
    ("Bruno Henrique", "1993-10-31", "999.000.111-22", "Rua dos Esportes, 77", 10)
]

dados_vitimas = [
    ("Roberto Gold", "1970-01-30", "111.222.333-44", "11988889999", 1),
    ("Banco Digital S/A", None, "00.111.222/0001-33", "0800-123-456", 2),
    ("Transportadora Express", None, "11.222.333/0001-44", "1133334444", 3),
    ("Helena Albuquerque", "1978-06-12", "222.333.444-88", "11966667777", 4),
    ("Comércio Varejista Ltda", None, "22.333.444/0001-55", "1133445566", 5),
    ("Sonia Maria Ramos", "1965-02-20", "333.444.555-99", "11955556666", 6),
    ("Prefeitura Municipal", None, "33.444.555/0001-66", "1131112222", 7),
    ("Ricardo Alves", "1984-11-05", "444.555.666-00", "11944445555", 8),
    ("Joalheria Imperial", None, "44.555.666/0001-77", "1135556666", 9),
    ("Thiago Santos", "2001-08-14", "555.666.777-11", "11933334444", 10)
]

dados_evidencias = [
    ("Pé de cabra metálico com marcas", "Ferramenta", "Porta traseira da loja", "2026-02-16", 1),
    ("Notebook com logs de acesso", "Dispositivo Eletrônico", "Apto do suspeito Fabio", "2026-03-02", 2),
    ("Rastreador de satélite violado", "Dispositivo Eletrônico", "Acostamento Km 45", "2026-03-11", 3),
    ("Projétil de arma de fogo 9mm", "Munição", "Parede da sala principal", "2026-04-02", 4),
    ("Dispositivo skimmer (chupa-cabra)", "Equipamento Eletrônico", "Caixa eletrônico Agência 02", "2026-04-13", 5),
    ("Aparelho celular quebrado", "Dispositivo Eletrônico", "Terreno baldio próximo à festa", "2026-05-03", 6),
    ("HD Externo com códigos maliciosos", "Dispositivo Eletrônico", "Casa do suspeito Alexandre", "2026-05-20", 7),
    ("Contratos de locação falsificados", "Documento", "Escritório virtual alugado", "2026-06-03", 8),
    ("Lingotes de liga metálica amarelada", "Objeto Metálico", "Galpão industrial", "2026-06-16", 9),
    ("Imagens do circuito interno de TV", "Mídia Digital", "Estacionamento do bar", "2026-07-01", 10)
]

dados_testemunhas = [
    ("Maria Oliveira (Segurança)", "11955554444", "Rua Lateral, 45", "Viu um homem de casaco escuro correndo.", 1),
    ("André Justo (Vizinho)", "11955553333", "Av. Paulista, 1502", "Ouviu discussões na madrugada do crime.", 2),
    ("Carlos Caminhoneiro", "19944442222", "Posto de Gasolina Rodovia", "Viu dois carros cercando o caminhão.", 3),
    ("Doutor Américo (Médico)", "11933332222", "Condomínio Alvorada", "Ouviu estampidos parecidos com tiros.", 4),
    ("Juliana Caixa", "11922221111", "Rua do Comércio", "Notou um homem instalando algo no caixa.", 5),
    ("Lucas Universitário", "11911110000", "República dos Estudantes", "Viu o jovem saindo sozinho da festa.", 6),
    ("Vitor Técnico de TI", "11900009999", "Setor de TI Prefeitura", "Notou lentidão incomum e logs apagados.", 7),
    ("Sandra Corretora", "11988880000", "Imobiliária Central", "Denunciou o uso indevido de suas fotos de anúncios.", 8),
    ("Pedro Ourives", "11977770000", "Mercado Central", "Afirmou que tentaram vender ouro falso a ele.", 9),
    ("Marcela Garçonete", "11966660000", "Bar do Canto", "Viu o início da discussão na mesa dos fundos.", 10)
]

dados_pericias = [
    ("Papiloscópica", "Análise de digitais no pé de cabra.", "Digitais compatíveis com Marcos Silva.", "Dr. Ricardo Perito", "2026-02-18", 1, 1),
    ("Forense Digital", "Extração de dados do notebook.", "Encontrados arquivos com dados das contas fraudadas.", "Dr. Fábio TI", "2026-03-05", 2, 2),
    ("Eletrônica", "Análise física do rastreador violado.", "Circuito cortado propositalmente com alicate.", "Dr. Lima", "2026-03-14", 3, 3),
    ("Balística", "Exame do projétil 9mm encontrado.", "Disparado por uma pistola Taurus compatível.", "Dra. Samanta", "2026-04-05", 4, 4),
    ("Engenharia Reversa", "Análise do chupa-cabra apreendido.", "O circuito capturava trilhas magnéticas e enviava por bluetooth.", "Dr. Fábio TI", "2026-04-16", 5, 5),
    ("Forense Digital", "Recuperação de memória do celular.", "Mensagens indicam que a vítima iria pegar carona.", "Dra. Alice", "2026-05-06", 6, 6),
    ("Análise de Malware", "Varredura no HD externo.", "Encontrado o ransomware usado no ataque à prefeitura.", "Dr. Marcelo", "2026-05-24", 7, 7),
    ("Grafotécnica", "Análise das assinaturas nos contratos.", "Assinaturas falsificadas grosseiramente por decalque.", "Dra. Clarice", "2026-06-06", 8, 8),
    ("Metalúrgica", "Teste químico nos lingotes apreendidos.", "Composição aponta 95% de latão e apenas banho de ouro.", "Dr. Silveira", "2026-06-20", 9, 9),
    ("Audiovisual", "Melhoria de imagem do circuito interno.", "Identificado o veículo do agressor (Placa ABC-1234).", "Dra. Nicole", "2026-07-03", 10, 10)
]

cursor.executemany("INSERT INTO investigadores (nome, matricula, cargo, telefone, email) VALUES (?, ?, ?, ?, ?)", dados_investigadores)
cursor.executemany("INSERT INTO casos (titulo, descricao, tipo_crime, data_abertura, status, investigador_id) VALUES (?, ?, ?, ?, ?, ?)", dados_casos)
cursor.executemany("INSERT INTO suspeitos (nome, data_nascimento, cpf, endereco, caso_id) VALUES (?, ?, ?, ?, ?)", dados_suspeitos)
cursor.executemany("INSERT INTO vitimas (nome, data_nascimento, cpf, telefone, caso_id) VALUES (?, ?, ?, ?, ?)", dados_vitimas)
cursor.executemany("INSERT INTO evidencias (descricao, tipo, local_encontrada, data_coleta, caso_id) VALUES (?, ?, ?, ?, ?)", dados_evidencias)
cursor.executemany("INSERT INTO testemunhas (nome, telefone, endereco, depoimento, caso_id) VALUES (?, ?, ?, ?, ?)", dados_testemunhas)
cursor.executemany("INSERT INTO pericias (tipo, descricao, resultado, perito_responsavel, data_pericia, evidencia_id, caso_id) VALUES (?, ?, ?, ?, ?, ?, ?)", dados_pericias)

conexao.commit()