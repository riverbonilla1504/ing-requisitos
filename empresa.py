class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []
        self.clientes = []

    def agregar_empleado(self, nombre, edad, sueldo_bruto, categoria=None, subordinados=None):
        empleado = {'nombre': nombre, 'edad': edad, 'sueldo_bruto': sueldo_bruto}
        if categoria:
            empleado['categoria'] = categoria
        if subordinados:
            empleado['subordinados'] = subordinados
        self.empleados.append(empleado)

    def agregar_cliente(self, nombre, edad, telefono):
        cliente = {'nombre': nombre, 'edad': edad, 'telefono': telefono}
        self.clientes.append(cliente)

    def mostrar_empleados(self):
        for empleado in self.empleados:
            print(empleado)

    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente)


# Crear una empresa
mi_empresa = Empresa("Mi Empresa")

# Agregar empleados
mi_empresa.agregar_empleado("Juan", 30, 50000)
mi_empresa.agregar_empleado("Maria", 35, 60000, "Directivo", ["Pedro", "Laura"])
mi_empresa.agregar_empleado("Pedro", 25, 40000)
mi_empresa.agregar_empleado("Laura", 28, 45000)

# Agregar clientes
mi_empresa.agregar_cliente("Carlos", 45, "555-1234")
mi_empresa.agregar_cliente("Ana", 50, "555-5678")

# Mostrar empleados y clientes
print("Empleados:")
mi_empresa.mostrar_empleados()

print("\nClientes:")
mi_empresa.mostrar_clientes()
