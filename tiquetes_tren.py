def pago(destino, precio):
    print ("El proceso de pago ha comenzado. Por favor digite los datos pedidos por el sistema") 
    while True:
        tarjeta=input("Por favor digite el numero de la tarjeta: ")
        verificacion=len(tarjeta)
        if verificacion == 16:
            print("Felicidades ! tarjeta validada correctamente")
            break
        else:
            print("Por favor ingrese un numero de tarjeta valida")
    nombres=input("Por favor ingrese su nombre y apellido: ")
    identificacion=int(input("Por favor ingrese su numero de identificacion: ")) 
    print("Su pago fue aceptado este es su tickete")
    print("----------------------------------------------------------------") 
    print(f"Destino-----------------------------------------------{destino}")
    print(f"Nombres y apellidos-----------------------------------{nombres}")
    print(f"Tarjeta de indentificacion----------------------------{identificacion}")
    print(f"Tarjeta a la cual se cobrò----------------------------{tarjeta}")
    print(f"Destino-----------------------------------------------{destino}")
    print("---------------------------------------------------------------") 
    print(f"Total cobrado-----------------------------------------{precio}")
while True: 
    print("Bienvenido al menu de compra de boletos del tren, por favor ingrese el numero correspondiente a su destino\n") 
    print("destinos:\n 1--Bogota \n 2--Cali \n 3--Popayan \n 4--Pasto \n 5--Medellin \n\n 0--salir") 
    numero_menu=int(input("")) 
    if numero_menu == 1: 
        destino="Bogota" 
        precio=1000
        print(f"Su destino elegido es {destino} y tiene un valor de {precio}")
        i=int(input("desea continuar?\n1--SI       2--NO\n"))
        if i==1:
            print("A continuacion sera llevado al sistema de pago")
            pago(destino, precio) 
        else:
            print("Volver al menu principal")
    elif numero_menu == 2: 
        destino="Cali" 
        precio=1000
        print(f"Su destino elegido es {destino} y tiene un valor de {precio}")
        i=int(input("Desea continuar?\n1--SI       2--NO\n"))
        if i==1:
            print(" A continuacion sera llevado al sistema de pago")
            pago(destino, precio) 
        else:
            print("Sera llevado al menu principal")
    elif numero_menu == 3: 
        destino="Popayan" 
        precio=1000
        print(f"Su destino elegido es {destino} y tiene un valor de {precio}")
        i=int(input("Desea continuar?\n1--SI       2--NO\n"))
        if i==1:
            print("A continuacion sera llevado al sistema de pago")
            pago(destino, precio) 
        else:
            print("Sera  llevado al menu principal")
    elif numero_menu == 4: 
        destino="Pasto"
        precio=1000 
        print(f"Su destino elegido es {destino} y tiene un valor de {precio}")
        i=int(input("desea continuar?\n1--SI       2--NO\n"))
        if i==1:
            print("A continuacion serà llevado al sistema de pago")
            pago(destino, precio) 
        else:
            print("Sera llevado al menu principal") 
    elif numero_menu == 5: 
        destino="Medellin"
        precio=1000 
        print(f"Su destino elegido es {destino} y tiene un valor de {precio}")
        i=int(input("desea continuar?\n1--SI       2--NO\n"))
        if i==1:
            print("acontinuacion serà llevado al sistema de pago")
            pago(destino, precio) 
        else:
            print("Sera llevado al menu principal")
    elif numero_menu == 0: 
        i=int(input("Desea continuar?\n1--SI       2--NO\n"))
        if i == 1:
            print("Hasta luego, vuelva pronto!") 
            break