#Nombre: fibo.py
#Objetivo: Obtener la serie de fibonacci un cierto numero de veces
#Autor: Mario Rubén Mancilla Tinoco
#Fecha: 01 de julio 2019

#Funcion para calcular la serie de Fibonacci
def fibo(digitos):
	ant1 = 0
	ant2 = 1
	act = 1
	for i in range (0, digitos):
		print(act)
		act = ant1 + ant2
		ant1 = ant2
		ant2 = act

#Funcion principal
def main():
	digitos = int(input("Cuantos digitos quiere de la serie de Fibonacci? "))
	fibo(digitos)

if __name__ == '__main__':
	main()