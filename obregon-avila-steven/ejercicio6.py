
numero = 0
bucle = "Si"
while bucle == "Si":
	numero = int(input("Introduce el numero que quieras:\n"))
	if (numero % 2 == 0):
		print("Este numero es par") 
	if (numero % 2 != 0):
		print("Este numero es inpar")
	bucle = input ("Quieres añadir mas datos a la tabla?: si/no ?\n")	
	if bucle != "Si":