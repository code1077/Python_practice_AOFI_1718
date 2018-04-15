import time
bucle = "si"
tablas = 0
numeros = 0


while bucle == "si":
	tablas = int(input ("Que tabla de multiplicar quieres saber?\n"))
	for numeros in range(11):
		print(tablas, " * ", numeros, "=",tablas * numeros)
		time.sleep(0.5)
	bucle = input ("Quieres continuar con otra tabla? Si o No\n")	
	if bucle != "si":
		print ("Hasta Luego")