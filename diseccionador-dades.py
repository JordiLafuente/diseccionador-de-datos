#Porgrama para la disección de los datos de un archivo CSV


#Indicamos al usuario que nos de el nombre del archivo a diseccionar
nombre_archivo = input("introduce el nombre del archivo a diseccionar: ")
#Comprovamos que se haya leido bien
print("Este es el nombre del archivo a diseccionar: \n" + nombre_archivo)
#Abrimos el archivo del nombre indicado, en modo solo lectura
archivo_origen = open(nombre_archivo, "r")
#Imprimimos la lectura de la primera linea del archivo de origen y devolvemos el puntero al principio del archivo de origen
print("Esta es la primera linea del archivo de origen: " + archivo_origen.readline())
archivo_origen.seek(0)
#Creamos el archivo de destino, en modo lectura y escritura
archivo_destino = open(str(nombre_archivo) + " diseccionado" + ".csv", "w+")
#Escribimos en el archivo de destino la primera linea del archivo de origen
archivo_destino.write(archivo_origen.readline())
#Devolvemos el puntero al principio del archivo de destino y lo imprimimos por pantalla
archivo_destino.seek(0)
print("Esto es lo que contiene el archivo destino: \n" + archivo_destino.read())


#Cerramos los archivos
archivo_origen.close()
archivo_destino.close()
