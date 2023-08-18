def crear_cuenta(): 
    cuenta=[]
    valor=0
    usuario = input("Ingrese su usuario: ") 
    contra = input("Ingrese la contraseña: ") 
    inicio_sesion = { 
    "usuario": usuario, 
    "contra": contra,
    "puntos": valor
    } 
    cuenta.append(inicio_sesion) 
    return cuenta 
def info_tarjeta(cuenta1): 
    marca= input("Ingrese la marca de la tarjeta: ") 
    numero_tarjeta=int(input("Ingrese el numero de su tarjeta: ")) 
    vencimiento=input("Ingrese su fecha de vencimiento con el siguiente formato mes/año: ") 
    codigo_verif=input("Ingrese el codigo de verificacion") 
    info_card= { 
        "marca": marca, 
        "numerotarjeta": numero_tarjeta, 
        "fecha de vencimiento": vencimiento, 
        "codigo de verificacion": codigo_verif 
    } 
    cuenta1.append(info_card) 
    return cuenta1 
def recibo(cuenta1, valor, aplicacion, puntos_acum):
    usuario=cuenta1[0]["usuario"]
    numero_tarjeta=cuenta1[1]["numerotarjeta"]
    print ("Este es su recibo, gracias por su compra")
    print("TIENDA APLICACIONES DE FANDROID")
    print("--------------------------------------")
    print(f"cobrado al usuario-----------{usuario}")
    print(f"tarjeta usada----------------{numero_tarjeta}")
    print(f"aplicacion comprada-----------{aplicacion}")
    print(f"puntos sumados a la cuenta-----{puntos_acum}")
    print("--------------------------------------")
    print(f"Valor total cobrado-------------{valor}")
    print("\n\n\nsera devuelto al menu de apliaciones")
    
print("Bienvenido a la tienda de aplicaciones online fandroid")
cuenta1=crear_cuenta() 
cuenta1=info_tarjeta(cuenta1)
while True: 
    print("Bienvenido al menu de aplicaciones de fandroid:\n 1--comprar apps \n 2--modificar tu informacion de inicio de sesion \n 3--modificar la informacion de tu tarjeta \n 4--consultar puntos \n5--consultar infomacion de cuenta \n\n 0--salir") 
    numero_menu=int(input("")) 
    if numero_menu==1:
        while True:
            print("Lista de aplicaciones")
            numero_menu=int(input("1--aplicacion1\n2--aplicacion2 \n3--aplicacion3\n4--aplicacion4\n5--aplicacion5\n6--aplicacion6\n0--volver"))
            if numero_menu==1:
                aplicacion="Telegram"
                valor=10000
                print(f"Esta a punto de comprar la aplicacion llamada {aplicacion}\n el valor de esta aplicacion es de {valor}\n desea continuar con la compra?\n1--SI      2--Volver al menu de aplicaciones")
                opcion_elegida=int(input(""))
                if opcion_elegida==1:
                    valor_prim=cuenta1[0]["puntos"] 
                    puntos_acum=valor/1000
                    valor_sum=valor_prim+puntos_acum
                    cuenta1[0]["puntos"]=valor_sum
                    recibo(cuenta1, valor, aplicacion, puntos_acum)
                elif opcion_elegida==2:
                    break
            elif numero_menu==2:
                aplicacion="Whatsapp"
                valor=10000
                print(f"Esta a punto de comprar la aplicacion llamada {aplicacion}\n el valor de esta aplicacion es de {valor}\n desea continuar con la compra?\n1--SI      2--Volver al menu de aplicaciones")
                opcion_elegida=int(input(""))
                if opcion_elegida==1:
                    valor_prim=cuenta1[0]["puntos"] 
                    puntos_acum=valor/1000
                    valor_sum=valor_prim+puntos_acum
                    cuenta1[0]["puntos"]=valor_sum
                    recibo(cuenta1, valor, aplicacion,puntos_acum)
                elif opcion_elegida==2:
                    break
            elif numero_menu==3:
                aplicacion="Messenger"
                valor=10000
                print(f"Esta a punto de comprar la aplicacion llamada {aplicacion}\n el valor de esta aplicacion es de {valor}\n desea continuar con la compra?\n1--SI      2--Volver al menu de aplicaciones")
                opcion_elegida=int(input(""))
                if opcion_elegida==1:
                    valor_prim=cuenta1[0]["puntos"] 
                    puntos_acum=valor/1000
                    valor_sum=valor_prim+puntos_acum
                    cuenta1[0]["puntos"]=valor_sum
                    recibo(cuenta1, valor, aplicacion, puntos_acum)
                elif opcion_elegida==2:
                    break
            elif numero_menu==4:
                aplicacion="Line"
                valor=10000
                print(f"Esta a punto de comprar la aplicacion llamada {aplicacion}\n el valor de esta aplicacion es de {valor}\n desea continuar con la compra?\n1--SI      2--Volver al menu de aplicaciones")
                opcion_elegida=int(input(""))
                if opcion_elegida==1:
                    valor_prim=cuenta1[0]["puntos"] 
                    puntos_acum=valor/1000
                    valor_sum=valor_prim+puntos_acum
                    cuenta1[0]["puntos"]=valor_sum
                    recibo(cuenta1, valor, aplicacion, puntos_acum)
                elif opcion_elegida==2:
                    break
            elif numero_menu==5:
                aplicacion="Discord"
                valor=10000
                print(f"Esta a punto de comprar la aplicacion llamada {aplicacion}\n el valor de esta aplicacion es de {valor}\n desea continuar con la compra?\n1--SI      2--Volver al menu de aplicaciones")
                opcion_elegida=int(input(""))
                if opcion_elegida==1:
                    valor_prim=cuenta1[0]["puntos"] 
                    puntos_acum=valor/1000
                    valor_sum=valor_prim+puntos_acum
                    cuenta1[0]["puntos"]=valor_sum
                    recibo(cuenta1, valor, aplicacion, puntos_acum)
                elif opcion_elegida==2:
                    break
            elif numero_menu==6:
                aplicacion="WeChat"
                valor=10000
                print(f"Esta a punto de comprar la aplicacion llamada {aplicacion}\n el valor de esta aplicacion es de {valor}\n desea continuar con la compra?\n1--SI      2--Volver al menu de aplicaciones")
                opcion_elegida=int(input(""))
                if opcion_elegida==1:
                    valor_prim=cuenta1[0]["puntos"] 
                    puntos_acum=valor/1000
                    valor_sum=valor_prim+puntos_acum
                    cuenta1[0]["puntos"]=valor_sum
                    recibo(cuenta1, valor, aplicacion, puntos_acum)
                elif opcion_elegida==2:
                    break
            elif numero_menu==0:
                break
    elif numero_menu==2: 
        print("Que deseas modificar? \n\n1--usuario\n2--contraseña\n3--usuario y contraseña")
        i=int(input(""))
        if i ==1:
            new_user=input("Por favor digite el nombre de usuario nuevo")
            cuenta1[0]["Usuario"]=new_user
            print("Su usuario se ha guardado correctamente, volviendo al menu principal")
        elif i==2:
            new_pass=input("Por favor digite la contraseña nueva nuevo")
            cuenta1[0]["contra"]=new_pass
            print("Su contraseña ha guardada correctamente, volviendo al menu principal")
        elif i==3:
            new_user=input("Por favor digite el nombre de usuario nuevo")
            new_pass=input("Por favor digite la contraseña nueva nuevo")
            cuenta1[0]["Usuario"]=new_user
            cuenta1[0]["Contra"]=new_pass
            print("Usuario y contraseña cambiados correctamente, volviendo al menu principal")
    elif numero_menu==3:
        new_tipo=input("Por favor digite la nueva marca de su tarjeta")
        new_card=input("Por favor digite el nuevo numero de tarjeta")
        new_expire=input("Por favor digite la nueva fecha de exp de la tarjeta")
        new_code=input("Por favor digite el nuevo codigo de seguridad de la tarjeta")
        cuenta1[1]["Marca"]=new_tipo
        cuenta1[1]["Numerotarjeta"]=new_card
        cuenta1[1]["Fecha de vencimiento"]=new_expire
        cuenta1[1]["Codigo de verificacion"]=new_code
        print("Datos cambiados correctamente")
    elif numero_menu==4: 
        consulta_puntos=cuenta1[0]["puntos"]
        print(f"Sus puntos actualmente son {consulta_puntos}")
        print("Usted sera redirigido al menu principal")
    elif numero_menu==5: 
        print(cuenta1)
    elif numero_menu==0:
        print("Vuelve pronto!!")
        break