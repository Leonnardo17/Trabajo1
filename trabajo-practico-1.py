import getpass
import os 

def inicializo (): #declaracion de variables
    global USER, CONTR, usr, contr_input, i, condicional, cont_indu, cont_comida, cont_per,aux1, aux2, auxru
    global mas_locales, menos_locales, nombreLocal, ubicacionLocal, rubroLocal, iguales, diferente
    #local
    nombreLocal = ' '
    ubicacionLocal = ' '
    rubroLocal = ' '
    
    #usuario
    USER = 'admin@shopping.com'#usuario. tipo string
    CONTR = '12345' # contraseña. tipo string

    usr = '' #variables para validacion de usuario
    contr_input = '' #variables para validacion de contraseña
    i = 3 #variable tipo entero de la cantidad de intentos incorrectos
    condicional = True #variable tipo bool

    #variables tipo entero. (contadores de Rubros)
    cont_indu = 0
    cont_per = 0
    cont_comida = 0
    
    #auxiliares usados en crear_locales ()
    aux1 = 'y'
    aux2 = True
    auxru = True
    
    #variables para mostrar el tipo de indumentaria que es mayor o menor
    mas_locales = ' '
    menos_locales = ' '
    
    #variables locales de choice
    iguales = ' '
    diferente = ' '
    #a = 0
    #b = 0
    #c = 0
    
    #variables locales de mostrar_max_min() para saber el orden en que colocar el mayor y menor
    #int more_locals 
    #int min_locals
        
def validar_usuario(condicional): #ingreso seguro de la contra asi como validacion
    global i
    while(condicional == True ):
        usr = input('Ingrese su nombre de usuario: ')
        contr_input = getpass.getpass('Ingrese su contraseña: ')
    
        if(contr_input == CONTR and usr == USER):
            os.system('cls')
            print ("ha iniciado sesion satisfactoriamente")
            condicional = val_opc_menu_prin (condicional)
        elif(i > 1):
            i = i-1
            os.system ('cls')
            print('Tiene', i, 'cantidad de intentos restantes')
        else:
            os.system('cls')
            print('Máximo de intentos permitidos alcanzado')
            condicional = False
            exit ()
    
    
def menu_principal (): #print del menu principal
     print ("1. Gestion de Locales")
     print ("2. Crear cuentas de dueños")
     print ("3. Aprobar / Denegar solicitud de descuento")
     print ("4. gestión de novedades")
     print ("5. Reporte")
     print ("0. salir ")

def val_opc_menu_prin (condicional): #seleccion y validacion del menu pirnciopal 
    while condicional == True:
        
        menu_principal()
        opcion = input("ingrese un numero: ")
        
        if (opcion != '0' and opcion !='1' and opcion != '2' and opcion !='3' and opcion != '4' and opcion !='5'):
            opcion_erronea()
        else:
            os.system('cls')
            condicional = elecciones (opcion)
            
    
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
            val_opc_menu_4 (condicional)
            return True
         
        case '5' : 
            en_contruccion ()
            return True
             
        case '0' :
            print ("saliendo del programa")
            exit ()
            
def menu_1 (): #exhibiendo el submenu1
    print ("a) Crear locales")
    print ("b) Modificar local")
    print ("c) Eliminar local")
    print ("d) Volver")

def menu_op1 (condicional): # seleccion y validacion del submenu 1
    while condicional == True:
        menu_1 ()
        opcion = input("ecsriba una opcion: ")
        opcion = opcion.lower()
        if (opcion != 'a' and  opcion != 'b' and opcion != 'c' and opcion != 'd'):
            opcion_erronea()
        else:
            condicional = elecciones_op1 (opcion)
    

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
            return val_opc_menu_prin (condicional)
        
def crear_locales (): #accion de crear
    aux1 = 's'
    while  aux1 != 'n':
        nombreLocal = input("Ingrese el nombre del local: ")
        os.system('cls')
        
        ubicacionLocal = input ("Ingrese la ubicacion: ")
        
        suma_conts ()   
        
        aux1 = ask_s_n ()   
            
    choice_iquals (cont_indu, cont_per, cont_comida)
    return  

def suma_conts ():
    global cont_indu
    global cont_per
    global cont_comida
    auxru = True
    while auxru == True:
            rubroLocal = input("Escoja un rubro: indumentaria, perfumería o comida\n")
            rubroLocal = rubroLocal.lower()    #en caso de tipear una mayuscula la transformamos a minuscula
            os.system('cls')
            match rubroLocal :
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
                    
def ask_s_n ():
    aux2 = True
    while aux2 == True :           
        aux1 = input("desea crear otro local? (s/n)\n")       #preguntando si desea crear otro local
        aux1 = aux1.lower()
        if (aux1 == 's' or aux1 == 'n'):                      #validando respuesta
            aux2 = False 
        else:
            print ("letra incorrecta")
    os.system('cls')
    return aux1
    

def choice_iquals (a, b, c):
    global iguales, diferente
    if (a == b and a != c ):
        iguales = 'indumentaria y perfumeria'
        diferente = 'comida'
        max_min_2_iguales (a,c)
    elif (a == c and a != b ):
        iguales = 'indumentaria y comida'
        diferente = 'perfumeria'
        max_min_2_iguales (a,b)
    elif (b == c and b != a ):
        iguales = 'perfumeria y comida'
        diferente = 'indumentaria'
        max_min_2_iguales (b,a)
    elif (a == b == c):
        print('todos los rubros tienen la misma cantidad de locales: ',a)
    else:
        choice_max_min_des ()
    
def max_min_2_iguales (iquals, dife):
    if (iquals > dife):
        print (f"{iguales} tienen la misma cantidad de locales: {iquals}")
        print (f"El rubro con menor cantidad de locales es {diferente} y cuenta con: {dife} locales")
    else:
       print (f"el rubro con mayor contidad de locales es: {diferente} y cuenta con: {dife} locales") 
       print (f"{iguales} son iguales y cuentan con {iquals}")
    

def choice_max_min_des (): #decision de el rubro mayor o menor
    global mas_locales, menos_locales
    if cont_indu < cont_per:
         if cont_indu < cont_comida:
            menos_locales = 'indumemtaria'                       # si se dan las dos primeras entonces cont_indu es menor
            if cont_per > cont_comida:                           # y cont_per es mayor que cont_comida entonces cont_per es el mayor
                mas_locales = 'Perfumeria'
                mostrar_max_min (cont_per,cont_indu)
            else:       
                mas_locales = 'comida'                           #sino cont_comida es mayor
                mostrar_max_min (cont_comida, cont_indu)
         else:
            mas_locales = 'Perfumeria'                           #si no se dio la segunda entonces cont_per es el mayor y cont_comida es el menor
            menos_locales = 'comida'
            mostrar_max_min (cont_per, cont_comida)
    elif cont_indu > cont_comida:                                #si no se da la primera y cont_indu es tambien mayor a cont_comida entonces cont_indu es mayor 
            mas_locales = 'Indumentaria'
            if cont_per > cont_comida:
                menos_locales = 'comida'                         #si cont_per  es mayor que cont_comida  entones cont_comida es el menor
                mostrar_max_min (cont_indu, cont_comida)
            else:
                menos_locales = 'Perfumeria'                      #sino es cont_per es el menor
                mostrar_max_min (cont_indu, cont_per)
    else:
            mas_locales = 'comida'                                #si cont_indu es mayor que cont_per y cont_comida es mayor que cont_indu entonces cont_ comida es mayor y cont_per menor
            menos_locales = 'perfumeria'
            mostrar_max_min (cont_comida, cont_per)

def mostrar_max_min (more_locals, min_locals): #exhibiendo mayores y menores
    print (f"El rubro con la mayor cantidad de locales es: {mas_locales} y cuenta con {more_locals} locales")
    print (f"El rubro con la menor cantidad de locales es: {menos_locales} y cuenta con {min_locals} locales")

def menu_4 (): #exhibiendo el submenu4
    print ("a) Crear novedades")
    print ("b) Modificar novedad")
    print ("c) Eliminar novedad")
    print ("d) Ver reporte de novedad")
    print ("e) Volver")

def val_opc_menu_4 (condicional): #validadando opcion del submenu4
    while condicional == True:
        menu_4 ()
        opcion = input("ecsriba una opcion: ")
        opcion = opcion.lower()
        if (opcion != 'a' and  opcion != 'b' and opcion != 'c' and opcion != 'd' and opcion != 'e'):
            opcion_erronea()
        else:
         condicional = elecciones_op4 (opcion)
         

def elecciones_op4 (opcion): #acciones del sub menu 4
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
            return val_opc_menu_prin (condicional)
    

def opcion_erronea (): #exhibiendo que la opcion tipeada fue erronea
    os.system('cls')
    print(" -por favor seleccione una de la opciones correctas-\n")

def en_contruccion (): #exhibiendo que la opcion seleccionada esta en construccion
    os.system('cls')
    print (" -En contruccion-\n")
 
#programa principal
inicializo()
os.system('cls')    
validar_usuario (condicional)