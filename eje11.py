def eje11():

    autos = int(input("Autos vendidos: "))
    valor = [] * autos
    salario = 0

    for i in range(autos):
        valor[i] = int(input("valor del auto:"))
        salario = salario + valor[i]*0.05 + 200
        print("Salario: ", int(5500 + salario))
eje11()
