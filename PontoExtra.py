# Questão 1
#def imprimir_quadrado(numero):
    #quadrado = numero ** 2
    #print("O quadrado de", numero, "é", quadrado)

#numero = float(input("Insira o número para calcular o quadrado dele: "))
#imprimir_quadrado(numero)

# Questão 2
#numero = float(input("Insira o número real aqui para ter a sua quinta parte: "))
#numero = numero / 5
#print(numero)

#questao 3
#def antsus(numero):
 #   ant = numero - 1
  #  sus = numero + 1
   # print("O antecessor é", ant, "e o sucessor é", sus)

#numero = float(input("Insira o número para saber o antecessor e o sucessor dele: "))
#antsus(numero)

#Questao 4
#base = float(input("valor base"))
#altura = float(input("valor altura"))
#area = base*altura/2
#print(" o triangulo com base",base , "e altura", altura , "tem como area : ", area)

#questao5
#def verifnum(numero):
 #   if numero < 0:
  #      print("É negativo")
   # elif numero > 0:
    #    print("É positivo")
    #else:
     #   print("É neutro")

#num = float(input("Insira um número para realizar a verificação: "))
#verifnum(num)


#questao7
#num= float(input("insert number"))
#if num % 5 == 0 :
#    print("is divisible by 5")
#else: 
#    print("is not divisible by 5")

#questao6
#num = float(input("insert number"))
#if num % 3 == 0 :
#     print(" é multiplo")
#else:
#     print("nao é multiplo ")


#questao 8 

# num1 = float(input("valor primeiro numero  :  "))
# num2 = float(input("valor segundo numero  :  "))
# if num1 % num2 == 0 :
#     print("é divisivel")
# else :
#     print(" nao é divisivel")
    
# Questão 9
# def calcular_peso_ideal():
#     altura = float(input("Digite sua altura em metros: "))
#     sexo = input("Digite seu sexo (masculino/feminino): ")

#     if sexo.lower() == "masculino":
#         peso_ideal = (72.7 * altura) - 58
#     elif sexo.lower() == "feminino":
#         peso_ideal = (62.1 * altura) - 44.7
#     else:
#         return "Sexo inválido. Por favor, informe 'masculino' ou 'feminino'."

#     return peso_ideal


# peso_ideal = calcular_peso_ideal()
# print("Seu peso ideal é:", peso_ideal)


##Questão 10 ############################################
# a = int(input("digite um valor"))
# b = int(input("digite um valor"))
# c = int(input("digite um valor"))


# if a<b and a<c and b<c:
#     print(a)
#     print(b)
#     print(c)

# elif a<b and a<c and c<b:
#      print(a)
#      print(c)
#      print(b)

# elif b<a and b<c and c<a:
#      print(b)
#      print(c)
#      print(a)

# elif b<a and b<c and a<c:
#      print(b)
#      print(a)
#      print(c)

# elif c<a and c<b and a<b:
#      print(c)
#      print(a)
#      print(b)

# elif c<a and c<b and b<a:
#      print(c)
#      print(b)
#      print(a)

# Questão 11 ########################################
# a = int(input("digite um valor"))
# b = int(input("digite um valor"))
# c = int(input("digite um valor"))


# if a<b and a<c and b<c:
#      print(c)
#      print(b)
#      print(a)

# elif a<b and a<c and c<b:
#      print(b)
#      print(c)
#      print(a)

# elif b<a and b<c and c<a:
#      print(a)
#      print(c)
#      print(b)

# elif b<a and b<c and a<c:
#      print(c)
#      print(a)
#      print(b)

# elif c<a and c<b and a<b:
#      print(b)
#      print(a)
#      print(c)

# elif c<a and c<b and b<a:
#       print(a)
#       print(b)
#       print(c)
# Questão 13 ###############################
# alturas = []


# for i in range(50):
#     altura = int(input("Digite uma idade: "))
#     alturas.append(altura)

# maior_altura = max(alturas)
# menor_altura = min(alturas)

# print("Maior altura:", maior_altura)
# print("Menor altura:", menor_altura)
# Questão 14 ###################################
# num_boi_mais_gordo = None
# peso_boi_mais_gordo = float('-inf')
# num_boi_mais_magro = None
# peso_boi_mais_magro = float('inf')

# for i in range(1, 91):
#     num_identificacao = int(input("Digite o número de identificação do boi: "))
#     peso = float(input("Digite o peso do boi: "))

#     if peso > peso_boi_mais_gordo:
#         num_boi_mais_gordo = num_identificacao
#         peso_boi_mais_gordo = peso

#     if peso < peso_boi_mais_magro:
#         num_boi_mais_magro = num_identificacao
#         peso_boi_mais_magro = peso

# print("Boi mais gordo - Número:", num_boi_mais_gordo, "Peso:", peso_boi_mais_gordo)
# print("Boi mais magro - Número:", num_boi_mais_magro, "Peso:", peso_boi_mais_magro)
# Questão 16 && 17 ##################################

# votos_candidatos = [0, 0, 0, 0]  # Inicializa a contagem dos votos para cada candidato
# votos_nulos = 0
# votos_brancos = 0
# total_votos = 0

# while True:
#     voto = int(input("Digite o código do voto (1 a 4 para candidatos, 5 para nulo, 6 para branco, 0 para encerrar): "))

#     if voto == 0:
#         break

#     if 1 <= voto <= 4:
#         votos_candidatos[voto - 1] += 1
#     elif voto == 5:
#         votos_nulos += 1
#     elif voto == 6:
#         votos_brancos += 1
#     else:
#         print("Código de voto inválido. Voto não será contabilizado.")

#     total_votos += 1

# print("--- Resultado da Eleição ---")

# # Calcula e imprime os votos e percentuais para cada candidato
# for i in range(4):
#     candidato = i + 1
#     votos = votos_candidatos[i]
#     percentual = (votos / total_votos) * 100
#     print("Candidato", candidato)
#     print("Total de votos:", votos)
#     print("Percentual sobre o total: {:.2f}%".format(percentual))
#     print()

# # Calcula e imprime os votos e percentuais para votos nulos
# percentual_nulos = (votos_nulos / total_votos) * 100
# print("Votos Nulos")
# print("Total de votos:", votos_nulos)
# print("Percentual sobre o total: {:.2f}%".format(percentual_nulos))
# print()

# # Calcula e imprime os votos e percentuais para votos em branco
# percentual_brancos = (votos_brancos / total_votos) * 100
# print("Votos em Branco")
# print("Total de votos:", votos_brancos)
# print("Percentual sobre o total: {:.2f}%".format(percentual_brancos))

#  Questão 18 ####################################
# notas = []

# for i in range(4):
#     nota = float(input("Digite a nota: "))
#     notas.append(nota)

# maior_nota = max(notas)
# menor_nota = min(notas)
# media = sum(notas) / len(notas)

# print("Média final:", media)
# print("Maior nota:", maior_nota)
# print("Menor nota:", menor_nota)



# Questão 20


#notas = []



#for i in range(4):
 #   nota = int(input(f"Digite a nota {i+1}: "))
  #  notas.append(nota)


#media = int((notas[0] + notas[1] + notas[2] + notas[3]) /4)

#if media>=7:
 #   print("APROVADO")
#else:
 #   print("Qual foi a sua nota da prova final?")
  #  final = int(input())
    
   # media2 = int((notas[0] + notas[1] + notas[2] + notas[3] + final) /4)


    #if media2>=5:
     #   print("APROVADO")
    #else:
      #  print("REPROVADO")


#Questão 21


# def imprimir_maiusculo(string):
#     maiusculo = string.upper()
#     print(maiusculo)


# entrada = input("Digite uma string: ")
# imprimir_maiusculo(entrada)





# Questão 22



#string = input("Digite uma frase: ")
#caractere = input("Digite um caractere: ")

#ocorrencias = string.count(caractere)
#print(f"O caractere '{caractere}' aparece {ocorrencias} vezes na frase.")







# Questão 23




#def somar(lista):
 #   soma = 0
  #  for sublistas in lista:
   #     for elemento in sublistas:
    #        soma += elemento
            #A cada vez que ele repete ele acumula o valor , percorre a lista , pega um elemento e acumula repetindo até que não tenha mais listas e elementos
    #return soma



#minha_lista = [[1, 2],[3],[4,5]]
#mostrar = somar(minha_lista)

#print(mostrar)









# Questão 24


#def cumsum(lista):
 #   soma_cumulativa = 0
  #  soma_cumulativa_lista = []
   # for elemento in lista:
    #    soma_cumulativa += elemento
     #   soma_cumulativa_lista.append(soma_cumulativa)
    #return soma_cumulativa_lista

#O primeiro valor continua 1 pois a cumlativa é iniciado com 0, o segundo valor é 2 + 1 e assim por diante

#numeros = [1, 2, 3, 4, 5]
#resultado = cumsum(numeros)
#print(resultado)


# Questão 25




#def middle(lista):
 #   if len(lista) <= 2:
  #      return []
   # else:
    #    return lista[1:-1]
    #O índice representa vai mostrar apartir do segundo número e o  -1 não vai mostrar o último


#numeros = [1, 2, 3, 4, 5]
#resultado = middle(numeros)
#print(resultado)







# Questão 26


#def is_sorted(lista):
 #   return all(lista[i] <= lista[i+1] for i in range(len(lista)-1))

#numeros = [1, 2, 3, 4, 5]
#numeros2 = [3,2,4,5,6,7]
#resultado = is_sorted(numeros)
#resultado2 = is_sorted(numeros2)

#print(resultado)
#print(resultado2)


#Questão 15


#Uma pesquisa sobre algumas características físicas da população de uma determinada região coletou os seguintes dados, 
#referentes a cada habitante, para serem analisados:
#• Sexo (masculino, feminino)
#• Cor dos olhos (azuis, verdes, castanhos)
#• Cor dos cabelos (louros, castanhos, pretos)
#• Idade

#Fazer um algoritmo que determine e escreva:
#a) A maior idade dos habitantes.
#b) A porcentagem de indivíduos do sexo feminino cuja idade entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros.
lista_pessoas = []

def add_caracteristicas(sexo, corOlhos, corCabelo, idade):
    lista_pessoas.append({"Sexo": sexo, "Cor dos olhos": corOlhos, "Cor dos cabelos": corCabelo, "Idade": idade})

add_caracteristicas("Masculino", "Castanhos", "Preto", "22")
add_caracteristicas("Masculino", "Verdes", "Loiro", "19")
add_caracteristicas("Masculino", "Verdes", "Loiro", "20")
add_caracteristicas("Masculino", "Castanhos", "Castanho", "37")
add_caracteristicas("Feminino", "Castanhos", "Verde", "18")
add_caracteristicas("Feminino", "Azuis", "Ruivo", "25")
add_caracteristicas("Feminino", "Verdes", "Loiro", "22")
add_caracteristicas("Feminino", "Castanhos", "Preto", "39")

for i in lista_pessoas:
    print(f"Sexo: {i['Sexo']} \nCor dos olhos: {i['Cor dos olhos']}\nCor dos cabelos: {i['Cor dos cabelos']}\nIdade: {i['Idade']}\n")


# Encontrar a maior idade
idades = [int(pessoa['Idade']) for pessoa in lista_pessoas]
maior_idade = max(idades)

# Calcular a porcentagem de indivíduos do sexo feminino com características específicas
total_mulheres = sum(1 for pessoa in lista_pessoas if pessoa['Sexo'] == 'Feminino')
mulheres_verdes_louras = sum(1 for pessoa in lista_pessoas if pessoa['Sexo'] == 'Feminino' and 18 <= int(pessoa['Idade']) <= 35 and pessoa['Cor dos olhos'] == 'Verdes' and pessoa['Cor dos cabelos'] == 'Loiro')
porcentagem = (mulheres_verdes_louras / total_mulheres) * 100


print(f"Maior idade: {maior_idade}")
print(f"Porcentagem de mulheres com olhos verdes, cabelos louros e idade entre 18 e 35 anos: {porcentagem}%")


# Questão 19
# 
# #Desenvolva um programa que armazene quatro notas em uma lista e que apresenta a média final. 
#Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", 
#caso contrário, armazenar a nota da prova final e recalcular a média. 
#Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem "REPROVADO"


lista_notas = []

nota1 = float(input('Digite a primeira nota: \n'))
lista_notas.append(nota1)
nota2 = float(input('Digite a segunda nota: \n'))
lista_notas.append(nota2)
nota3 = float(input('Digite a terceira nota: \n'))
lista_notas.append(nota3)
nota4 = float(input('Digite a quarta nota: \n'))
lista_notas.append(nota4)

mediaF = (nota1+nota2+nota3+nota4)/4
if mediaF >= 7:
    print(f"A média final foi: {round(mediaF, 1)}", "\nSituação: \nAPROVADO")
else:
    print(f"A média final foi: {round(mediaF, 1)}","\nSituação: \nREPROVADO" )

#Questão 28
# 
# lista_palavras = ['Pindamonhangaba', 'abagnahnomadniP', 'Celular', 'raluleC', 'Pc', 'Torneira']

def sao_inversos(palavra1, palavra2):
    return palavra1 == palavra2[::-1]

for i in range(0, len(lista_palavras), 2):
    print("Palavras", lista_palavras[i], ' e ', lista_palavras[i+1])
    print(sao_inversos(lista_palavras[i], lista_palavras[i+1]))


#Questão 12


soma_pares = 0
lista_pares = []

for i in range(0, 501, 2):
    soma_pares += i
    lista_pares.append(i)
print("Números pares: \n", lista_pares)
print("O somatório dos valores pares de 0 a 500 é:", soma_pares)

#Questão 31

import random

lista_numeros = [random.randint(0, 100) for _ in range(5)] 

print("Lista sem ordem: \n", lista_numeros)
lista_numeros.sort()
print("Lista ordenada: \n", lista_numeros)

#Questão 29

#Faça um programa que remova todos os números pares de uma lista de 0 até 10

def verificar_pares():
    lista_numeros = []
    for i in range(1, 11):
        if i%2 == 0:
            lista_numeros.append(i)
    return lista_numeros

print(verificar_pares())




