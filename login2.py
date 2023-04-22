USER = 'admin@shopping.com'
CONTR = '12345'

user_input = ''
contr_input = ''
i = 3
condicional = True

def elecciones (opcion):
    match opcion:
        case  1 :  
             print(" dentro de opcion 1") 
             return True
        case opcion if opcion> 1 and opcion < 6 : 
             print("En construccion...") 
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
        

    







      