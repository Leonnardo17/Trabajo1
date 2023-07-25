# integrantes:
# Lugo santeliz Leonardo Daniel
# Zega Juan Cruz
# Goyenechea Álvaro
# Lopez Frias Facundo Manuel

import getpass
import os
import msvcrt


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
max_locales = 0

# auxiliares usados en crear_locales ()
# aux1 = "y"
aux2 = True

# variables locales de choice
# iguales = " "
# diferente = " "
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
        usr_aprob= busqueda(usuarios, LIM_USERS_RAW, LIM_USERS_COL,usr) #comprobando existenci de usuario
        contr_input = getpass.getpass("Ingrese su contraseña: ")
        contr_aprob, num_fila = busqueda(usuarios , LIM_USERS_RAW, LIM_USERS_COL, contr_input) #comprobando existencia de contrasenia

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

def elecciones_client(opcion):  #elecciones del cliente (por construir)
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


def elecciones_admin(opcion): #elecciones del menu de administrador
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

def elecciones_owner(opcion): #elecciones para el menu de duenos (por construir)
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

def gestion_descuentos (): #submenu de una sesion de duenos
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


def elecciones_op1(opcion):  # acciones del submenu de duenos
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
    global max_locales
    nombreLocal = " "
    
    aux = ask_continue()
    if aux == 's':
        ver_locales()
    
    if max_locales != 50:
        while nombreLocal != "*":
            special= False
            column = 1                                                                  #ingreso del nombre del local
            print("---- ingresando un ' * ' se termina el ingreso de locales ----\n")
            nombreLocal = (input("Ingrese el nombre del local: ")).capitalize()
            
    
            for i in range(0,len(nombreLocal)):
                verifi = nombreLocal[i]                                                 #verificando si tienes caracteres validos
                verifi = verifi.upper()
                if i == 0:
                    if verifi == " " or verifi == " " or verifi == "'" or verifi == "&":
                        special = True
                if ((verifi < "A" and verifi > "Z") or (verifi < "0" and verifi > "9")) and not(verifi != " " or verifi != "'" or verifi !="&" or verifi != "." ):
                    special = True
            

            if special != True:       
                aprob, fila = busqueda(locales, LIM_LOCALS_ROW, LIM_LOCALS_COL, nombreLocal) #busqueda fila vacia en donde escribir el nombre
                if aprob != True and nombreLocal != "*":
                    locales[column][fila] = nombreLocal                                      #guardando el nombre
                    column += 1
                    
                    while column < 3 :
                        
                        special = False
                        os.system("cls")
                        ubicacionLocal = (input("Ingrese la ubicacion: ")).capitalize()                     #ingreso de ubicacion
                        
                        for i in range(0,len(ubicacionLocal)):
                            verifi = ubicacionLocal[i]
                            verifi = verifi.upper()
                            if i == 0:
                                if verifi == " " or verifi == " " or verifi == "'" or verifi == "&":     #verificando si tiene caracteres especiales
                                    special = True
                            if ((verifi < "A" and verifi > "Z") or (verifi < "0" and verifi > "9")) and not(verifi != " " or verifi != "'" or verifi !="&" or verifi != "." ):
                                special = True
                                
                        if special != True:
                            aprob, x = busqueda(locales, max_locales, LIM_LOCALS_COL,nombreLocal)
                                                                                              #buqueda de fila vacia
                            if aprob == False:
                                locales[column][fila] = ubicacionLocal                                   #guardando ubicacion
                                column += 1
                            else:
                                os.system("cls")
                                repetido("La direcion")
                        else:
                            os.system("cls")
                            print("Caracter no permitido\n")
                            
                    ingreso_rubro (column, fila)                                                #ingreso del tipo de rubro
                    column += 1
                    aprob = ingreso_codigos(column, fila)                                       #ingreso de codigo del dueno y asignacion del codigo de local
                    max_locales += 1 
                    ordenar() #ordenando array de locales por orden alfabetico 
                else:
                    repetido("el nombre")
            else:
                os.system("cls")
                print("Caracter no permitido\n")
    else:
        os.system("cls")
        print ("maxima cantidad de locales alcanzada\n")
        
    os.system("cls")
    
    contador_rubro()  #eleccion de cantidad de rubros
    
    return


def ingreso_rubro(column, fila): #ingreso de rubro
    os.system("cls")
    aux = False
    while aux != True:
        rubroLocal = input("Escoja un rubro: indumentaria, perfumería o comida\n")
        rubroLocal = (rubroLocal.lower())  # en caso de tipear una mayuscula la transformamos a minuscula
        aux = busqueda_uni(tipo_local, 3, rubroLocal, aux) #verificando existencia del rubro
        os.system("cls")
        if aux != False:
            locales[column][fila] = rubroLocal
        else:
            
            print("rubro ivalido")
            
def contador_rubro ():
    global cont_comida, cont_per, cont_indu
    
    contador_max_min = [cont_indu, cont_per, cont_comida] #adiganando los contadores a un array
    for i in range(0,3):
        contador_max_min[i] = contador(i)
    
    contador_max_min, tipos = max_min_arrays(contador_max_min, tipo_local) #organizandolos de mayor a menor
    
    for i in range(0,3):
            print(f"Cantidad de locales de {tipos[i]}: {contador_max_min[i]}") #print de cantidad de locales al terminar carga de locales
    print("---------  ----------")
    
def contador (type): #contador utilizado para la cantidad de locales 
    fila = 1
    cont = 0
    while fila <= max_locales :
        
        if  locales[3][fila] == tipo_local[type]:
            cont += 1
            
            
        fila += 1
    return cont

def max_min_arrays(dato, tipo): #funcion encargada de  ordenar el array que contiene los contadores de mayor a menor (necesita ser usada dos veces consecutivas)
    for j in range(0,3):
        for i in range (0,2):
            if dato[i] < dato[i+1]:
            
                aux = dato[i]
                dato[i] = dato[i+1]
                dato[i+1]= aux
            
                aux = tipo[i]
                tipo[i] = tipo[i+1]
                tipo[i+1]= aux
        
            
    return dato, tipo

def ingreso_codigos (column, fila):   #ingreso de los codigos y el estado
    cont = 0
    
    while cont != 1:
        try:                                                                       #excepcion usada para evitar que el operador colo que una caracter de tipo char,                                          
            cod_owner = int(input("ingrese el codigo: "))                          #pues daria error al intentador lo hacer entero 
            aux , x = busqueda(usuarios, LIM_USERS_RAW, LIM_USERS_COL, cod_owner)  #considero necesaria aplicarla dado que es necesario hacer el input entero para poder compararlo con algun codigo exitente
            if aux == True and usuarios[3][x] == tipos_user[1]:
                locales[column][fila] = cod_owner
                cont += 1
            else:
                os.system("cls")
                print("Codigo Invalido!!!!")
        except:
            os.system("cls")
            print("Codigo Invalido!!!!")
        
    locales[0][fila] = max_locales + 1   #en este punto se termina los input y se determia el codigo de local
    column += 1             
    locales[column][fila] = "A"          #y se le asigna una 'A' para su estado de activo 
    os.system("cls")
    return False
              
def ask_continue():
    aux2 = True
    while aux2 == True:
        aux1 = input("desea ver los locales? (s/n)\n")  # preguntando si desea crear otro local
        aux1 = aux1.lower()
        if aux1 == "s" or aux1 == "n":  # validando respuesta
            aux2 = False
        else:
            print("letra incorrecta")
    os.system("cls")
    return aux1

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


def elecciones_op4(opcion):  # acciones del sub menu 4 del perfil de administrador
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

def precarga(): #precarga de los datos de las cuentas
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
               condicional = True
            else:
                column += 1
        fila += 1
    return condicional, fila-1
        
def busqueda_uni (buscar, lim,buscado, aux): #busqueda unidimensional
    for i in range(0, lim):
        if buscar [i] == buscado:
            aux = True
    return aux
            
# def busq_dico()


def ordenar():  #funcion encargada de ordenar el array locales
    if max_locales > 1:
        for i in range(1,max_locales):
                
                first_character_1 = locales [1][i]          #se obtine la primera letra de una posicion en la columna de los nombres del array locales y se guarda en una variable
                first_character_1 =  first_character_1[0]
                
                first_character_2 = locales [1][i+1]        #luego se hace lo mismo con la posicion siguiente
                first_character_2 = first_character_2[0]
        
                if first_character_1 > first_character_2:
                    for j in range(0,LIM_LOCALS_COL+1):     #si la primera es mayor (ASCII)  que la segunda se intercambian 
                        aux = locales[j][i]
                        locales[j][i] = locales[j][i+1]
                        locales[j][i+1] = aux
                        
                elif first_character_1 == first_character_2: #si son iguales se compara la segunda letra
                    second_character_1 = locales [1][i]
                    second_character_1 =  second_character_1[1]
                
                    second_character_2 = locales [1][i+1]
                    second_character_2 = second_character_2[1]
                    if second_character_1 > second_character_2:  #y si esta segunda letra es mayor en el primer nombre se intercambian
                        for j in range(0,LIM_LOCALS_COL+1):
                            aux = locales[j][i]
                            locales[j][i] = locales[j][i+1]
                            locales[j][i+1] = aux
    return
        
def ver_locales():  #print en pantalla de la tabla de locales 
    if max_locales != 0:
        print ("Presione culaquier tecla para continuar\n")
        for i in range(0,LIM_LOCALS_ROW):
            if locales[0][i] != 0:
                print("")
                for j in range(0,LIM_LOCALS_COL+1):
                    x = 20 - len(str(locales[j][i]))
                    spaces = " " * x
                    if j == 3:
                        print (locales[j][i].capitalize(),spaces, end="")
                    else:
                        print (locales[j][i],spaces, end="")
        msvcrt.getch() #esta funcion pausa el sistema hasta que el operador tipee cualquier letra
        os.system("cls")
    else:
        print ("-- no se ha ingresado ningun local al sistema ---\n")  #este aviso aparece cuando no se ha introdido ningun local
        print ("presione cualquier tecla para continuar\n")
        msvcrt.getch()
        os.system("cls")
        
# programa principal
os.system("cls")
precarga()
validar_usuario(condicional)