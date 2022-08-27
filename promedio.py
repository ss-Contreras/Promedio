ward = 0
suma = 0
notas = int(input("¿Cuantos notas desea ingresar?\n"))
lista = []
while notas > len(lista):
    num = float(input("Digite la nota: "))
    lista.append(num)
    if notas == len(lista):
        for n in lista:
            ward = ward + 1
            suma += n
            divtotal = 0
divtotal = suma / ward

print(f"El promedio de los {ward} numeros es de: {int(divtotal)}")




