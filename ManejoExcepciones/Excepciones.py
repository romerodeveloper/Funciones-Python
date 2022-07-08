#Excepcion de tipo try(intentar) y except(excepto)


from cmath import e


try: 
    num = int(input("ingrese un numero: "))
    print("el numero {} y al dividirlo da {}".format(num,num/num))
except:
    print("intente de nuevo")
#Se activa si no se ejecuta ninguna excepcion
else:
    print("la ejecucion fue exitosa")
#Se ejecuta sin importar si se ejecuta alguna excepcion
finally:
    print("Se realizo un proceso bien o mal, no importa")

#Excepciones multiples

#Ejemplo para obtener el nombre especifico de la variable de excepcion
try: 
    num_2 = int(input("ingrese un numero: "))
    print("el numero {} y al dividirlo da {}".format(num_2,num_2/num_2))
except Exception as e:
    print("Ocurrio el siguiente error: ", type(e).__name__)

#Ejemplo de excepcion multiple
#Se debe definir el Exception como ultima opcion, de lo contrario no evaluara las otras opciones
try: 
    num_2 = int(input("ingrese un numero: "))
    print(" 9 / {} y al dividirlo da {}".format(num_2,9/num_2))
except ValueError:
    print("No se puede dividir 9 entre un texto")
except ZeroDivisionError:
    print("No se puede dividir entre cero. Intenta de nuevo")
except Exception as e:
    print("Ocurrio el siguiente error: ", type(e).__name__)
    
