#Nombre: triangulo.py
#Objetivo: identifica el tipo de triangulo de acuerdo al valor de sus lados
#Autor: Mario Rubén Mancilla Tinoco
#Fecha: 01 de julio 2019

#Función para identificar el tipo de triangulo
def identificar(l1, l2, l3):
	if(l1 == l2 and l1 == l3):
		print("EL triangulo ingresado es Equilatero")
	elif(l1 != l2 and l1 != l3 and l2 != l3):
		print("El triangulo ingresado es Escaleno")
	else:
		print("EL triangulo ingresado es Isoceles")


#Función principal
def main():
	print("---Script para identificar triangulos")
	lado1 = float(input("Ingrese el lado 1: "))
	lado2 = float(input("Ingrese el lado 2: "))
	lado3 = float(input("Ingrese el lado 3: "))

	#Invocar funcion
	identificar(lado1, lado2, lado3)
	print("EL perimetro del triangulo es: ",(lado1 + lado2 + lado3))

if __name__ == '__main__':
	main()