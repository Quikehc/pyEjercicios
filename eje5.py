def eje5():
    horas = int(input("Ingrese el valor de las horas"))
    minutos = int(input("Ingrese el valor de los minutos"))
    segundos = int(input("Ingrese el valor de los segundos"))
    resultadoexpresadoensegundos = horas * 3600 + minutos * 60 + segundos
    print("El resultado expresado en segundos es: ", resultadoexpresadoensegundos)
eje5()