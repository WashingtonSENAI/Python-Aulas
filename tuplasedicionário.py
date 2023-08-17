
# QUESTÃO 1

# d= {'nome': 'João', 'idade': '30', 'telefone': '123123123', endereço': 'Queimadinha'}
# print(d['nome'])

#QUESTÃO 2

# d= {'nome': 'João', 'idade': '30', 'telefone': '123123123', 'endereço': 'Queimadinha'}

# nome = input("Digite o seu nome: ")
# idade = input("Digite a sua idade: ")
# tel = input("Digite o seu telefone: ")
# ende = input("Digite o seu endereço: ")

# d['nome'] = nome
# d['idade'] = idade
# d['endereço'] = ende
# d['telefone'] = tel

# print(d)

# QUESTÃO 3

# agenda  = {}

# while True:
#     cpf = input("Digite o CPF (ou 'printar' para encerrar o programar e mostrar a agenda): ")
#     if cpf.lower() == "printar":
#         break

#     nome = input("Digite o nome: ")
#     idade = input("Digite a idade: ")
#     telefone = input("Digite o telefone: ")

#     agenda[cpf] = {'nome': nome, 'idade': idade, 'telefone': telefone}

# print("\nAgenda:")
# for cpf, contato in agenda.items():
#     print(f"{cpf}: {contato['nome']}-{contato['idade']}-{contato['telefone']}")

#QUESTAO 4
# d = {}
# dmenor = {}

# while True:
#     nome = input("Digite o nome (ou 'sair' para encerrar): ")
#     if nome.lower() == "sair":
#         break

#     idade = int(input("Digite a idade: "))
#     cpf = input("Digite o CPF: ")

#     d[cpf] = {'nome': nome, 'idade': idade, 'cpf': cpf}
#     if idade < 18:
#         dmenor[cpf] = d[cpf]

# print("\nDicionário de pessoas (com menores de 18 anos):")
# for cpf, pessoa in d.items():
#     if cpf not in dmenor:
#         print(f"CPF: {cpf} - Nome: {pessoa['nome']} - Idade: {pessoa['idade']}")
# for cpf, pessoa in dmenor.items():
#     print(f"CPF: {cpf} - Nome: {pessoa['nome']} - Idade: {pessoa['idade']}")
    

# print("\nDicionário de pessoas (sem menores de 18 anos):")
# for cpf, pessoa in d.items():
#     if cpf not in dmenor:
#         print(f"CPF: {cpf} - Nome: {pessoa['nome']} - Idade: {pessoa['idade']}")

#QUESTAO 5

# dados_principais = {}  
# dados_backup = []  

# while True:
#     nome = input("Digite o nome (ou 'sair' para encerrar): ")
#     if nome.lower() == "sair":
#         break

#     idade = int(input("Digite a idade: "))
#     cpf = input("Digite o CPF: ")

#     # Armazena os dados no dicionário principal
#     dados_principais[cpf] = {'nome': nome, 'idade': idade, 'cpf': cpf}

#     if len(dados_principais) == 5:
      
#         dados_backup.append(dados_principais)
#         dados_principais = {}


# print("\nBackups:")
# for i, backup in enumerate(dados_backup):
#     print(f"Backup {i+1}:")
#     for cpf, pessoa in backup.items():
#         print(f"CPF: {cpf} - Nome: {pessoa['nome']} - Idade: {pessoa['idade']}")


# print("\nDados restantes no dicionário principal:")
# for cpf, pessoa in dados_principais.items():
#     print(f"CPF: {cpf} - Nome: {pessoa['nome']} - Idade: {pessoa['idade']}")

#QUESTÃO 6

# def contar_vogais(texto):
#     vogais = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

#     for letra in texto.lower():
#         if letra in vogais:
#             vogais[letra] += 1

#     return vogais

# texto = input("Digite o texto: ")
# resultado = contar_vogais(texto)
# print(resultado)

#QUESTÃO 7

# def calcular_media_aluno(nome, notas):
#     if nome in notas:
#         quantidade_notas = len(notas[nome])
#         soma_notas = sum(notas[nome])
#         media = soma_notas / quantidade_notas
#         return media
#     else:
#         return None


# notas = {}

# while True:
#     nome = input("Digite o nome do aluno (ou deixe em branco para encerrar): ")
#     if nome == "":
#         break

#     nota1 = float(input("Digite a primeira nota: "))
#     nota2 = float(input("Digite a segunda nota: "))

#     notas[nome] = [nota1, nota2]

# nome_aluno = input("Digite o nome do aluno para calcular a média: ")
# media_aluno = calcular_media_aluno(nome_aluno, notas)

# if media_aluno is not None:
#     print(f"A média do aluno {nome_aluno} é: {media_aluno}")
# else:
#     print(f"Aluno {nome_aluno} não encontrado.")

#QUESTÃO 8

# def calcular_media_tempos(corredor):
#     total_voltas = len(corredor)
#     soma_tempos = sum(corredor)
#     media = soma_tempos / total_voltas
#     return media

# tempos = {}

# for i in range(6):
#     nome_corredor = input(f"Digite o nome do corredor {i+1}: ")
#     tempos_corredor = []
#     for volta in range(1, 11):
#         tempo = float(input(f"Digite o tempo (em segundos) da volta {volta}: "))
#         tempos_corredor.append(tempo)
#     tempos[nome_corredor] = tempos_corredor

# melhor_volta = float('inf')
# melhor_volta_corredor = None
# classificacao = []

# for nome, tempos_corredor in tempos.items():
#     media_tempos = calcular_media_tempos(tempos_corredor)

#     if media_tempos < melhor_volta:
#         melhor_volta = media_tempos
#         melhor_volta_corredor = nome

#     classificacao.append((nome, media_tempos))

# classificacao = sorted(classificacao, key=lambda x: x[1])

# print(f"\nMelhor volta da prova:")
# print(f"Corredor: {melhor_volta_corredor}")
# print(f"Volta: {tempos[melhor_volta_corredor].index(min(tempos[melhor_volta_corredor])) + 1}")

# print("\nClassificação final:")
# for posicao, (nome, media_tempos) in enumerate(classificacao):
#     print(f"{posicao + 1}º lugar: {nome} - Média de tempos: {media_tempos} segundos")