#Nombre: listas.py
#Objetivo: muestra el funcionamiento de las listas en python
#Autor: Mario Rubén Mancilla Tinoco
#Fecha: 02 de junio del 2019

#Variable global lista
lista = []

#Funcion para agregar items a la lista
def agregarItem(dato):
	lista.append(dato)
	print("Se agrego el elemento: ", dato)

#Funcion para buscar un item
def buscarItem(dato):
	if(dato in lista):
		print("El dato ", dato, " se encuentra en la lista")
	else:
		print("El dato no se encuentra en la lista")

#Funcion para modificar un item
def modificarItem():
	print("Modificando")

#Funcion para imprimir los elementos de la lista
def imprimirLista():
	j = 1
	for i in lista:
		print("Item ", j, ": ", i)
		j+=1

#Funcion para borrar items de la lista
def eliminarItem(dato):
	if(dato in lista):
		lista.remove(dato)
		print("Item eliminado")
	else:
		print("Item no existe en la lista...")

#Funcion principal
def main():
	opc = 0
	while(opc != 6):
		print("-------------------------------------")
		print("---Script para trabajar con listas---")
		print("1.- Agregar elementos a la lista")
		print("2.- Buscar un elemento en la lista")
		print("3.- Modificar un elemento en la lista")
		print("4.- Eliminar un elemento de la lista")
		print("5.- Imprimir lista")
		print("6.- Salir")

		opc = int(input("ELija una opcion entre 1 y 5: "))
		print("-------------------------------------")

		if(opc == 1):
			agregar = input("Ingrese el elemento a agregar: ")
			agregarItem(agregar)
		elif(opc == 2):
			buscar = input("Que elemento quiere buscar?: ")
			buscarItem(buscar)
		elif(opc == 3):
			modi = input("Que elemento quiere modificar?: ")
			modificarItem(modi)
		elif(opc == 4):
			item = input("Que item desea eliminar?: ")
			eliminarItem(item)
		elif(opc == 5):
			imprimirLista()
		elif(opc == 6):
			print("Gracias por usar el programa")
		else:
			print("Opcion incorrecta")


if __name__ == '__main__':
	main()