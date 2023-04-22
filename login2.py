USER = 'admin@shopping.com'
CONTR = '12345'

user_input = ''
contr_input = ''
i = 3
condicional = True

#variables para crear_locales()
cont_indu = 0
cont_per = 0
cont_comida = 0

def en_contruccion ():
    print ("en contruccion")
    
def mostrar_max_min ():
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
    

def crear_locales (): 
    aux1 = 'y'
    while  aux1 != 'n':
        aux2 = True
        auxru = True
        nombre = input("ingrese el nombre del local: ")
        ubicacion = input ("ingrese la ubicacion: ")
        
        while auxru == True:
            global cont_indu
            global cont_per
            global cont_comida
            rubro = input("escoja un rubro: indumentaria, perfumería o comida\n")
            
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
            if aux1 == 'y':
                aux2 = False 
            elif aux1 == 'n':
                aux2 = False
            else:
                print ("letra incorrecta")

    mostrar_max_min ()
    return True     
        
    

def elecciones_op1 (opcion):
    match opcion:
        case "a" : 
            crear_locales ()
            return True
        case "b" : 
            en_contruccion ()
            return True
        case "c" : 
            en_contruccion ()
            return True
        case "d": 
            return menu (condicional)
        case _ : 
            print ("tipee una de las letras correspondientes: ")
            return True
        

def menu_op1 (condicional):
    while condicional == True:
        print ("a) Crear locales")
        print ("b) Modificar local")
        print ("c) Eliminar local")
        print ("d) Volver")
        opcion = input("ecsriba una opcion: ")
        condicional = elecciones_op1 (opcion)
    return True

def elecciones (opcion):
    match opcion:
        case  1 :  
             menu_op1 (condicional)
             
        case opcion if opcion> 1 and opcion < 6 : 
             en_contruccion ()
             return True     
        case 0 :
            print ("saliendo del programa")
            return False

def menu (condicional):
    while (condicional == True):
     print ("1. Gestion de Locales")
     print ("2. Crear cuentas de dueños")
     print ("3. Aprobar / Denegar solicitud de descuento")
     print ("4. gestión de novedades")
     print ("5. Reporte")
     print ("0. salir ")
     opcion = int (input("ingrese un numero: "))
     if opcion >= 0 and opcion <=5:
         condicional = elecciones (opcion)
         continue 
    
    return (condicional)

while(condicional == True):
    user_input = input('Ingrese su nombre de usuario: ')
    contr_input = input('Ingrese su contraseña: ')
    
    if(user_input == USER and contr_input == CONTR):
         print('Ha iniciado sección satisfactoriamente')
         condicional = menu (condicional)
    elif(i > 1):
         i = i-1
         print('Tiene', i, 'cantidad de intentos restantes')
    else:
         print('Máximo de intentos permitidos alcanzado')
         condicional = False
        