#TP de python:
#Mapa de Locales: Se sabe que la superficie de nuestro shopping tiene forma
#rectangular (10 filas por 5 columnas), y que todos los locales tienen el mismo tamaño.
#Se debe mostrar el código de cada local, de manera consecutiva, teniendo en cuenta
#que los locales están ordenados de manera alfabética por su nombre. Ejemplo: si solo
#existieran 3 locales, donde local 1 – Mimo / local 2 – Garbarino / local 3 – Frávega / al
#ordenarlos implica que los códigos que se colocarían en el mapa serían: 2 – 3 – 1.
#o Se desea obtener un pequeño mapa del shopping que tenga la siguiente forma:
#donde cada código de local debe estar encerrado en un rectángulo como en el diagrama
#anterior (separado por barras de valor absoluto | a los costados, y por signos +-+ arriba y
#abajo). Para los locales que aún no han sido ocupados, dejarlos con un número 0.
 
 # estructura del mapa del shopping
    filas = 10
    columnas = 5
 # Exibir mapa: 
    print("Mapa del shopping:")
    print("+---+---+---+---+---+")
    for i in range(filas):
        for j in range(columnas):
            codigo = mapa_shop[i][j]
            if codigo != "0":
                print(f"| {codigo:2s} ", end="")
            else:
                print("|    ", end="")
        print("|")
        print("+---+---+---+---+---+")

