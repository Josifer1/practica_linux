# Abre el archivo en modo escritura. Si el archivo no existe, se crea.
archivo = open("saludo.txt", "w")

# Escribe la cadena en el archivo.
archivo.write("Hola desde Python en Linux")

# Cierra el archivo. Esto es importante para guardar los cambios.
archivo.close()
