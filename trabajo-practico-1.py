import getpass
import os 


def inicializo ():
    global USER, CONTR, user_input, contr_input, i, condicional, cont_indu, cont_comida, cont_per
    USER = 'admin@shopping.com'#usuario. tipo string
    CONTR = '12345' # contraseña. tipo string

    user_input = '' #variables para validacion de usuario
    contr_input = '' #variables para validacion de contraseña
    i = 3 #variable tipo entero de la cantidad de intentos incorrectos
    condicional = True #variable tipo bool

    #variables tipo entero. (contadores de Rubros)
    cont_indu = 0
    cont_per = 0
    cont_comida = 0

def validarUsuario(condicional):
    while condicional != False:
        usr = input('Ingrese su nombre de usuario: ')
        
        while usr != USER:
            os.system('cls')
            print('Nombre de usuario incorrecto')
            validarUsuario(condicional)
        
        os.system('cls')
        validarpassword (condicional)
        
def validarpassword(condicional):
    global i
    while(condicional == True):
        
        contr_input = getpass.getpass('Ingrese su contraseña: ')
    
        if(contr_input == CONTR):
            os.system('cls')
            print ("ha iniciado sesion satisfactoriamente")
            condicional = val_opc_menu_1 (condicional)
        elif(i > 1):
            i = i-1
            os.system ('cls')
            print('Tiene', i, 'cantidad de intentos restantes')
        else:
            os.system('cls')
            print('Máximo de intentos permitidos alcanzado')
            condicional = False
            exit ()
    
    
def menu (): #print del menu principal
     print ("1. Gestion de Locales")
     print ("2. Crear cuentas de dueños")
     print ("3. Aprobar / Denegar solicitud de descuento")
     print ("4. gestión de novedades")
     print ("5. Reporte")
     print ("0. salir ")

def val_opc_menu_1 (condicional):
    while condicional == True:
        
        menu()
        opcion = input("ingrese un numero: ")
        
        if (opcion != '0' and opcion !='1' and opcion != '2' and opcion !='3' and opcion != '4' and opcion !='5'):
            opcion_erronea()
        else:
            os.system('cls')
            condicional = elecciones (opcion)
            continue 
    
    return (condicional)

def elecciones (opcion): #acciones y validacion de input menu princial
    match opcion:
        case  '1' :  
            menu_op1 (condicional)
             
        case '2' : 
            en_contruccion ()
            return True
         
        case '3' : 
            en_contruccion ()
            return True
         
        case '4' : 
            menu_op4 (condicional)
            return True
         
        case '5' : 
            en_contruccion ()
            return True
             
        case '0' :
            print ("saliendo del programa")
            exit ()
            
        
def menu_op1 (condicional): # mostrar menu opcion 1)
    while condicional == True:
        print ("a) Crear locales")
        print ("b) Modificar local")
        print ("c) Eliminar local")
        print ("d) Volver")
        opcion = input("ecsriba una opcion: ")
        opcion = opcion.lower()
        if (opcion != 'a' and  opcion != 'b' and opcion != 'c' and opcion != 'd'):
            opcion_erronea()
        else:
            condicional = elecciones_op1 (opcion)
    os.system ('cls')
    return True

def elecciones_op1 (opcion): #acciones del menu y validacion 1) 
    match opcion:
        case "a" : 
            os.system('cls')
            crear_locales ()
            return True
        case "b" : 
            en_contruccion ()
            return True
        case "c" : 
            en_contruccion ()
            return True
        case "d": 
            os.system('cls')
            return val_opc_menu_1 (condicional)
        
def crear_locales (): #accion de crear
    aux1 = 'y'
    global cont_indu
    global cont_per
    global cont_comida
    while  aux1 != 'n':
        aux2 = True
        auxru = True
        nombreLocal = input("ingrese el nombre del local: ")
        os.system('cls')
        ubicacionLocal = input ("ingrese la ubicacion: ")
        
        while auxru == True:
            rubro = input("escoja un rubro: indumentaria, perfumería o comida\n")
            rubro = rubro.lower()
            os.system('cls')
            match rubro :
                case "indumentaria" : 
                    cont_indu = cont_indu + 1
                    auxru = False
                case "perfumeria" : 
                    cont_per = cont_per + 1
                    auxru = False
                case "comida" :
                    cont_comida = cont_comida + 1
                    auxru = False
                case _ :
                    print ("rubro ivalido")
                    
        while aux2 == True :           
            aux1 = input("desea crear otro local? (n/y)\n")
            aux1 = aux1.lower()
            if (aux1 == 'y' or aux1 == 'n'):
                aux2 = False 
            else:
                print ("letra incorrecta")
        os.system('cls')

    mostrar_max_min ()
    return True   

def mostrar_max_min (): #decision de el rubro mayor o menor
        if cont_indu < cont_per:
         if cont_indu < cont_comida:
            min_locals = cont_indu # si se dan las dos primeras entonces cont_indu es menor
            if cont_per > cont_comida:
                more_locals = cont_per # y cont_per es mayor 
                print (f"El rubro con la mayor cantidad de locales es: Perfumeria y cuenta con {more_locals} locales")
                print (f"El rubro con la menor cantidad de locales es: Indumentaria y cuenta con {min_locals} locales")
            else:       
                more_locals = cont_comida #sino cont_comida es menor
                print (f"El rubro con la mayor cantidad de locales es: Comida y cuenta con {more_locals} locales")
                print (f"El rubro con la menor cantidad de locales es: Indumentaria y cuenta con {min_locals} locales")
         else:
            more_locals = cont_per #si no se dio la segunda entonces cont_per es mayor y cont_comida es menor
            min_locals = cont_comida  
            print (f"El rubro con la mayor cantidad de locales es: Perfumeria y cuenta con {more_locals} locales")
            print (f"El rubro con la menor cantidad de locales es: Comida y cuenta con {min_locals} locales")
        elif cont_indu > cont_comida:#si no se da la primera y cont_indu es tambien mayor a  cont cont comida entonces es mayor 
            more_locals = cont_indu
            if cont_per > cont_comida:
                min_locals = cont_comida #si cont_per  es mayor que cont_comida  entones cont_comida es el menor
                print (f"El rubro con la mayor cantidad de locales es: Indumentaria y cuenta con {more_locals} locales")
                print (f"El rubro con la menor cantidad de locales es: Comida y cuenta con {min_locals} locales")
            else:
                min_locals = cont_per  #sino es cont_per el menor
                print (f"El rubro con la mayor cantidad de locales es: Indumentaria y cuenta con {more_locals} locales")
                print (f"El rubro con la menor cantidad de locales es: Perfumeria y cuenta con {min_locals} locales")
        else:
            more_locals = cont_comida #si cont_indu es mayor que cont_per y cont_comida es mayor que cont_indu entonces cont_ comida es mayor y cont_per menor
            min_locals = cont_per 
            print (f"El rubro con la mayor cantidad de locales es: Comida y cuenta con {more_locals} locales")
            print (f"El rubro con la menor cantidad de locales es: Perfumeria y cuenta con {min_locals} locales")

def menu_op4 (condicional):
    while condicional == True:
        print ("a) Crear novedades")
        print ("b) Modificar novedad")
        print ("c) Eliminar novedad")
        print ("d) Ver reporte de novedad")
        print ("e) Volver")
        opcion = input("ecsriba una opcion: ")
        opcion = opcion.lower()
        if (opcion != 'a' and  opcion != 'b' and opcion != 'c' and opcion != 'd' and opcion != 'e'):
            opcion_erronea()
        else:
         condicional = elecciones_op4 (opcion)
         continue
    

def elecciones_op4 (opcion):
    match opcion:
        case "a" : 
            en_contruccion ()
            return True
        case "b" : 
            en_contruccion ()
            return True
        case "c" : 
            en_contruccion ()
            return True
        case "d":
            en_contruccion ()
            return True
        case "e": 
            os.system('cls')
            return val_opc_menu_1 (condicional)
    

def opcion_erronea ():
    os.system('cls')
    print("-por favor seleccione una de la opciones correctas-\n")

def en_contruccion (): 
    os.system('cls')
    print ("-En contruccion-\n")
 
inicializo()
os.system('cls')    
validarUsuario (condicional)