def eje9():
    fecha = int(input("Ingrese la fecha en formato DDMMAAAA: "))
    anio = fecha % 10000
    mes = (fecha / 10000) % 100
    dia = fecha / 1000000

    print("Dia", dia)
    print("Mes", mes)
    print("Año", anio)
eje9()