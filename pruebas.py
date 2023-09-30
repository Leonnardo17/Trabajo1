import getpass
import io
import pickle
import os
import os.path
import msvcrt
import pandas as pd
import inspect

tipos_user = ["administrador", "dueñoLocal", "cliente"]

class USUARIOS():
    
    def __init__(self):
        self.codUsuario = 0
        self.nombreUsuario = " "
        self.claveUsuario = " "
        self.tipoUsuario = " "
        
    # def __str__(self) :
    #     return f'usuario: {self.codUsuario} ,{self.nombreUsuario}, {self.claveUsuario} , {self.tipoUsuario}'



def precarga(): #precarga de los datos de las cuentas
    global afusuarios, tipos_user

    #, 4,"localA@shopping.com", "AAAA1111", tipos_user[1], 6, "localB@shopping.com","BBBB2222", tipos_user[1], 9, "unCliente@shopping.com", "33xx33",tipos_user[2]
    #antiguos usuarios, se usaran despues para hacer pruebas!!!!
    
    users = [ 1,"admin@shopping.com", "12345", tipos_user[0], 4,"localA@shopping.com", "AAAA1111", tipos_user[1], 6, "localB@shopping.com","BBBB2222", tipos_user[1], 9, "unCliente@shopping.com", "33xx33",tipos_user[2]]

    cont = 0
    
    #precargando usuario
    
    b = USUARIOS()
    for i in range(0, 4):
        
        b.codUsuario = users[cont]
        cont+=1
        b.nombreUsuario =  users[cont]
        cont+=1
        b.claveUsuario = users[cont]
        cont+=1
        b.tipoUsuario = users[cont]
        cont+=1
        
        # formatear(b)
        
        pickle.dump(b,afusuarios)
        afusuarios.flush()
        
       
        
 
# def formatear(b):
#      b.codUsuario = str(b.codUsuario).ljust(3, ' ')
#      b.nombreUsuario = str(b.nombreUsuario).ljust(20, ' ')
#      b.claveUsuario = str(b.claveUsuario).ljust(8,' ')
#      b.tipoUsuario = str(b.tipoUsuario).ljust(12,' ')


def lookFor (x, attr):
    global afusuarios, urlusuarios
    condicional = False
    afusuarios.seek(0,0 )
    tam = os.path.getsize(urlusuarios)
    filelf = USUARIOS()
    y = None
    tipo = None
    
    while afusuarios.tell() <tam:
        filelf = pickle.load(afusuarios)

        
        if attr == "code":
            y = filelf.codUsuario
        if attr == "nombre":
            y = filelf.nombreUsuario
        if attr == "clave":
            y = filelf.claveUsuario
        if attr == "tipo":
            y = filelf.tipoUsuario

        
        if y == x:
            condicional = True
            tipo = filelf.tipoUsuario
          
    return condicional, tipo
        
         

urlusuarios = "./USUARIOS.dat"
if not(os.path.exists(urlusuarios)):
    afusuarios = open(urlusuarios, "w+b")
    precarga()
else:
    afusuarios = open(urlusuarios, "r+b")



x = "12345"




respuesta = lookFor(x, "clave")
print(respuesta)


# afusuarios.seek(0,0)
# x = USUARIOS()
# x= pickle.load(afusuarios)
# tam = afusuarios.tell()
# afusuarios.seek(0,0)
# x = pickle.load(afusuarios)

# print (x.claveUsuario)




