



print("Você quer doar o seu sangue?(Y/N)")
saber = input()


if saber == "Y":



    print("Qual é a sua idade?")

    idade = int(input())


    print("Qual é o seu peso?")

    peso = float(input())


    print("Quantas horas você dormiu na ultima noite?")

    horas = int(input())


    if idade>=16 or 69<=idade and peso>=50 and horas>=6:
        print("Parabéns você pode doar o seu sange")
    else:
         print("Você não pode doar o seu sangue")
        

elif saber =="N":

    print("Fechando..")

