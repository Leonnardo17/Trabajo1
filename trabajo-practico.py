# integrantes:
# Lugo santeliz Leonardo Daniel
# Zega Juan Cruz
# Goyenechea Álvaro
# Lopez Frias Facundo Manuel

import datetime
import getpass
import io
import pickle
import os
import msvcrt

# declaracion de variables
# local
nombreLocal = " "
rubroLocal = " " 

condicional = True  # variable tipo bool

# variables tipo entero. (contadores de Rubros)
cont_indu = 0
cont_per = 0
cont_comida = 0
max_locales = 0

#tipos de usuarios y locales
tipos_user = ["administrador", "dueñoLocal", "cliente"]
tipo_local = ["indumentaria", "perfumeria", "comida"]

class USUARIOS():
    
    def __init__(self):
        self.codUsuario = 0
        self.nombreUsuario = " "
        self.claveUsuario = " "
        self.tipoUsuario = " "

class LOCALES():
    def __init__(self):
        self.codLocal = 0 
        self.codUsuario = 0
        self.nombreLocal = " " 
        self.ubicacionLocal = " "
        self.rubroLocal = " "
        self.estado = " "
               
class PROMOCIONES():
    def __init__(self):
        self.codPromo = 0
        self.textoPromo = " "
        self.fechaDesdePromo = " "
        self.fechaHastaPromo = " "
        self.diasSemana = [0]*6
        self.estado = " "
        self.codLocal = 0

class USO_PROMOCIONES():
    def __init__(self):
        self.codCliente = 0
        self.codPromo = 0
        self.fechaUsoPromo = " "

def validar_inicio():
    opcion = "0"
    while opcion != "3":
        menu_inicio()
        opcion = input("ingrese un numero: ")

        if (opcion != "1" and opcion != "2" and opcion != "3"):
            opcion_erronea()
        elif (opcion != 3):
            os.system("cls")
            elecciones_inicio(opcion)

def menu_inicio():
    os.system("cls")
    print("1. Ingresar con usuario registrado")
    print("2. Registrarse como cliente")
    print("3. Salir")

def elecciones_inicio(opcion):
    match opcion:
        case "1":
            validar_usuario(True)
            return 
        case "2":
            crear_usuario("cliente")
            return

def lookForUser (x, attr):
    global afusuarios, urlusuarios
    condicional = False
    afusuarios.seek(0,0 )
    tam = os.path.getsize(urlusuarios)
    filelf = USUARIOS()
    attr_comparar = None
    tipo = None
    
    while afusuarios.tell() <tam:
        prueba = afusuarios.tell()
        filelf = pickle.load(afusuarios)

        
        if attr == "code":
            attr_comparar = filelf.codUsuario.strip()
        if attr == "nombre":
            attr_comparar = filelf.nombreUsuario.strip()
        if attr == "clave":
            attr_comparar = filelf.claveUsuario.strip()
        if attr == "tipo":
            attr_comparar = filelf.tipoUsuario.strip()

        
        if attr_comparar == x:
            condicional = True
            tipo = filelf.tipoUsuario.strip()
            
    return condicional, tipo
    
    
def crear_usuario(tipo):
    global afusuarios
    usuario = USUARIOS()
    
    usuario.codUsuario = asig_codigo()
    usuario.nombreUsuario = ingreso_mail()
    usuario.claveUsuario = ingreso_clave()
    usuario.tipoUsuario = tipo
    
    formatear_usuario(usuario)
    pickle.dump(usuario, afusuarios)
    afusuarios.flush()
        
    
def asig_codigo():
    global afusuarios, urlusuarios
    tam = os.path.getsize(urlusuarios)
    aux = USUARIOS
    
    codigo = 0
    cont = 0
    
    afusuarios.seek(0,0)
    while  afusuarios.tell() < tam :
        aux = pickle.load(afusuarios)
        cont+=1
        
    afusuarios.seek(0,0)
    
    iguales = True
    
    while iguales != False and codigo <= cont:
        codigo += 1
        iguales, no_use = lookForUser(codigo, "code")
        
    return codigo
        
def  ingreso_mail():
    dominio = "@shopping.com"
    condicion = True
    nombre = " "
    while condicion == True and len(nombre)<=100:
        os.system("cls")
        print("  ----- ingrese un nombre de usuario  ( el sistema agregara el dominio @shopping.com!!!! ) -----")
        nombre = input("")
        nombre = nombre + dominio
        if len(nombre)>100:
            print("MAXIMA CANTIDAD DE CARACTERES PERMITIDOS: 100")
            msvcrt.getch()
        else:
            condicion, no_use = lookForUser(nombre, "nombre")
        
    return nombre
        
    
def ingreso_clave():
    condicion = True
    while condicion == True:
        os.system("cls")
        print("  ----- ingrese una clave con 8 digitos -----")
        clave = input("")
        
        if len(clave) == 8:
            condicion, no_use = lookForUser(clave, "clave")
        else:
            print("LA CLAVE DEBE TENER 8 DIGITOS")
            msvcrt.getch()
        
    return clave


def validar_usuario(condicional):  # ingreso seguro de la contra asi como validacion
    
    usr = ""  # variables para validacion de usuario
    contr_input = ""  # variables para validacion de contraseña
    i = 3  # variable tipo entero de la cantidad de intentos incorrectos
    
    while condicional == True:
        
        usr = input("Ingrese su nombre de usuario: ")
        usr_aprob, tipo = lookForUser(usr,'nombre')
        contr_input = getpass.getpass("Ingrese su contraseña: ")
        contr_aprob = lookForUser(contr_input, "clave")
    
        if usr_aprob != False and contr_aprob[0] != False:
            os.system("cls")
            print("ha iniciado sesion satisfactoriamente")
            if tipo == tipos_user[0]:                   #decidion del menu segun el tipo de usuario
                condicional = val_menu_admin(condicional)
            elif tipo == tipos_user[1]:
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
            crear_usuario("dueñoLocal")
            os.system("cls")
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
            condicional = elecciones_desc(opcion)


def elecciones_desc(opcion):  # acciones del submenu de duenos
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
            return False 


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
            mapa_locales()
            return True 
        case "e":
            os.system("cls")
            return False


def crear_locales():  # accion de crear
    global max_locales, aflocales, urllocales
    local = LOCALES()
    local.nombreLocal = " "
    
    pregunta = "desea ver los locales?"
    aux = ask_continue(pregunta)
    if aux == 's':
        ver_locales()
    
    
    userOwner = lookForUser("dueñoLocal", "tipo")
    
    if userOwner[0] != False:
        while local.nombreLocal != "*" and max_locales != 50:
            
            local.nombreLocal = ingreso_nombre()
            
            if local.nombreLocal != '*':
                
                local.ubicacionLocal = ingreso_ubi()
                
                local.rubroLocal = ingreso_rubro ()
                
                local.codUsuario = ingreso_codigos()
                
                local.codLocal = asig_codLocal()
                
                local.estado = "A"
                
                formatear_locales(local)
                #asignar_codigo_active (fila,column)
                
                pickle.dump(local, aflocales)
                aflocales.flush()
                
                max_locales = cuentaLocales()
                ordenar()
    else:
        print("----- No existe una cuenta tipo dueño -----")
        msvcrt.getch()
    if max_locales == 50:
        os.system("cls")
        print("--- presione cualquier tecla para salir ---\n")
        print ("maxima cantidad de locales alcanzada\n")
        msvcrt.getch()
    
    os.system("cls")
    contador_rubro()
    return

def cuentaLocales():
    global aflocales, urllocales
    cont = 0
    aflocales.seek(0,0)
    tam = os.path.getsize(urllocales)
    if tam > 0:
        while aflocales.tell() < tam:
            prueba = aflocales.tell()
            x = pickle.load(aflocales)
            cont +=1
    return cont

def lookForLocals(x, attr):
    global aflocales, urllocales
    condicional = False
    aflocales.seek(0,0)
    tam = os.path.getsize(urllocales)
    filelf = LOCALES()
    attr_comparar = None
    pos =  None
    
    while aflocales.tell() < tam:
        before = aflocales.tell()
        filelf = pickle.load(aflocales)
        
        if attr == "codigoUsuario":
            attr_comparar = filelf.codUsuario.strip()
        if attr == "nombre":
            attr_comparar = filelf.nombreLocal.strip()
        if attr == "Ubicacion":
            attr_comparar = filelf.ubicacionLocal.strip()
        if attr == "estado":
            attr_comparar = filelf.estado.strip()
        if attr =="codigoLocal":
            attr_comparar = filelf.codLocal.strip()
            
        if attr_comparar == x:
            condicional = True
            pos = before
                
    return condicional,pos

def ingreso_nombre ():
    os.system("cls")
    cont = 0
    nombreLocal = " "
    while cont != 1 and nombreLocal != "*":
                                                            #ingreso del nombre del local
        print("---- ingresando un ' * ' se termina el ingreso de locales ----\n")
        nombreLocal = (input("Ingrese el nombre del local: ")).capitalize()
        
        if len(nombreLocal) > 2 and len(nombreLocal) <= 15:   
            special = char_allow(nombreLocal)
            
            if special != True: 
                aprob, pos_no_use = lookForLocals(nombreLocal, "nombre") 
                
                if aprob != True:
                    cont+= 1  #saliendo de loop si no se repite
                else:
                    repetido("el nombre")
            else:
                os.system("cls")
                print("Caracter no permitido\n")
                
        elif nombreLocal != '*' and len(nombreLocal) < 3:
            os.system("cls")
            print ("---- minimo de caracteres permitidos: 3 ----")
            
        elif nombreLocal != '*' and len(nombreLocal) > 15:
             os.system("cls")
             print ("---- maximo de caracteres permitidos: 15 ----")
    
    return nombreLocal


def ingreso_ubi ():
    cont = 0
    os.system("cls")
    while cont != 1:             
        ubicacionLocal = (input("Ingrese la ubicacion: ")).capitalize()                     #ingreso de ubicacion
        
        if len(ubicacionLocal) > 3 and len(ubicacionLocal) <= 15: 
            special = char_allow(ubicacionLocal)              
                              
            if special != True:                                  #guardando ubicacion
                cont += 1
            else:
                os.system("cls")
                print("Caracter no permitido\n")
        elif len(ubicacionLocal) < 4:
            os.system("cls")
            print("---- minimo de caracteres permitidos: 4 ---- ")
        elif  len(ubicacionLocal) > 15:
            os.system("cls")
            print("---- maximo de caracteres permitidos: 15 ----")
            
    return ubicacionLocal


def ingreso_rubro(): #ingreso de rubro
    os.system("cls")
    aux = False
    while aux != True:
        rubroLocal = input("Escoja un rubro: indumentaria, perfumería o comida\n")
        rubroLocal = (rubroLocal.lower())  # en caso de tipear una mayuscula la transformamos a minuscula
        aux = busqueda_uni(tipo_local, 3, rubroLocal) #verificando existencia del rubro
        os.system("cls")
        if aux == False:
            print("rubro ivalido")
            
    return rubroLocal

def busqueda_uni (buscar, lim,buscado): #busqueda unidimensional
    aux = False
    for i in range(0, lim):
        if buscar [i] == buscado:
            aux = True
    return aux

def asig_codLocal():
    global aflocales, urllocales
    
    aux = LOCALES
    cont = 0
    tam = os.path.getsize(urllocales)
    aflocales.seek(0,0)
    while tam > aflocales.tell():
        aux = pickle.load(aflocales) 
        cont+=1
        
    return cont+1

def ingreso_codigos ():   #ingreso de los codigos y el estado
    cont = 0
    
    while cont != 1:                                                                                                           
        cod_owner = input("ingrese el codigo: ")
        aprob = verif_num(cod_owner)                 #verificando si en el numero es numero para cuando se intente pasar de str a int no de error (logramos descartar el try que teniamos antes)                                                 
        if aprob != False:
            cod_owner = int(cod_owner)
            aux, tipo =  lookForUser(cod_owner, "code") 
               
            if aux == True and tipo == tipos_user[1]:    # si existe y es un codigo de dueno se guarda
                cont += 1
            else:
                os.system("cls")
                print("Codigo Invalido!!!!")
        else:
            os.system("cls")
            print("Codigo Invalido!!!!")
    
    return cod_owner
         
def contador_rubro ():
    
    contador_max_min = [cont_indu, cont_per, cont_comida] #adiganando los contadores a un array
    for i in range(0,3):
        contador_max_min[i] = contador(i)
    
    contador_max_min, tipos = max_min_arrays(contador_max_min, tipo_local) #organizandolos de mayor a menor
    
    for i in range(0,3):
            print(f"Cantidad de locales de {tipos[i]}: {contador_max_min[i]}") #print de cantidad de locales al terminar carga de locales
    print("---------  ----------")
    
def contador (type): #contador utilizado para la cantidad de locales 
    global aflocales,urllocales
    cont = 0
    tam = os.path.getsize(urllocales)
    aflocales.seek(0,0)
    aux = LOCALES()
    
    while aflocales.tell() < tam :
        prueba = aflocales.tell()
        aux = pickle.load(aflocales)
        if  (aux.rubroLocal).strip() == tipo_local[type] and aux.estado == "A":
            cont += 1
                
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


def modificar ():
    global aflocales, urllocales
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
                    condi, pos = lookForLocals(modificar, "codigoLocal")
                    if condi != False:
                        local = LOCALES()
                        aflocales.seek(pos, 0)
                        local = pickle.load(aflocales)
                        if local.estado != "A":
                            pregunta = "----El local que ingreso se encuentra dado de baja (B) ----\n\nDesea activarlo?"
                            ask = ask_continue(pregunta)
                            if ask != "n":
                                local.estado = "A"
                        
                        if  local.estado != "B":
                            choice_modifi(local)
                            formatear_locales(local)
                            aflocales.seek(pos,0)
                            pickle.dump(local, aflocales)
                            aflocales.flush()
                            
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

def choice_modifi(modificar):
    condicional = True
    while condicional == True:
        os.system("cls")
        print (f"---- Elija Atributo a Modificar del local {modificar.codLocal}----\n")
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
            condicional = elecciones_modifi(opcion, modificar)
    return

def elecciones_modifi(opcion,modificar):
    match opcion:
        case '1':
            modificar.nombreLocal = modifi_name ()
            return True
        case '2':
            modificar.ubicacionLocal = ingreso_ubi() 
            return True
        case '3':
            modificar.rubroLocal = ingreso_rubro()
            return True
        case '4':
            modificar.codUsuario = ingreso_codigos ()
            return True
        case '0':
            return False

def modifi_name ():
    cont = 0
    while cont != 1 :
        nombreLocal = (input("Ingrese el nombre del local: ")).capitalize()
        
        if len(nombreLocal) > 2 and len(nombreLocal) <= 15:   
            special = char_allow(nombreLocal)
        
            if special != True: 
                aprob, no_use = lookForLocals(nombreLocal, "nombre")      #busqueda verificacndo que no existe otro local con el mismo nombre
                if aprob != True :
                    cont+= 1                        
                else:
                    repetido("el nombre")
            else:
                os.system("cls")
                print("Caracter no permitido\n")
        elif len(nombreLocal) < 3:
            os.system("cls")
            print ("---- minimo de caracteres permitidos: 3 ----")
        elif len(nombreLocal) > 15:
             os.system("cls")
             print ("---- maximo de caracteres permitidos: 15 ----")
             
    return nombreLocal

def borrar():
    global aflocales, urllocales
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
                condi, pos = lookForLocals(borrar, "codigoLocal")
                if condi != False :
                    local = LOCALES()
                    aflocales.seek(pos, 0)
                    local = pickle.load(aflocales)
                    if local.estado != "B":
                        cont += 1
                        aflocales.seek(pos,0)
                        local.estado = "B"
                        pickle.dump(local,aflocales)
                        aflocales.flush()
                        os.system("cls")
                        print("---- Local borrado ----\n")
                    else:
                        os.system("cls")
                        print(f"---- el local {borrar} ya se encuentra dado de baja ----\n")
                        
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
    global aflocales, urllocales
 # Exibir mapa: 
    os.system("cls")
    print("---- Mapa del shopping ----\n")
    
    local = LOCALES()
    aflocales.seek(0,0)
    for i in range(0,10):
        print("+--+--+--+--+--+")
        for j in range(0,5):
        
            try:
                local = pickle.load(aflocales)
                nro = int(local.codLocal)
            except:
                nro = 0
    
            if nro <10:
                print(f"|0{nro}", end="")
            else:
                print(f"|{nro}", end="")
                
        print("|")    
    print("+--+--+--+--+--+\n")
    print("---- presione cualquier tecla para salir ----")
    msvcrt.getch()
    os.system("cls")
        
        
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
    global afusuarios
    
    users = [ 1,"admin@shopping.com", "12345", tipos_user[0]]
    
    #precargando usuario
    b = USUARIOS()
    b.codUsuario = users[0]
    
    b.nombreUsuario =  users[1] 
        
    b.claveUsuario = users[2]
        
    b.tipoUsuario = users[3]
        
    #formatear(b)
        
    pickle.dump(b,afusuarios)
    afusuarios.flush()

             
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

            
# def busq_dico()              

def ordenar():  #funcion encargada de ordenar el array locales
    global aflocales, urllocales, max_locales
    max_locales = cuentaLocales()
    
    if max_locales > 1:
        aflocales.seek(0,0)
        aux = pickle.load(aflocales)
        wherefile = aflocales.tell()
        tamfile = os.path.getsize(urllocales)
        cantrep = int(tamfile/wherefile)
        auxi = LOCALES()
        auxj = LOCALES()
        
        for i in range(0,cantrep-1):
            for j in range(i+1,cantrep):
                
                aflocales.seek(i*wherefile, 0)
                auxi = pickle.load(aflocales)
                first_character_1 = auxi.nombreLocal[0].upper()  #se obtine la primera letra de una posicion en la columna de los nombres del array locales y se guarda en una variable
                    
                aflocales.seek(j*wherefile,0)
                auxj = pickle.load(aflocales)  
                first_character_2 = auxj.nombreLocal[0].upper()       #luego se hace lo mismo con la posicion siguiente
                    
                if first_character_1 > first_character_2:
                    aflocales.seek(i*wherefile, 0)
                    pickle.dump(auxj, aflocales)
                    aflocales.seek(j*wherefile,0)
                    pickle.dump(auxi,aflocales)
                    aflocales.flush()
                            
    
def ver_locales():  #print en pantalla de la tabla de locales 
    global aflocales, urllocales, max_locales
    max_locales = cuentaLocales()
    if max_locales != 0:
        print ("Presione culaquier tecla para continuar\n")
        aflocales.seek(0,0)
        tam = os.path.getsize(urllocales)
        aux = LOCALES()
        
        #Encabezado
        print ("Codigo Local              ",end="")
        print ("Nombre                    ",end="") 
        print ("Ubicacion                 ",end="")
        print ("Rubro                     ",end="")
        print ("Codigo dueño              ",end="")
        print ("Estado                    ",end="")
        
        while aflocales.tell() < tam:
            aux = pickle.load(aflocales)
            print("")
            
            spaces = (25 - len(str(aux.codLocal))) * " "
            print (str(aux.codLocal).capitalize(),spaces, end="")
            
            spaces = (25 - len(aux.nombreLocal)) * " "
            print (aux.nombreLocal.capitalize(),spaces, end="")
            
            spaces = (25 - len(aux.ubicacionLocal)) * " "
            print (aux.ubicacionLocal.capitalize(),spaces, end="")
            
            spaces = (25 - len(aux.rubroLocal)) * " "
            print (aux.rubroLocal.capitalize(),spaces, end="")
            
            spaces = (25 - len(str(aux.codUsuario))) * " "
            print (str(aux.codUsuario).capitalize(),spaces, end="")
            
            spaces = (25 - len(aux.estado)) * " "
            print (aux.estado.capitalize(),spaces, end="")
          
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


def formatear_usuario(usr):
    
    usr.codUsuario = str(usr.codUsuario)
    usr.codUsuario = usr.codUsuario.ljust(3, ' ')
    usr.nombreUsuario = str(usr.nombreUsuario).ljust(20, ' ')
    usr.claveUsuario = str(usr.claveUsuario).ljust(8,' ')
    usr.tipoUsuario = str(usr.tipoUsuario).ljust(13,' ')


def formatear_locales(x):
     x.codLocal = str(x.codLocal) 
     x.codLocal = x.codLocal.ljust(3," ") 
     x.nombreLocal = str(x.nombreLocal).ljust(15, " ") 
     x.ubicacionLocal = str(x.ubicacionLocal).ljust(15," ")
     x.rubroLocal = str(x.rubroLocal).ljust(12," ")
     x.codUsuario = str(x.codUsuario)
     x.codUsuario = x.codUsuario.ljust(3, " ")
     x.estado = str(x.estado)
    
# programa principal
os.system("cls")

urlusuarios = "./USUARIOS.dat"
if not(os.path.exists(urlusuarios)):
    afusuarios = open(urlusuarios, "w+b")
    precarga()
else:
    afusuarios = open(urlusuarios, "r+b")


urllocales = "./LOCALES.dat"
if not (os.path.exists(urllocales)):
    aflocales = open (urllocales, "w+b")
else:
    aflocales = open (urllocales, "r+b")


max_locales = cuentaLocales()

validar_inicio()

afusuarios.close()
aflocales.close()