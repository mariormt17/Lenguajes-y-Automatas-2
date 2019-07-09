#Nombre: Circunferencia.py
#Objetivo: calcula el área y diamétro  de una circunferencia e importar libreria
#Autor: Mario Rubén Mancilla Tinoco
#Fecha: 01 de julio 2019

import math as math
import os

#------------------------------------------------------------------------------------
#Función para calcular Área
def calculaArea(radio):
	area = math.pi*(math.pow(radio, 2))
	return area

#Función para calcular Diamétro
def calculaDiametro(radio):
	diametro = radio * 2
	return diametro

#Función principal
def main():
	ciclo = True
	while ciclo == True:
		print ("---Script para calcular Área de una circunferencia---")
		radio = float(input("Introduce  el valor del radio: "))
		#Invocar un metodo
		print("El area es: ", calculaArea(radio))
		print("EL diamétro es: ", calculaDiametro(radio))

		resp = input("Desea hacer otro calculo? s/n: ")
		if(resp == "s" or resp == "S"):
			ciclo = True
			os.system('cls')
		else:
			ciclo = False


if __name__ == '__main__':
	main()