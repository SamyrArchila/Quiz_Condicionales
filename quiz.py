# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a = int(input("Ingrese el valor correspondiente al primer lado del triangulo"))
b = int(input("Ingrese el valor correspondiente al segundo lado del triangulo"))
c = int(input("Ingrese el valor correspondiente al tercer lado del triangulo"))


# processing
def es_triangulo(a, b, c):
    # Verifica si se cumplen las desigualdades triangulares
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    return False

# output

if es_triangulo(a, b, c):
        print("Los lados pueden formar un triángulo.")
else:
        print("Los lados no pueden formar un triángulo.")
