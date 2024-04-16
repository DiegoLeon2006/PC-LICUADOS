#Diego León y Estuardo González 
import datetime

print("Bienvenido a la cafetería URL")
nombre_cliente = input("Ingrese el nombre del cliente: ")
print("Hola", nombre_cliente)
opcion_NIT = input(" ingresar NIT (s/n): ")
nit_cliente = ""
if opcion_NIT.lower() == "sí" or opcion_NIT.lower() == "si":
    nit_cliente = input("Ingrese el NIT del cliente: ")

precio_base = 20.00
cantidad_azucar = 0
precio_azucar = 0
cantidad_de_azucar = ""
precio_total = precio_base
tipo_leche = "Leche deslactosada"
descuento_leche = 0
agrandado = False
tipo_azucar = ""  

opcion = 0
while opcion != 6:
    print("\nMenú: Licuado de fresa con leche deslactosada Q20.00")
    print("1. Ver información del pedido")
    print("2. Agregar azúcar")
    print("3. Modificar leche")
    print("4. Agrandar")
    print("5. Confirmar")
    print("6. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("\nInformación del pedido:")
        print("Cliente:", nombre_cliente)
        print("NIT:", nit_cliente)
        print("Fecha y hora:", datetime.datetime.now())
        print("Producto: Licuado de fresa con", tipo_leche)
        print("Cantidad de azúcar:", cantidad_azucar, "cucharada de", tipo_azucar)
        print("Precio total: Q", precio_total)
    elif opcion == 2:
        if cantidad_azucar < 3:
            print("\nTipos de azúcar:")
            print("1. Agregar 1 de azucar (Q0.50 por una cucharada)")
            print("2. agregar 2 cucharadas (Q1.00 por dos cucharada)")
            print("3. No azucar (Q0.00 por cucharada)")
            tipo = int(input("Seleccione el tipo de azúcar: "))
            if tipo == 1:
                tipo_azucar = "1 cucharada"
                precio_azucar = 0.50
            elif tipo == 2:
                tipo_azucar = "2 cucharadas"
                precio_azucar = 1.00
            elif tipo == 3:
                tipo_azucar = "no azucar"
                precio_azucar = 0.00
            else:
                print("Opción inválida.")
                continue
            cantidad_azucar += 1
            precio_total += precio_azucar
            print("Se agregó", tipo_azucar, "al licuado. Precio adicional: Q", precio_azucar)
        else:
            print("No se puede agregar más azúcar, se alcanzó el límite de 2 cucharadas.")
    elif opcion == 3:
        print("\nTipos de leche:")
        print("1. Sin leche (descuento de Q2.00)")
        print("2. Leche deslactosada")
        print("3. Leche entera")
        print("4. Leche de soya (aumento de Q3.00)")
        tipo_leche_seleccionada = int(input("Seleccione el tipo de leche: "))
        if tipo_leche_seleccionada == 1:
            tipo_leche = "con agua"
            precio_total -= 2.00
        elif tipo_leche_seleccionada == 2:
            tipo_leche = "leche deslactosada"
        elif tipo_leche_seleccionada == 3:
            tipo_leche = "leche entera"
        elif tipo_leche_seleccionada == 4:
            tipo_leche = "leche de soya"
            precio_total += 3.00
        else:
            print("Opción inválida.")
            continue
        print("Se modificó la leche del licuado a:", tipo_leche)
    elif opcion == 4:
        if not agrandado:
            precio_total += precio_total * 0.05
            agrandado = True
            print("El licuado se ha agrandado. Precio adicional: 5%")
        else:
            print("El licuado ya fue agrandado anteriormente.")
    elif opcion == 5:
        print("\nConfirmación del pedido:")
        print("Cliente:", nombre_cliente)
        print("NIT:", nit_cliente)
        print("Fecha y hora de inicio:", datetime.datetime.now())
        print("Producto: Licuado de fresa con", tipo_leche)
        print("Cantidad de azúcar:", cantidad_azucar, "cucharaditas de", tipo_azucar)
        print("Precio total: Q", precio_total)
        print("Simulando la entrega del producto...")
        print("¡Gracias por su compra!")
        print("Fecha y hora de finalización:", datetime.datetime.now())
        break
    elif opcion == 6:
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida.")