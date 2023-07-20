# integrantes:
# Lugo santeliz Leonardo Daniel
# Zega Juan Cruz
# Goyenechea Álvaro
# Lopez Frias Facundo Manuel

import getpass
import os


# declaracion de variables
# local
nombreLocal = " "
ubicacionLocal = " "
rubroLocal = " " 

# registro 
INT = [0]
STRING = [""]

COD = INT * 100
USER = STRING * 100
CLAVE = STRING * 100
TIPO = STRING * 100

BASE = [COD, USER, CLAVE, TIPO]

#USER = "admin@shopping.com"  # usuario. tipo string
#CONTR = "12345"  # contraseña. tipo string

usr = ""  # variables para validacion de usuario
contr_input = ""  # variables para validacion de contraseña
i = 3  # variable tipo entero de la cantidad de intentos incorrectos
condicional = True  # variable tipo bool

# variables tipo entero. (contadores de Rubros)
cont_indu = 0
cont_per = 0
cont_comida = 0

# auxiliares usados en crear_locales ()
aux1 = "y"
aux2 = True
auxru = True

# variables para mostrar el tipo de indumentaria que es mayor o menor
mas_locales = " "
menos_locales = " "

# variables locales de choice
iguales = " "
diferente = " "
# a = 0
# b = 0
# c = 0

# variables locales de mostrar_max_min() para saber el orden en que colocar el mayor y menor
# int more_locals
# int min_locals

#tipos owners
type_1 = "administrador"
type_2 = "dueñoLocal"
type_3 = "cliente"


def validar_usuario(condicional):  # ingreso seguro de la contra asi como validacion
    global i
    while condicional == True:
        usr = input("Ingrese su nombre de usuario: ")
        usr_aprob= busqueda(usr)
        contr_input = getpass.getpass("Ingrese su contraseña: ")
        contr_aprob, num_fila = busqueda(contr_input)

        if usr_aprob != False and contr_aprob != False:
            os.system("cls")
            print("ha iniciado sesion satisfactoriamente")
            if BASE[3][num_fila] == type_1:                   #decidion del menu segun el tipo de usuario
                condicional = val_menu_admin(condicional)
            elif BASE[3][num_fila] == type_2:
                condicional = val_menu_owner(condicional)
            else:
                condicional = val_menu_client(condicional)
            
        elif i > 1:
            i = i - 1
            os.system("cls")
            print("Tiene", i, "cantidad de intentos restantes")
        else:
            os.system("cls")
            print("Máximo de intentos permitidos alcanzado")
            condicional = False


def menu_prin_client():  #menu para clientes
    print ("1. Registrarme")
    print ("2. Buscar descuentos en locales")
    print ("3. Solicitar descuento")
    print ("4. Ver novedades")
    print ("0. Salir")

def menu_prin_admin(): #menu para administrador
    print ("1. Gestión de locales")
    print ("2. Crear cuentas de dueños de locales")
    print ("3. Aprobar / Denegar solicitud de descuento")
    print ("4. Gestión de Novedades")
    print ("5. Reporte de utilización de descuentos")
    print ("0. Salir")
    
def menu_prin_owner(): # menu para dueños
    print ("1. Gestión de Descuentos")
    print ("2. Aceptar / Rechazar pedido de descuento")
    print ("3. Reporte de uso de descuentos")
    print ("0. Salir")


def val_menu_client(condicional): #validacion de opciones del menu para clientes
    while condicional == True:
        menu_prin_client()
        opcion = input("ingrese un numero: ")

        if (opcion != "0" and opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" ):
            opcion_erronea()
        else:
            os.system("cls")
            condicional = elecciones_client(opcion)

def elecciones_client(opcion):
      match opcion:
        case "1":
            en_contruccion()
            return True

        case "2":
            en_contruccion()
            return True

        case "3":
            en_contruccion()
            return True

        case "4":
            en_contruccion()
            return True

        case "0":
            print("saliendo del programa")
            return False


def val_menu_admin(condicional): #validacion de opciones del menu para administrador
    while condicional == True:
        menu_prin_admin()
        opcion = input("ingrese un numero: ")

        if (opcion != "0" and opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5"):
            opcion_erronea()
        else:
            os.system("cls")
            condicional = elecciones_admin(opcion)


def elecciones_admin(opcion):
      match opcion:
        case "1":
            menu_op1(condicional)
            return True

        case "2":
            en_contruccion()
            return True

        case "3":
            en_contruccion()
            return True

        case "4":
            val_opc_menu_4(condicional)
            return True
        case "5":
            en_contruccion
            return True
        case "0":
            print("saliendo del programa")
            return False


def val_menu_owner(condicional): #validacion de opciones del menu para duenos
    while condicional == True:
        menu_prin_owner()
        opcion = input("ingrese un numero: ")

        if (opcion != "0" and opcion != "1" and opcion != "2" and opcion != "3"):
            opcion_erronea()
        else:
            os.system("cls")
            condicional = elecciones_owner(opcion)

def elecciones_owner(opcion):
      match opcion:
        case "1":
            menu_gestion(condicional)
            return True

        case "2":
            en_contruccion()
            return True

        case "3":
            en_contruccion()
            return True

        case "0":
            print("saliendo del programa")
            return False

def gestion_descuentos ():
    print ("a) Crear descuento para mi local")
    print ("b) Modificar descuento de mi local")
    print ("c) Eliminar descuento de mi local")
    print ("d) Volver")

def menu_gestion (condicional):  # seleccion y validacion del submenu 1
    while condicional == True:
        gestion_descuentos()
        opcion = input("ecsriba una opcion: ")
        opcion = opcion.lower()
        if opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d":
            opcion_erronea()
        else:
            condicional = elecciones_op1(opcion)


def elecciones_op1(opcion):  # acciones del menu y validacion 1)
    match opcion:
        case "a":
            en_contruccion()
            return True
        case "b":
            en_contruccion()
            return True
        case "c":
            en_contruccion()
            return True
        case "d":
            return val_menu_owner(condicional) #por hacer


def menu_1():  #submenu_gestion_locales
    print("a) Crear locales")
    print("b) Modificar local")
    print("c) Eliminar local")
    print("d) Mapa de locales")
    print("e) Volver")


def menu_op1(condicional):  # seleccion y validacion del submenu 1
    while condicional == True:
        menu_1()
        opcion = input("ecsriba una opcion: ")
        opcion = opcion.lower()
        if opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d" and opcion != "e":
            opcion_erronea()
        else:
            condicional = elecciones_op1(opcion)


def elecciones_op1(opcion):  # acciones del menu y validacion 1)
    match opcion:
        case "a":
            os.system("cls")
            crear_locales()
            return True
        case "b":
            en_contruccion()
            return True
        case "c":
            en_contruccion()
            return True
        case "d":
            en_contruccion() #por hacer
        case "e":
            os.system("cls")
            return val_menu_admin(condicional)


def crear_locales():  # accion de crear
    nombreLocal = " "
    while nombreLocal != "*":
        print("---- ingresando un ' * ' se termina el ingreso de locales ----")
        nombreLocal = input("Ingrese el nombre del local: ")
        os.system("cls")
        if nombreLocal != "*":
            ubicacionLocal = input("Ingrese la ubicacion: ")

            suma_conts()
    choice_iquals(cont_indu, cont_per, cont_comida)
    return


def suma_conts():
    global cont_indu
    global cont_per
    global cont_comida
    auxru = True
    while auxru == True:
        rubroLocal = input("Escoja un rubro: indumentaria, perfumería o comida\n")
        rubroLocal = (rubroLocal.lower())  # en caso de tipear una mayuscula la transformamos a minuscula
        os.system("cls")
        match rubroLocal:
            case "indumentaria":
                cont_indu = cont_indu + 1
                auxru = False
            case "perfumeria":
                cont_per = cont_per + 1
                auxru = False
            case "comida":
                cont_comida = cont_comida + 1
                auxru = False
            case _:
                print("rubro ivalido")


def ask_continue():
    aux2 = True
    while aux2 == True:
        aux1 = input("desea crear otro local? (s/n)\n")  # preguntando si desea crear otro local
        aux1 = aux1.lower()
        if aux1 == "s" or aux1 == "n":  # validando respuesta
            aux2 = False
        else:
            print("letra incorrecta")
    os.system("cls")
    return aux1


def choice_iquals(a, b, c):
    global iguales, diferente
    if a == b and a != c:
        iguales = "indumentaria y perfumeria"
        diferente = "comida"
        max_min_2_iguales(a, c)
    elif a == c and a != b:
        iguales = "indumentaria y comida"
        diferente = "perfumeria"
        max_min_2_iguales(a, b)
    elif b == c and b != a:
        iguales = "perfumeria y comida"
        diferente = "indumentaria"
        max_min_2_iguales(b, a)
    elif a == b == c:
        print("todos los rubros tienen la misma cantidad de locales: ", a)
    else:
        choice_max_min_des()


def max_min_2_iguales(iquals, dife):
    if iquals > dife:
        print(f"{iguales} tienen la misma cantidad de locales: {iquals}")
        print(f"El rubro con menor cantidad de locales es {diferente} y cuenta con: {dife} locales")
    else:
        print(f"el rubro con mayor contidad de locales es: {diferente} y cuenta con: {dife} locales")
        print(f"{iguales} son iguales y cuentan con {iquals}")


def choice_max_min_des():  # decision de el rubro mayor o menor
    global mas_locales, menos_locales
    if cont_indu < cont_per:
        if cont_indu < cont_comida:
            menos_locales = ("indumemtaria")  # si se dan las dos primeras entonces cont_indu es menor
            if (
                cont_per > cont_comida
            ):  # y cont_per es mayor que cont_comida entonces cont_per es el mayor
                mas_locales = "Perfumeria"
                mostrar_max_min(cont_per, cont_indu)
            else:
                mas_locales = "comida"  # sino cont_comida es mayor
                mostrar_max_min(cont_comida, cont_indu)
        else:
            mas_locales = "Perfumeria"  # si no se dio la segunda entonces cont_per es el mayor y cont_comida es el menor
            menos_locales = "comida"
            mostrar_max_min(cont_per, cont_comida)
    elif (
        cont_indu > cont_comida
    ):  # si no se da la primera y cont_indu es tambien mayor a cont_comida entonces cont_indu es mayor
        mas_locales = "Indumentaria"
        if cont_per > cont_comida:
            menos_locales = "comida"  # si cont_per  es mayor que cont_comida  entones cont_comida es el menor
            mostrar_max_min(cont_indu, cont_comida)
        else:
            menos_locales = "Perfumeria"  # sino es cont_per es el menor
            mostrar_max_min(cont_indu, cont_per)
    else:
        mas_locales = "comida"  # si cont_indu es mayor que cont_per y cont_comida es mayor que cont_indu entonces cont_ comida es mayor y cont_per menor
        menos_locales = "perfumeria"
        mostrar_max_min(cont_comida, cont_per)


def mostrar_max_min(more_locals, min_locals):  # exhibiendo mayores y menores
    print(f"El rubro con la mayor cantidad de locales es: {mas_locales} y cuenta con {more_locals} locales")
    print(f"El rubro con la menor cantidad de locales es: {menos_locales} y cuenta con {min_locals} locales")


def menu_4():  #submenu_gestion_novedades
    print("a) Crear novedades")
    print("b) Modificar novedad")
    print("c) Eliminar novedad")
    print("d) Ver reporte de novedad")
    print("e) Volver")


def val_opc_menu_4(condicional):  # validadando opcion del submenu4
    while condicional == True:
        menu_4()
        opcion = input("ecsriba una opcion: ")
        opcion = opcion.lower()
        if (opcion != "a" and opcion != "b" and opcion != "c" and opcion != "d" and opcion != "e"):
            opcion_erronea()
        else:
            condicional = elecciones_op4(opcion)


def elecciones_op4(opcion):  # acciones del sub menu 4
    match opcion:
        case "a":
            en_contruccion()
            return True
        case "b":
            en_contruccion()
            return True
        case "c":
            en_contruccion()
            return True
        case "d":
            en_contruccion()
            return True
        case "e":
            os.system("cls")
            return False


def opcion_erronea():  # exhibiendo que la opcion tipeada fue erronea
    os.system("cls")
    print(" -por favor seleccione una de la opciones correctas-\n")


def en_contruccion():  # exhibiendo que la opcion seleccionada esta en construccion
    os.system("cls")
    print(" -En contruccion-\n")

def precarga():
    # Primer usuario

    COD[0] = 1
    USER[0] = "admin@shopping.com"
    CLAVE[0] =  "12345"
    TIPO [0] = type_1

    # Segundo usuario

    COD[1] = 4
    USER[1] = "localA@shopping.com"
    CLAVE[1]=  "AAAA1111"
    TIPO [1]= type_2

    # Tercer usuario

    COD[2] = 6
    USER[2] = "localB@shopping.com"
    CLAVE[2] =  "BBBB2222"
    TIPO [2] = type_2

    # Cuarto usuario

    COD[3] = 9
    USER[3] = "unCliente@shopping.com"
    CLAVE[3] =  "33xx33"
    TIPO [3] = type_3

            
def busqueda(dato): #busqueda secuencial bidimensional
    fila = 0
    condicional = False
    while condicional != True and fila <= 99:
        column = 0
        while condicional != True and column <= 3:
            if dato == BASE[column][fila]:
                condicional = True
            else:
                column += 1
        fila += 1
    return condicional, fila-1
        


# programa principal
os.system("cls")
precarga()
validar_usuario(condicional)
