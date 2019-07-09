#Nombre: factorial.py
#Objetivo: Obtener el factorial de un numero
#Autor: Mario Rubén Mancilla Tinoco
#Fecha: 01 de julio 2019

#Funcion para calcular el factorial
def fact(num, facto):
	if(num > 1):
		facto = facto * num
		num = num-1
		fact(num, facto)
	else:
		print("EL factorial del numero ", num, " es el siguiente: ", facto)

#Funcion principal
def main():
	facto = 1
	num = int(input("Ingrese un numero: "))
	fact(num, facto)

if __name__ == '__main__':
	main()