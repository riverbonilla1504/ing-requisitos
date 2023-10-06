# realizar una clase en el cual se declaren dos valores enteros por teclado. calcular despues la suma, la resta, multiplicacion y division. utilizar un metodo para cada una e imprimir los resultados obtenidos. llamar a la clase calculadora
#hecho por river bonilla
#6/10/2023
# Definimos una función para solicitar un valor entero por teclado
def obtener_valor():
    valor = int(input("Ingresa un valor entero: "))  # Solicita un valor entero por teclado
    return valor  # Retorna el valor ingresado
# Definimos una función para realizar la suma
def suma(valor1, valor2):
    resultado = valor1 + valor2  # Calcula la suma
    return resultado  # Retorna el resultado de la suma
# Definimos una función para realizar la resta
def resta(valor1, valor2):
    resultado = valor1 - valor2  # Calcula la resta
    return resultado  # Retorna el resultado de la resta
# Definimos una función para realizar la multiplicación
def multiplicacion(valor1, valor2):
    resultado = valor1 * valor2  # Calcula la multiplicación
    return resultado  # Retorna el resultado de la multiplicación
# Definimos una función para realizar la división
def division(valor1, valor2):
    resultado = valor1 / valor2  # Calcula la división
    return resultado  # Retorna el resultado de la división


# Llamamos a las funciones e imprimimos los resultados
valor1 = obtener_valor()  # Llamamos a la función para obtener el primer valor
valor2 = obtener_valor()  # Llamamos a la función para obtener el segundo valor

# Llamamos a las funciones de operaciones e imprimimos los resultados
print(f"Suma: {suma(valor1, valor2)}")  # Imprime el resultado de la suma
print(f"Resta: {resta(valor1, valor2)}")  # Imprime el resultado de la resta
print(f"Multiplicación: {multiplicacion(valor1, valor2)}")  # Imprime el resultado de la multiplicación
print(f"División: {division(valor1, valor2)}")  # Imprime el resultado de la división
