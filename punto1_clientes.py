def ValidarEntero(x):
    try:
        int(x)
    except: return True
     
def buscarCOD(x):
    global afpromo, alpromo
    t = os.path.getsize(afpromo)
    vrtemp = PROMOCIONES()
    encontrado = False
    alpromo.seek(0,0)
    while alpromo.tell() < t and not encontrado:
        pos = alpromo.tell()
        vrtemp = pickle.load(alpromo)
        if vrtemp.codLocal == x:
            encontrado = True    
    if encontrado:
        return pos
    else:
        return -1
    
def buscarPromos(c,f):
    global afpromo, alpromo
    tam = os.path.getsize(afpromo)
    vrtemp = PROMOCIONES()
    vrtemp = pickle.load(alpromo)
    alpromo.seek(0, 0)
    while vrtemp.tell() < tam:
        if vrtemp.codLocal == c and vrtemp.estado == "A" and vrtemp.fechaDesdePromo <= f.date() <= vrtemp.fechaHastaPromo:
            for i in range(6):
                if vrtemp.diasSemana[i] == 1:
                    encabezado = " "
                    encabezado += "{:<15}".format("Codigo Promo")
                    encabezado += "{:<40}".format("Texto")
                    encabezado += "{:<20}".format("Fecha desde")
                    encabezado += "{:<10}".format("Fecha hasta")
                    print(encabezado)
                    print("----------------------------------------------------------------------------------")
                    salida = " "
                    salida += "{:<15}".format(vrtemp.codPromo.strip())
                    salida += "{:<40}".format(vrtemp.textoPromo.strip())
                    salida += "{:<20}".format(vrtemp.fechaDesdePromo.strip())
                    salida += "{:<10}".format(vrtemp.fechaHastaPromo.strip())
                    print(salida)
        vrtemp = pickle.load(alpromo)

def buscarDescuentos():
    global alpromo, afpromo
    fecha_valida = False
    cod = print("Ingrese el codigo del local")
    while ValidarEntero:
        cod = input("Incorrecto, intente de nuevo")
    cod = int(cod)
    while not fecha_valida:
        fecha = input("Ingresa una fecha (dd/mm/aaaa): ")
        try:
            fecha_obj = datetime.datetime.strptime(fecha, "%d/%m/%Y")
            if fecha_obj.date() >= datetime.datetime.now().date():
                    fecha_valida = True
            else:
                print("La fecha ingresada debe ser igual o posterior a la fecha actual.")
        except ValueError:
            print("Formato de fecha incorrecto. Intente de nuevo (dd/mm/aaaa): ")
    buscarPromos(cod, fecha)