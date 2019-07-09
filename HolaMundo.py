#Funcion para sumar dos numeros
def suma(num1, num2):
	return num1 + num2
#Funcion para restar dos numeros
def resta(num1, num2):
	return num1 - num2
#Funcion para multiplicar dos numeros
def multiplicacion(num1, num2):
	return num1 * num2
#Funcion para dividir dos numeros
def division(num1, num2):
	return num1 / num2
#Funcion para comparar dos numeros
def compara(num1, num2):
	if(num1 > num2):
		print ("El mayor es num1: ", num1)
	elif(num2 > num1):
		print ("EL mayor es num2: ", num2)
	else:
		print ("Los numeros son iguales :", num1, " = ", num2)

#Funcion main
def main():
	ciclo = True
	while(ciclo == True):
		print ("---Operaciones basicas---")
		n1 = int(input("Introduce el primer numero: "))
		n2 = int(input("Introduce el segundo numero: "))

		#Invocamos a las funciones
		print("La suma es: " + str(suma(n1, n2)))
		print("La resta es: " + str(resta(n1, n2)))
		print("La multiplicacion es: " + str(multiplicacion(n1 , n2)))
		print("La division es: " + str(division(n1, n2)))
		compara(n1, n2)
		cad = input("¿Quiere realizar otro calculo? s/n: ")
		if (cad == "n" or cad == "N"):
			ciclo = False

if __name__ == "__main__":
	main()