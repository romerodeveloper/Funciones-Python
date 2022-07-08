#Ejemplos de funciones open
#El uso de with es para la optimizacion de abrir y cerrar el archivo con el cual vamos a trabajar, el se encarga de hacer esas junciones automaticamente
#f es la asignacion de ese fichero para su debida lectura o creacion

#el argumento dos 'w' sobreescribe el texto del documento
with open(r'C:\Users\NICOLAS\Desktop\prueba2.txt', 'w') as f:
    f.write('los poemas y sus esplendidos versos')

#el argumento 'r' leera las cadenas del archivo ademas de requerir el uso de la funcion read()
with open(r'C:\Users\NICOLAS\Desktop\prueba.txt', 'r') as f:
    print(f.read())

#la funcion readlines() nos permite leer las cadenas linea por linea y retornar un array list de las cadenas
with open(r'C:\Users\NICOLAS\Desktop\prueba.txt', 'r') as f:
    data = f.readlines()
    #print(data)

#ejemplo de separar las palabras de una cadena y almacenarlas en una lista
with open(r'C:\Users\NICOLAS\Desktop\prueba.txt', 'r') as f:
    for linea in f:
        palabras = linea.split()
        #print(palabras)

#ejemplo para separar y contener todas las palabras del archivo
with open(r'C:\Users\NICOLAS\Desktop\prueba.txt', 'r') as f:
    lista = []
    for linea in f:
        palabras = linea.split()
        for palabra in palabras:
            lista.append(palabra)
    print(lista)