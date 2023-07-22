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

ENTERO = [0]
STRING = [""]

# Usuarios 
COD = ENTERO * 101
USER = STRING * 101
CLAVE = STRING * 101
TIPO = STRING * 101

usuarios = [COD, USER, CLAVE, TIPO]
LIM_USERS_RAW = 100
LIM_USERS_COL = 3

#Locales
COD_LOCAL = ENTERO * 51
NOMBRE_LOCAL = STRING * 51
UBICACION_LOCAL = STRING * 51
COD_USUARIO = ENTERO * 51
ESTADO = STRING * 51
RUBRO = STRING * 51

locales = [COD_LOCAL, NOMBRE_LOCAL, UBICACION_LOCAL, RUBRO, COD_USUARIO, ESTADO]
LIM_LOCALS_ROW = 50
LIM_LOCALS_COL = 5

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

#tipos de usuarios y locales
tipos_user = ["administrador", "dueñoLocal", "cliente"]
tipo_local = ["indumentaria", "perfumeria", "comida"]


def validar_usuario(condicional):  # ingreso seguro de la contra asi como validacion
    global i
    while condicional == True:
        usr = input("Ingrese su nombre de usuario: ")
        usr_aprob= busqueda(usuarios, LIM_USERS_RAW, LIM_USERS_COL,usr)
        contr_input = getpass.getpass("Ingrese su contraseña: ")
        contr_aprob, num_fila = busqueda(usuarios , LIM_USERS_RAW, LIM_USERS_COL, contr_input)

        if usr_aprob != False and contr_aprob != False:
            os.system("cls")
            print("ha iniciado sesion satisfactoriamente")
            if usuarios[3][num_fila] == tipos_user[0]:                   #decidion del menu segun el tipo de usuario
                condicional = val_menu_admin(condicional)
            elif usuarios[3][num_fila] == tipos_user[1]:
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
            return False #por hacer


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
            en_contruccion()
            return True #por hacer
        case "e":
            os.system("cls")
            return False


def crear_locales():  # accion de crear
    nombreLocal = " "
    
    while nombreLocal != "*":
        column = 1  
        print("---- ingresando un ' * ' se termina el ingreso de locales ----")
        nombreLocal = input("Ingrese el nombre del local: ")
        aprob, fila = busqueda(locales, LIM_LOCALS_ROW, LIM_LOCALS_COL, nombreLocal)
        if aprob != True and nombreLocal != "*":
            locales[column][fila] = nombreLocal
            aprob = True
            while aprob != False :
                os.system("cls")
                ubicacionLocal = input("Ingrese la ubicacion: ")
                aprob, x = busqueda(locales, LIM_LOCALS_ROW, LIM_LOCALS_COL,nombreLocal)
                if aprob != True:
                    column += 1
                    locales[column][fila] = ubicacionLocal
                    column += 1
                else:
                    os.system("cls")
                    repetido("La direcion")
                ingreso_rubro (column, fila)
                column += 1
                aprob = ingreso_codigos(column, fila)
        else:
            repetido("el nombre")
        os.system("cls")
    contador_rubro()
    
    return


def ingreso_rubro(column, fila):
    os.system("cls")
    aux = False
    while aux != True:
        rubroLocal = input("Escoja un rubro: indumentaria, perfumería o comida\n")
        rubroLocal = (rubroLocal.lower())  # en caso de tipear una mayuscula la transformamos a minuscula
        aux = busqueda_uni(tipo_local, 3, rubroLocal, aux)
        os.system("cls")
        if aux != False:
            locales[column][fila] = rubroLocal
        else:
            
            print("rubro ivalido")
            
def contador_rubro ():
    global cont_comida, cont_per, cont_indu
    cont_indu = contador(locales,0)
    cont_per= contador(locales, 1)
    cont_comida= contador(locales, 2)
    
    contador_max_min = [cont_indu, cont_per, cont_comida]
    
    contador_max_min = max_min_arrays(contador_max_min)
    
    if cont_indu != cont_per and cont_comida != cont_per and cont_comida != cont_indu:
        diferentes(contador_max_min)
    elif cont_indu == cont_comida and cont_per == cont_comida and cont_indu == cont_per:
        for i in range(0,3):
            print(f"Cantidad de locales de {tipo_local[i]}: {contador_max_min[i]}")
        print("-----  -----")
    else:
        choice_iquals()

def diferentes(contador_max_min):
    global cont_comida, cont_per, cont_indu
    tipos = [""] * 3
    for i in range(0,3):
            
        if contador_max_min[i] == cont_indu:
            tipos[i] = tipo_local[0]
        elif contador_max_min[i] == cont_per:
            tipos[i] = tipo_local[1]
        elif contador_max_min[i] == cont_comida:
            tipos[i] = tipo_local[2]
            
    for i in range(0,3):
        print(f"Cantidad de locales de {tipos[i]}: {contador_max_min[i]}")
    print("-----  -----")
    
def max_min_arrays(dato):
    for i in range (0,2):
        if dato[i] < dato[i+1]:
            aux = dato[i]
            dato[i] = dato[i+1]
            dato[i+1]= aux
    return dato

def ingreso_codigos (column, fila):
    cont = 0
    
    while cont != 1:
        try:
            cod_owner = int(input("ingrese el codigo: "))
            aux , x = busqueda(usuarios, LIM_USERS_RAW, LIM_USERS_COL, cod_owner)
            if aux == True:
                locales[column][fila] = cod_owner
                cont += 1
            else:
                os.system("cls")
                print("Codigo Invalido!!!!")
        except:
            os.system("cls")
            print("Codigo Invalido!!!!")
        
    locales[0][fila] = fila
    column += 1
    locales[column][fila] = "A"
    return False
              

# def suma_conts():
#     global cont_indu
#     global cont_per
#     global cont_comida
#     auxru = True
#     while auxru == True:
#         rubroLocal = input("Escoja un rubro: indumentaria, perfumería o comida\n")
#         rubroLocal = (rubroLocal.lower())  # en caso de tipear una mayuscula la transformamos a minuscula
#         os.system("cls")
#         match rubroLocal:
#             case "indumentaria":
#                 cont_indu = cont_indu + 1
#                 auxru = False
#             case "perfumeria":
#                 cont_per = cont_per + 1
#                 auxru = False
#             case "comida":
#                 cont_comida = cont_comida + 1
#                 auxru = False
#             case _:
#                 print("rubro ivalido")


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


def choice_iquals():
    global cont_indu, cont_per, cont_comida
    if cont_indu == cont_per and cont_indu != cont_comida:
        iguales = ["indumentaria", "perfumeria"]
        diferente = "comida"
        max_min_2_iguales(cont_indu, cont_comida, iguales, diferente)
    elif cont_indu == cont_comida and cont_indu != cont_per:
        iguales = ["indumentaria","comida"]
        diferente = "perfumeria"
        max_min_2_iguales(cont_indu, cont_per, iguales, diferente)
    elif cont_per == cont_comida and cont_per != cont_indu:
        iguales = ["perfumeria","comida"]
        diferente = "indumentaria"
        max_min_2_iguales(cont_per, cont_indu, iguales, diferente)


def max_min_2_iguales(iquals, dife, iguales, diferente):
    if iquals > dife:
        print(f"Cantidad de locales de {iguales[0]}: {iquals}")
        print(f"Cantidad de locales de {iguales[1]}: {iquals}")
        print(f"Cantidad de locales de {diferente}: {dife}")
        print("-----  -----")
    else:
        print(f"Cantidad de locales de {diferente}: {dife}")
        print(f"Cantidad de locales de {iguales[0]}: {iquals}")
        print(f"Cantidad de locales de {iguales[1]}: {iquals}\n")
        print("-----  -----")


# def choice_max_min_des():  # decision de el rubro mayor o menor
#     global mas_locales, menos_locales
#     if cont_indu < cont_per:
#         if cont_indu < cont_comida:
#             menos_locales = ("indumemtaria")  # si se dan las dos primeras entonces cont_indu es menor
#             if (cont_per > cont_comida):  # y cont_per es mayor que cont_comida entonces cont_per es el mayor
#                 mas_locales = "Perfumeria"
#                 mostrar_max_min(cont_per, cont_indu)
#             else:
#                 mas_locales = "comida"  # sino cont_comida es mayor
#                 mostrar_max_min(cont_comida, cont_indu)
#         else:
#             mas_locales = "Perfumeria"  # si no se dio la segunda entonces cont_per es el mayor y cont_comida es el menor
#             menos_locales = "comida"
#             mostrar_max_min(cont_per, cont_comida)
#     elif (cont_indu > cont_comida):  # si no se da la primera y cont_indu es tambien mayor a cont_comida entonces cont_indu es mayor
#         mas_locales = "Indumentaria"
#         if cont_per > cont_comida:
#             menos_locales = "comida"  # si cont_per  es mayor que cont_comida  entones cont_comida es el menor
#             mostrar_max_min(cont_indu, cont_comida)
#         else:
#             menos_locales = "Perfumeria"  # sino es cont_per es el menor
#             mostrar_max_min(cont_indu, cont_per)
#     else:
#         mas_locales = "comida"  # si cont_indu es mayor que cont_per y cont_comida es mayor que cont_indu entonces cont_ comida es mayor y cont_per menor
#         menos_locales = "perfumeria"
#         mostrar_max_min(cont_comida, cont_per)


# def mostrar_max_min(more_locals, min_locals):  # exhibiendo mayores y menores
#     print(f"El rubro con la mayor cantidad de locales es: {mas_locales} y cuenta con {more_locals} locales")
#     print(f"El rubro con la menor cantidad de locales es: {menos_locales} y cuenta con {min_locals} locales")


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
    
def repetido(x):
    os.system("cls")
    print (f" -{x} que intenta ingresar ya se encuentra guardado- \n")

def precarga():
    users = ["codigo","Usuario","Clave","Tipo", 1,"admin@shopping.com", "12345", tipos_user[0], 4,"localA@shopping.com", "AAAA1111", tipos_user[1], 6, "localB@shopping.com","BBBB2222", tipos_user[1], 9, "unCliente@shopping.com", "33xx33",tipos_user[2]]
    encabezado = ["Codigo del local", "nombre", "Ubicacion", "Rubro", "Codigo del usuario", "Estado"]
    cont = 0
    #precargando usuarios
    for i in range(0,5):
        for j in range(0,4):
            usuarios[j][i] = users[cont]
            cont += 1
            
    #precarga encabezado de locales
    for i in range (0,6):
        locales[i][0] = encabezado[i]
             
def busqueda(dato,limraw, limcolumn, dato_buscar): #busqueda secuencial bidimensional
    fila = 0
    condicional = False
    while condicional != True and fila <= limraw :
        column = 0
        while condicional != True and column <= limcolumn:
            if dato_buscar == dato[column][fila]:
                return True, fila
            
            elif dato[0][fila] == 0:
                return False, fila
            
            else:
                column += 1
        fila += 1
    return False, fila-1
        
def busqueda_uni (buscar, lim,buscado, aux):
    for i in range(0, lim):
        if buscar [i] == buscado:
            aux = True
    return aux
            
def contador (dato, type):
    fila = 0
    cont = 0
    condicional = False
    while condicional != True and fila <= LIM_LOCALS_ROW :
        
        if  dato[3][fila] == tipo_local[type]:
            cont += 1
            
            
        fila += 1
    return cont
    

# programa principal
os.system("cls")
precarga()
validar_usuario(condicional)