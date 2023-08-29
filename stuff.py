
#QUESTÃO 1


# class Bola:
#     def __init__(self, cor, circunferencia, material):
#         self.cor = cor
#         self.circunferencia = circunferencia
#         self.material = material
    
#     def trocaCor(self, nova_cor):
#         self.cor = nova_cor
    
#     def mostraCor(self):
#         return self.cor



# minha_bola = Bola("vermelho", 10, "plástico")


# print(minha_bola.mostraCor())  


# minha_bola.trocaCor("azul")

# print(minha_bola.mostraCor()) 




#QUESTÃO 2


# class Quadrado:
#     def __init__(self, lado):
#         self.lado = lado
    
#     def mudarLado(self, novo_lado):
#         self.lado = novo_lado
    
#     def retornarLado(self):
#         return self.lado
    
#     def calcularArea(self):
#         return self.lado ** 2 
    



# meu_quadrado = Quadrado(5)


# print(meu_quadrado.retornarLado())  


# meu_quadrado.mudarLado(7)


# print(meu_quadrado.retornarLado()) 


# area = meu_quadrado.calcularArea()
# print(area)  



#QUESTÃO 3

# class Retangulo:
#     def __init__(self, ladoA, ladoB):
#         self.ladoA = ladoA
#         self.ladoB = ladoB
    
#     def mudarLados(self, novo_ladoA, novo_ladoB):
#         self.ladoA = novo_ladoA
#         self.ladoB = novo_ladoB
    
#     def retornarLados(self):
#         return self.ladoA, self.ladoB
    
#     def calcularArea(self):
#         return self.ladoA * self.ladoB
    
#     def calcularPerimetro(self):
#         return 2 * (self.ladoA + self.ladoB)

# ladoA = float(input("Informe o valor do lado A: "))
# ladoB = float(input("Informe o valor do lado B: "))


# meu_retangulo = Retangulo(ladoA, ladoB)


# area = meu_retangulo.calcularArea()
# print("Área do retângulo:", area)

# perimetro = meu_retangulo.calcularPerimetro()
# print("Perímetro do retângulo:", perimetro)



#QUESTÃO 4

# class Pessoa:
#     def __init__(self, nome, idade, peso, altura):
#         self.nome = nome
#         self.idade = idade
#         self.peso = peso
#         self.altura = altura
    
#     def envelhecer(self, anos):
#         self.idade += anos
    
#     def engordar(self, quilos):
#         self.peso += quilos
    
#     def emagrecer(self, quilos):
#         self.peso -= quilos
    
#     def crescer(self, centimetros):
#         self.altura += centimetros



# pessoa = Pessoa("João", 25, 70, 170)


# print("Nome:", pessoa.nome)
# print("Idade:", pessoa.idade)
# print("Peso:", pessoa.peso)
# print("Altura:", pessoa.altura)


# pessoa.envelhecer(5)


# pessoa.engordar(3)


# pessoa.emagrecer(2)


# pessoa.crescer(10)


# print("Idade após envelhecer:", pessoa.idade)
# print("Peso após engordar/emagrecer:", pessoa.peso)
# print("Altura após crescer:", pessoa.altura)      



#QUESTÃO 5

# class ContaCorrente:
#     def __init__(self, numero_conta, nome_correntista, saldo=0):
#         self.numero_conta = numero_conta
#         self.nome_correntista = nome_correntista
#         self.saldo = saldo
    
#     def alterarNome(self, novo_nome):
#         self.nome_correntista = novo_nome
    
#     def deposito(self, valor):
#         self.saldo += valor
    
#     def saque(self, valor):
#         if self.saldo >= valor:
#             self.saldo -= valor
#         else:
#             print("Saldo insuficiente.")

# conta = ContaCorrente(123, "João")


# print("Número da conta:", conta.numero_conta)
# print("Nome do correntista:", conta.nome_correntista)
# print("Saldo:", conta.saldo)


# conta.alterarNome("João Silva")


# conta.deposito(500)


# conta.saque(200)


# print("Nome do correntista após alteração:", conta.nome_correntista)
# print("Saldo após depósito e saque:", conta.saldo)            



#QUESTÃO 6


# class TV:
#     def __init__(self):
#         self.canal = 1  # Canal inicial
#         self.volume = 50  # Nível de volume inicial
    
#     def alterarCanal(self, novo_canal):
#         if novo_canal >= 1 and novo_canal <= 100:
#             self.canal = novo_canal
#         else:
#             print("Canal inválido.")
    
#     def aumentarVolume(self):
#         if self.volume < 100:
#             self.volume += 1
#         else:
#             print("Volume máximo atingido.")
    
#     def diminuirVolume(self):
#         if self.volume > 0:
#             self.volume -= 1
#         else:
#             print("Volume mínimo atingido.")



# tv = TV()


# print("Canal:", tv.canal)
# print("Volume:", tv.volume)


# tv.alterarCanal(10)


# tv.aumentarVolume()
# tv.aumentarVolume()

# print("Canal após alteração:", tv.canal)
# print("Volume após aumento:", tv.volume)

# tv.diminuirVolume()
# tv.diminuirVolume()
# tv.diminuirVolume()


# print("Canal após alteração:", tv.canal)
# print("Volume após diminuição:", tv.volume)            


#QUESTÃO 7


# class BichinhoVirtual:
#     def __init__(self, nome):
#         self.nome = nome
#         self.fome = 0
#         self.saude = 100
#         self.idade = 0
    
#     def alterarNome(self, novo_nome):
#         self.nome = novo_nome
    
#     def alterarFome(self, nova_fome):
#         self.fome = nova_fome
    
#     def alterarSaude(self, nova_saude):
#         self.saude = nova_saude
    
#     def alterarIdade(self, nova_idade):
#         self.idade = nova_idade
    
#     def retornarNome(self):
#         return self.nome
    
#     def retornarFome(self):
#         return self.fome
    
#     def retornarSaude(self):
#         return self.saude
    
#     def retornarIdade(self):
#         return self.idade
    
#     def retornarHumor(self):
#         return self.fome + self.saude
    
#     def verificarEstado(self):
#         print("Nome:", self.nome)
#         print("Fome:", self.fome)
#         print("Saúde:", self.saude)
#         print("Idade:", self.idade)
#         print("Humor:", self.retornarHumor())




# bichinho = BichinhoVirtual("Meu Bichinho")

# bichinho.verificarEstado()


# bichinho.alterarNome("Bichinho Feliz")

# bichinho.alterarFome(50)


# bichinho.alterarSaude(75)


# bichinho.alterarIdade(2)


# print("Nome:", bichinho.retornarNome())


# print("Fome:", bichinho.retornarFome())


# print("Saúde:", bichinho.retornarSaude())


# print("Idade:", bichinho.retornarIdade())


# print("Humor:", bichinho.retornarHumor())


# bichinho.verificarEstado()       


#QUESTÃO 8


# class Macaco:
#     def __init__(self, nome):
#         self.nome = nome
#         self.bucho = []
    
#     def comer(self, alimento):
#         self.bucho.append(alimento)
    
#     def verBucho(self):
#         if len(self.bucho) == 0:
#             print("O bucho de", self.nome, "está vazio.")
#         else:
#             print("O bucho de", self.nome, "contém:")
#             for alimento in self.bucho:
#                 print("-", alimento)
    
#     def digerir(self):
#         if len(self.bucho) == 0:
#             print("O bucho de", self.nome, "já está vazio.")
#         else:
#             print("Digerindo o bucho de", self.nome)
#             self.bucho = []


# macaco1 = Macaco("Macaco 1")
# macaco2 = Macaco("Macaco 2")

# macaco1.comer("Banana")
# macaco1.comer("Maçã")
# macaco1.comer("Manga")

# macaco1.verBucho()


# macaco2.comer("Cenoura")
# macaco2.comer("Pêssego")

# macaco2.verBucho()


# macaco1.digerir()

# macaco1.verBucho()

# macaco2.digerir()


# macaco2.verBucho()

#QUESTÃO 9


# class Ponto:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def imprimir(self):
#         print("Ponto: ({}, {})".format(self.x, self.y))


# class Retangulo:
#     def __init__(self, ponto_inicial, largura, altura):
#         self.ponto_inicial = ponto_inicial
#         self.largura = largura
#         self.altura = altura
    
#     def encontrar_centro(self):
#         centro_x = self.ponto_inicial.x + self.largura / 2
#         centro_y = self.ponto_inicial.y + self.altura / 2
#         centro = Ponto(centro_x, centro_y)
#         return centro



# def exibir_centro(retangulo):
#     centro = retangulo.encontrar_centro()
#     print("Centro do retângulo:")
#     centro.imprimir()



# def alterar_retangulo(retangulo):
#     x = int(input("Digite o valor de x do ponto inicial: "))
#     y = int(input("Digite o valor de y do ponto inicial: "))
#     largura = int(input("Digite a largura do retângulo: "))
#     altura = int(input("Digite a altura do retângulo: "))
    
#     ponto_inicial = Ponto(x, y)
#     retangulo.ponto_inicial = ponto_inicial
#     retangulo.largura = largura
#     retangulo.altura = altura


# retangulo1 = Retangulo(Ponto(0, 0), 10, 5)
# retangulo2 = Retangulo(Ponto(2, 3), 7, 3)


# opcao = 0
# while opcao != 3:
#     print("\nMENU:")
#     print("1 - Alterar valores do retângulo")
#     print("2 - Exibir centro do retângulo")
#     print("3 - Sair")
    
#     opcao = int(input("Escolha uma opção: "))
    
#     if opcao == 1:
#         retangulo_escolhido = None
#         num_retangulo = int(input("Digite o número do retângulo (1 ou 2): "))
        
#         if num_retangulo == 1:
#             retangulo_escolhido = retangulo1
#         elif num_retangulo == 2:
#             retangulo_escolhido = retangulo2
        
#         if retangulo_escolhido is not None:
#             alterar_retangulo(retangulo_escolhido)
#         else:
#             print("Opção inválida!")
    
#     elif opcao == 2:
#         retangulo_escolhido = None
#         num_retangulo = int(input("Digite o número do retângulo (1 ou 2): "))
        
#         if num_retangulo == 1:
#             retangulo_escolhido = retangulo1
#         elif num_retangulo == 2:
#             retangulo_escolhido = retangulo2
        
#         if retangulo_escolhido is not None:
#             exibir_centro(retangulo_escolhido)
#         else:
#             print("Opção inválida!")

# print("Programa encerrado.")




#QUESTÃO 10

# class BombaCombustivel:
#     def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
#         self.tipoCombustivel = tipoCombustivel
#         self.valorLitro = valorLitro
#         self.quantidadeCombustivel = quantidadeCombustivel
    
#     def abastecerPorValor(self, valor):
#         litros_abastecidos = valor / self.valorLitro
#         if litros_abastecidos <= self.quantidadeCombustivel:
#             self.quantidadeCombustivel -= litros_abastecidos
#             print("Abastecimento realizado.")
#             print("Litros abastecidos:", litros_abastecidos)
#         else:
#             print("Não há combustível suficiente na bomba.")
    
#     def abastecerPorLitro(self, litros):
#         valor_pagar = litros * self.valorLitro
#         if litros <= self.quantidadeCombustivel:
#             self.quantidadeCombustivel -= litros
#             print("Abastecimento realizado.")
#             print("Valor a pagar:", valor_pagar)
#         else:
#             print("Não há combustível suficiente na bomba.")
    
#     def alterarValor(self, novo_valor):
#         self.valorLitro = novo_valor
    
#     def alterarCombustivel(self, novo_combustivel):
#         self.tipoCombustivel = novo_combustivel
    
#     def alterarQuantidadeCombustivel(self, nova_quantidade):
#         self.quantidadeCombustivel = nova_quantidade



# bomba = BombaCombustivel("Gasolina", 5.0, 1000)

# bomba.abastecerPorValor(50)  
# bomba.abastecerPorLitro(20) 
# bomba.alterarValor(5.5)  
# bomba.alterarCombustivel("Etanol")  
# bomba.alterarQuantidadeCombustivel(1500)  