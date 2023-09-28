class Cliente:
    def __init__(self, dni, nombre, direccion, telefono, codigo):
        # Inicialización de un objeto Cliente con atributos
        self.dni = dni          # DNI del cliente
        self.nombre = nombre    # Nombre del cliente
        self.direccion = direccion  # Dirección del cliente
        self.telefono = telefono    # Teléfono del cliente
        self.codigo = codigo    # Código único del cliente
        self.aval = None        # Inicialmente, el cliente no tiene aval asignado

    def set_aval(self, aval):
        # Método para asignar un aval a un cliente
        self.aval = aval


class Reserva:
    def __init__(self, cliente, fecha_inicio, fecha_final, precio):
        # Inicialización de un objeto Reserva con atributos
        self.cliente = cliente              # Cliente que realiza la reserva
        self.fecha_inicio = fecha_inicio    # Fecha de inicio de la reserva
        self.fecha_final = fecha_final      # Fecha de finalización de la reserva
        self.precio = precio                # Precio de la reserva
        self.coches = []                    # Lista para almacenar los coches involucrados en la reserva

    def agregar_coche(self, coche):
        # Método para agregar un coche a la reserva
        self.coches.append(coche)

    def mostrar_reserva(self):
        # Método para imprimir la información de la reserva
        print(f"Cliente: {self.cliente.nombre}")
        print(f"DNI: {self.cliente.dni}")
        print(f"Fecha de inicio: {self.fecha_inicio}")
        print(f"Fecha de final: {self.fecha_final}")
        print(f"Precio: {self.precio}")
        print("Coches:")
        for coche in self.coches:
            print(f" - Modelo: {coche['modelo']}, Matrícula: {coche['matricula']}")


# Crear clientes temporales
cliente1 = Cliente("12345678A", "Juan Perez", "Calle A, Ciudad B", "555-1234", "C001")
cliente2 = Cliente("87654321B", "Maria Lopez", "Calle X, Ciudad Y", "555-5678", "C002")

# Establecer aval
cliente1.set_aval(cliente2)

# Crear una reserva temporal
reserva = Reserva(cliente1, "2023-09-22", "2023-09-25", 300)

# Agregar coches a la reserva
coche1 = {'modelo': 'Toyota', 'matricula': 'ABC123'}
coche2 = {'modelo': 'Ford', 'matricula': 'DEF456'}

reserva.agregar_coche(coche1)
reserva.agregar_coche(coche2)

# Mostrar información de la reserva
reserva.mostrar_reserva()
