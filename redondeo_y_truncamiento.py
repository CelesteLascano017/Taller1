def calcular_promedio():
    nota1 = int(input("Ingresa la nota 1:"))
    nota2 = int(input("Ingresa la nota 2:"))
    nota3 = int(input("Ingresa la nota 3:"))

    promedio = (nota1+nota2+nota3)/3

    print(f"Promedio: {promedio}")  

def menu():
    while True:
        print("Menu xdxd")
        print("1. Truncamiento")
        print("2. Redondeo")
        print("3. Salir")

def opcion_1():
    

def manejar_opcion(opcion):
    if opcion == "1":
        opcion_1()
    elif opcion == "2":
        opcion_2()
    elif opcion == "3":
        print("xdxd")
    else: 
        print ("no xdxd")

def main():
    while True:
        mostrar_menu()
        opcion = input("Opcion")
        manejar_opcion(opcion)

