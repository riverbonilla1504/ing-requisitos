# realizar una clase en el cual se declaren dos valores enteros por teclado. calcular despues la suma, la resta, multiplicacion y division. utilizar un metodo para cada una e imprimir los resultados obtenidos. llamar a la clase calculadora
#hecho por river bonilla
#6/10/2023
class Calculadora:
    def __init__(self):
        # Método para inicializar los valores
        self.valor1 = int(input("Ingresa el primer valor entero: "))  # Solicita el primer valor por teclado
        self.valor2 = int(input("Ingresa el segundo valor entero: "))  # Solicita el segundo valor por teclado
    
    def suma(self):
        # Método para realizar la suma
        self.resultado_suma = self.valor1 + self.valor2  # Calcula la suma
        return self.resultado_suma  # Retorna el resultado de la suma

    def resta(self):
        # Método para realizar la resta
        self.resultado_resta = self.valor1 - self.valor2  # Calcula la resta
        return self.resultado_resta  # Retorna el resultado de la resta

    def multiplicacion(self):
        # Método para realizar la multiplicación
        self.resultado_multiplicacion = self.valor1 * self.valor2  # Calcula la multiplicación
        return self.resultado_multiplicacion  # Retorna el resultado de la multiplicación

    def division(self):
        # Método para realizar la división
        if self.valor2 != 0:  # Verifica que el segundo valor no sea cero para evitar la división por cero
            self.resultado_division = self.valor1 / self.valor2  # Calcula la división
            return self.resultado_division  # Retorna el resultado de la división
        else:
            return "la divison no pudo ser acabada ya que estas intentando dividir entre 0"  # Retorna un mensaje de error si se intenta dividir por cero

# Creamos una instancia de la clase "Calculadora"
mi_calculadora = Calculadora()

# Llamamos a los métodos e imprimimos los resultados
print(f"Suma: {mi_calculadora.suma()}")  # Imprime el resultado de la suma
print(f"Resta: {mi_calculadora.resta()}")  # Imprime el resultado de la resta
print(f"Multiplicación: {mi_calculadora.multiplicacion()}")  # Imprime el resultado de la multiplicación
print(f"División: {mi_calculadora.division()}")  # Imprime el resultado de la división
