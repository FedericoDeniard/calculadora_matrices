# Desarrollar un programa que sea capaz de multiplicar dos matrices ingresadas por el usuario.
# Validar las dimensiones de cada una para que sea consistente con el procedimiento
'''
Nombre: Federico
Apellido: Deniard
'''

from Packages.Package_Arrays.Matrices import *
from Packages.Package_Input.Input import *

def print_array(operation: int):
    """ Recieves an array and prints a formatted version of it.

    Args:
        array (list): The array you want to print.

    """
    match operation:
        case 1:
            result = multiply_array()
            if result == []:
                message = f"Las matrices no se pueden multiplicar"
                print(message)
            else:    
                message = f"El producto de las dos matrices es:\n"
                print(message + show_array(result))
        case 2:
            result = sum_array()
            if result == []:
                message = f"Las matrices no se pueden sumar"
                print(message)
            else:
                message = f"La suma de las dos matrices es:\n"
                print(message + show_array(result))
        case 3:
            result = subtract_array()
            if result == []:
                message = f"Las matrices no se pueden restar"
                print(message)
            else:
                message = f"La resta de las dos matrices es:\n"
                print(message + show_array(result))
    system("pause")

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