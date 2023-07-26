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
        usr_aprob = busqueda(usuarios, LIM_USERS_RAW, LIM_USERS_COL,usr, 'codi') #comprobando existenci de usuario
        
        contr_input = getpass.getpass("Ingrese su contraseña: ")
        contr_aprob = busqueda(usuarios , LIM_USERS_RAW, LIM_USERS_COL, contr_input, 'condi') #comprobando existencia de contrasenia
        num_fila = busqueda(usuarios , LIM_USERS_RAW, LIM_USERS_COL, contr_input, 'fila')
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
            modificar ()
            return True
        case "c":
            borrar()
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
    
    pregunta = "desea ver los locales?"
    aux = ask_continue(pregunta)
    if aux == 's':
        ver_locales()
    
    if max_locales != 50:
        while nombreLocal != "*":
            column = 1
            nombreLocal = ingreso_nombre()
            if nombreLocal != '*':
                fila = max_locales + 1
                column += 1
                ingreso_ubi(column, fila)
                column += 1
                ingreso_rubro (column, fila)
                column += 1
                ingreso_codigos(column, fila)
                column += 1
                asignar_codigo_active (fila,column)
                max_locales += 1
                ordenar()
    else:
        os.system("cls")
        print ("maxima cantidad de locales alcanzada\n")
    
    os.system("cls")
    
    contador_rubro()
    return

def ingreso_nombre ():
    cont = 0
    nombreLocal = " "
    while cont != 1 and nombreLocal != "*":
                                                            #ingreso del nombre del local
        print("---- ingresando un ' * ' se termina el ingreso de locales ----\n")
        nombreLocal = (input("Ingrese el nombre del local: ")).capitalize()
        
        if len(nombreLocal) > 2:   
            special = char_allow(nombreLocal)
        
            if special != True:       
                    aprob = busqueda(locales, LIM_LOCALS_ROW, LIM_LOCALS_COL, nombreLocal, 'condi') #busqueda fila vacia en donde escribir el nombre
                    fila = busqueda(locales, LIM_LOCALS_ROW, LIM_LOCALS_COL, nombreLocal, 'fila')
                    if aprob != True:
                        locales[1][fila] = nombreLocal
                        cont+= 1#guardando el nombre
                    else:
                        repetido("el nombre")
            else:
                os.system("cls")
                print("Caracter no permitido\n")
        elif nombreLocal != '*':
            os.system("cls")
            print ("---- minimo de caracteres permitidos: 3 ----")
    
    return nombreLocal


def ingreso_ubi (column, fila):
    cont = 0
    os.system("cls")
    while cont != 1:             
        ubicacionLocal = (input("Ingrese la ubicacion: ")).capitalize()                     #ingreso de ubicacion
        
        if len(ubicacionLocal) > 3: 
            special = char_allow(ubicacionLocal)              
                              
            if special != True:
                locales[column][fila] = ubicacionLocal                                   #guardando ubicacion
                cont += 1
            else:
                os.system("cls")
                print("Caracter no permitido\n")
        else:
            os.system("cls")
            print("---- minimo de caracteres permitidos: 4 ---- ")



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
        
        if  locales[3][fila] == tipo_local[type] and locales[5][fila] == "A":
            cont += 1
            
            
        fila += 1
    return cont

def max_min_arrays(dato, tipo):                     #funcion encargada de  ordenar el array que contiene los contadores de mayor a menor (necesita ser usada dos veces consecutivas)
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
        cod_owner = input("ingrese el codigo: ")
        aprob = verif_num(cod_owner)                 #verificando si en el numero es numero para cuando se intente pasar de str a int no de error (logramos descartar el try que teniamos antes)                                                 
        if aprob != False:
            cod_owner = int(cod_owner)
            aux = busqueda(usuarios, LIM_USERS_RAW, LIM_USERS_COL, cod_owner, 'condicional')
            x = busqueda(usuarios, LIM_USERS_RAW, LIM_USERS_COL, cod_owner, 'fila') #verificando que el codigo de usuario que se ingreso existe    
            if aux == True and usuarios[3][x] == tipos_user[1]:    # si existe y es un codigo de dueno se guarda
                locales[column][fila] = cod_owner
                cont += 1
            else:
                os.system("cls")
                print("Codigo Invalido!!!!")
        else:
            os.system("cls")
            print("Codigo Invalido!!!!")


def asignar_codigo_active(fila,column):
    locales[0][fila] = fila
    
    locales[column][fila] = "A"          #y se le asigna una 'A' para su estado de activo 
    os.system("cls")

def modificar ():
    if max_locales > 0:
        modificar = ""
        os.system("cls")
        pregunta = "desea ver los locales?"
        aux = ask_continue(pregunta)
        if aux == 's':
            ver_locales()
        cont = 0
        while modificar != "*" and cont != 1:
            
            print("---- ingrese '*' para salir ----\n")
    
            modificar = input("ingrese el codigo del local a modificar: ")
            if modificar != '*':
                aprob = verif_num(modificar)
                if aprob != False:
                    modificar = int(modificar)
                    condi = busqueda(locales, LIM_LOCALS_ROW, 0, modificar, 'condi')
                    fila = busqueda(locales, max_locales, 0, modificar, 'fila')
                    if locales[5][fila] != "A":
                        pregunta = "----El local que ingreso se encuentra dado de baja (B) ----\n\nDesea activarlo?"
                        ask = ask_continue(pregunta)
                        if ask != "n":
                            locales[5][fila] = "A"
                    
                    if condi != False and locales[5][fila] != "B":
                        choice_modifi(fila,modificar)
                        ordenar()
                        cont += 1
                        os.system("cls")
                        print("---- Local Modificado ----\n")
                    elif condi != True: 
                        os.system("cls")
                        print("codigo invalido!!!\n")
                    else:
                        os.system("cls")
                        print("--- Para modificar un local debe estar Activo (A) ---\n")
                else:
                    os.system("cls")
                    print("codigo invalido!!!\n")
            else:
                os.system("cls")
    else:
        os.system("cls")
        print ("---- No se ha ingresado ningun local al sistema ----")
        msvcrt.getch()
        os.system("cls")
    return

def choice_modifi(fila,modificar):
    condicional = True
    while condicional == True:
        os.system("cls")
        print (f"---- Elija Atributo a Modificar del local {modificar}----\n")
        print ("1) nombre")
        print ("2) ubicacion")
        print ("3) rubro")
        print ("4) codigo dueño")
        print ("0) salir")
        opcion = input("ingrese un numero: ")

        if opcion < '0' and opcion > "4":
            opcion_erronea()
        else:
            os.system("cls")
            condicional = elecciones_modifi(opcion, fila,modificar)
    return

def elecciones_modifi(opcion,fila, modificar):
    match opcion:
        case '1':
            modifi_name (1 ,fila, modificar)
            return True
        case '2':
            ingreso_ubi(2, fila) 
            return True
        case '3':
            ingreso_rubro(3,fila)
            return True
        case '4':
            ingreso_codigos (4,fila)
            return True
        case '0':
            return False

def modifi_name (column, fila,x):
    cont = 0
    while cont != 1 :
        nombreLocal = (input("Ingrese el nombre del local: ")).capitalize()
        
        if len(nombreLocal) > 2:   
            special = char_allow(nombreLocal)
        
            if special != True:       
                    aprob = busqueda(locales, LIM_LOCALS_ROW, LIM_LOCALS_COL, nombreLocal, 'condi') #busqueda fila vacia en donde escribir el nombre
                    if aprob != True :
                        locales[column][fila] = nombreLocal
                        cont+= 1                        #guardando el nombre
                    else:
                        repetido("el nombre")
            else:
                os.system("cls")
                print("Caracter no permitido\n")
        else:
            print ("---- minimo de caracteres permitidos: 3 ----")
  

def borrar():
    borrar = ""
    os.system("cls")
   
    if max_locales > 0:
        pregunta = "desea ver los locales?"
        aux = ask_continue(pregunta)
        if aux == 's':
            ver_locales()
        cont = 0  
        while borrar != "*" and cont != 1:
            
            print("---- ingrese '*' para salir ----\n")
    
            borrar = input("ingrese el codigo del local a borrar: ")
            if borrar != '*':
                aprob = verif_num(borrar)
                if aprob != False:
                    borrar = int(borrar)
                    condi = busqueda(locales, LIM_LOCALS_ROW, 0, borrar, 'condi')
                    fila = busqueda(locales, max_locales, 0, borrar, 'fila')
                    if condi != False:
                        locales[5][fila] = "B"
                        cont += 1
                        os.system("cls")
                        print("---- Local borrado ----\n")
                    else: 
                        os.system("cls")
                        print("codigo invalido!!!\n")
                else:
                    os.system("cls")
                    print("codigo invalido!!!\n")
            else:
                os.system("cls")
    else:
        os.system("cls")
        print ("---- No se ha ingresado ningun local al sistema ----")
        msvcrt.getch()
        os.system("cls")
    return

def mapa_locales ():
    

def ask_continue(pregunta):
    aux2 = True
    while aux2 == True:
        os.system("cls")
        aux1 = input(f"{pregunta} (s/n)\n")  # preguntando si desea crear otro local
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
        opcion = input("Escriba una opcion: ")
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
             
def busqueda(dato,limraw, limcolumn, dato_buscar, retorno): #busqueda secuencial bidimensional
    fila = 0
    condicional = False
    while condicional != True and fila <= limraw :
        column = 0
        while condicional != True and column <= limcolumn:
            if dato_buscar == dato[column][fila]:
                if retorno == 'fila':
                    return fila
                else:
                    return True
            elif dato[0][fila] == 0:
                if retorno == 'fila':
                    return fila
                else:
                    return False
            else:
                column += 1
        fila += 1
    
    print ("Memoria llena")
    return 

        
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
                    x = 25 - len(str(locales[j][i]))
                    spaces = " " * x
                    if j == 3:
                        print (locales[j][i].capitalize(),spaces, end="")
                    else:
                        print (locales[j][i],spaces, end="")
        print ("\n\n\nA = Local activo   B = Local dado de baja")
        msvcrt.getch() #esta funcion pausa el sistema hasta que el operador tipee cualquier letra
        os.system("cls")
    else:
        print ("-- no se ha ingresado ningun local al sistema ---\n")  #este aviso aparece cuando no se ha introdido ningun local
        print ("presione cualquier tecla para continuar\n")
        msvcrt.getch()
        os.system("cls")
        
def verif_num(str):
    special = True
    if len(str) > 1:
        for i in range(0,len(str)):
            verifi = str[i]
            if not(verifi >= "0" and verifi <= "9"):
                special = False
    else:
        if not(str >= "0" and str <= "9"):
            special = False
            
    return special

def char_allow (word):
    special = False
    for i in range(0,len(word)):
            verifi = word[i]                                                 #verificando si tienes caracteres validos
            verifi = verifi.upper()
            if i == 0:
                if verifi == " " or verifi == " " or verifi == "'" or verifi == "&":
                    special = True
            if ((verifi < "A" and verifi > "Z") or (verifi < "0" and verifi > "9")) and not(verifi != " " or verifi != "'" or verifi !="&" or verifi != "." ):
                    special = True
    return special


# programa principal
os.system("cls")
precarga()
validar_usuario(condicional)