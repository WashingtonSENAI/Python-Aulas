valor = 65.00

dolar = 3.25


print("$", valor/dolar , "Dolares\n")


celular = 299.99
chaleira = 23.87
gnomo = 66.66
adesivo = 1.42*6
frete = 12.34

total = frete+celular+chaleira+gnomo+adesivo
emdolar = total*3.25

IOF = emdolar*0.0638

print("Em  dolar : $ {:0.2f}".format(total), "\n")

print("Em real com o IOF R$ {:0.2f} :".format(emdolar+IOF), "\n")

print("Preço do IOF: {:0.2f}".format(IOF), "\n")