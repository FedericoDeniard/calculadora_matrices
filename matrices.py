# Desarrollar un programa que sea capaz de multiplicar dos matrices ingresadas por el usuario.
# Validar las dimensiones de cada una para que sea consistente con el procedimiento
'''
Nombre: Federico
Apellido: Deniard
'''

from Packages.Package_Arrays.Matrices import *
from Packages.Package_Input.Input import *

def menu():
    run = True
    while run:
        option = get_int(message="1. Multiply 2 matrix\n2. Sum 2 matrix\n3. Subtract 2 matrix\n4. Exit\nChoose an operation: ",min=1,max=4)
        match option:
            case 4:
                run = False
            case _:
                print_array(option)
        system("cls")
menu()