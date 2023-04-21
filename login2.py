USER = 'admin@shopping.com'
CONTR = '12345'

user_input = ''
contr_input = ''
i = 3
condicional = True

while(condicional == True):
    user_input = input('Ingrese su nombre de usuario: ')
    contr_input = input('Ingrese su contraseña: ')
    
    if(user_input == USER and contr_input == CONTR):
        print('Ha iniciado sección satisfactoriamente')
        condicional = False
    elif(i > 1):
        i = i-1
        print('Tiene', i, 'cantidad de intentos restantes')
    else:
        print('Máximo de intentos permitidos alcanzado')
        condicional = False