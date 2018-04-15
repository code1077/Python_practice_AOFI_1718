import time
numero=int(input("Dime un numero para cuenta atras:\n"))
for i in range (numero):
		print (numero)
		time.sleep(1)
		numero-=1
print(numero,"!!COHETE VAAA!!")