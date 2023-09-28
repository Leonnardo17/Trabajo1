import tabulate
INT = [0]
STRING = [""]

COD = INT * 101
USER = STRING * 101
CLAVE = STRING * 101
TIPO = STRING * 101

BASE = [COD, USER, CLAVE, TIPO]
type_1 = "administrador"
type_2 = "dueñoLocal"
type_3 = "cliente"

def precarga():
    
    # Primer usuario
    
    COD[0] = 1
    USER[0] = "admin@shopping.com"
    CLAVE[0] =  "12345   "
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
    CLAVE[3] =  "33xx33  "
    TIPO [3] = type_3
    


precarga()

x = BASE[1][3].upper()
x = x[0]

z = BASE[1][2].upper()
z = z[0]

if x > z: 
    print(z, x)

# for i in range (0,5):
#     firstChar1 = BASE[1][i]
#     firstChar2 = BASE[1][i+1]
#     if firstChar1 > firstChar2:
#         for j in range(0,4):
#             aux = BASE[j][i]
#             BASE[j][i] = BASE[1][i+1]
#             BASE[j][i+1] = aux


# locales_ordenados = locales
#     for i in range(0,LIM_LOCALS_ROW-1):
#         first_character_1 = locales [1][i]
#         first_character_2 = locales [1][i+1]
#         if first_character_1 > first_character_2:
#             for j in range(0,LIM_LOCALS_COL):
#                 aux = locales_ordenados[j][i]
#                 locales_ordenados[j][i] = locales_ordenados[j][i+1]
#                 locales_ordenados[j][i] = aux


# name = 'mango'

# if len(name) > 0:
#     firstChar = name[0]
#     print(f'First character : {firstChar}')
# else:
#     print('The string is empty. Please check.')
# print(BASE[3][0])
