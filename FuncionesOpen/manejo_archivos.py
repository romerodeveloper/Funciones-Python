from typing import final

#Clase creada para el manejo de archivos txt sin el with
#Para el uso de caracteres especiales usamos el atributo encoding
try:
    archivo = open(r'C:\Users\NICOLAS\Desktop\prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo \n')
    archivo.write('Adios')
    #lectura de un archivo de algunos caracteres
    archivo1 = open(r'C:\Users\NICOLAS\Desktop\prueba.txt', 'r', encoding='utf8')
    print(archivo1.read())
except Exception as e:
    print(e)
finally: 
    archivo.close()
    print("Fin del archivo")