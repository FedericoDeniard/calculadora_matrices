from Packages.Package_Input.Input import *
from os import system

def new_array() -> list:
    """Asks how many rows and colums are in the array, in order to set them.

    Returns:
        list: returns a list with the array.
    """
    rows = get_int("Ingrese la cantidad de filas del array: ")
    columns = get_int("Ingrese la cantidad de columnas del array: ")
    array = [[f"x{i}{j}" for j in range(1, columns + 1)] for i in range(1, rows + 1)]
    for i in range(len(array)):
        for j in range(len(array[0])):
            system("cls")
            print(show_array(array))
            array[i][j] = get_int(f"Ingrese el valor de la posicion x{i+1}{j+1}: ")



    return array


def can_multiply(A: list, B: list) -> bool:
    """Checks if the arrays can be multiplied

    Args:
        A (list): First array
        B (list): Second array

    Returns:
        bool: returns True if can be multiplied, False otherwise
    """
    columns_A = len(A[0])
    rows_B = len(B)
    validate = False
    if columns_A == rows_B:
        validate = True
    return validate

def multiply_matrix(A: list, B: list) -> list:
    """Multiplies 2 arrays without caring about validation

    Args:
        A (list): First Array
        B (list): Second Array

    Returns:
        str: Returns the result formatted between A and B
    """

    rows_A = len(A)
    columns_B = len(B[0])
    C = [[0]*columns_B for _ in range(rows_A)]
    
    for i in range(len(C)): # Recorremos las filas de C
        for j in range(len(C[0])): # Recorremos las columnas de C
            actual_cell = 0
            for k in range(len(A[0])): # Recorremos las columnas de A
                valor_A = A[i][k]   # Cambiamos de columna
                valor_B = B[k][j]   # Cambiamos de fila
                multiplicacion = valor_A * valor_B
                actual_cell += multiplicacion
            C[i][j] = actual_cell

    return C

def sum_array() -> list:
    print("Primera matriz")
    A = new_array()
    system("cls")
    print("Segunda matriz")
    B = new_array()
    system("cls")
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        C = [[f"x{i}{j}" for j in range(1, len(A[0]) + 1)] for i in range(1, len(A) + 1)]
        for i in range(len(C)):
            for j in range(len(C[0])):
                C[i][j] = A[i][j] + B[i][j]
    else:
        C = []
    return C

def subtract_array() -> list:
    print("Primera matriz")
    A = new_array()
    system("cls")
    print("Segunda matriz")
    B = new_array()
    system("cls")
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        C = [[f"x{i}{j}" for j in range(1, len(A[0]) + 1)] for i in range(1, len(A) + 1)]
        for i in range(len(C)):
            for j in range(len(C[0])):
                C[i][j] = A[i][j] - B[i][j]
    else:
        C = []
    return C


def multiply_array() -> list:
    """ Calls other array methods and if succesfull, returns the product between, otherwise, returns an empty array.

    Returns:
        list: _description_
    """
    print("Primera matriz")
    A = new_array()
    system("cls")
    print("Segunda matriz")
    B = new_array()
    system("cls")
    if  can_multiply(A,B):
        result = multiply_matrix(A,B)
    else:
        result = []
    return result

def show_array(array: list):
    """ Recieves an array and prints a formatted version of it.

    Args:
        array (list): The array you want to print.

    """
    message = "[ "
    for i in range(len(array)):
        for j in range(len(array[i])):
            message += f"{array[i][j]} "
        if i == len(array) - 1:
            message += "]"
        else:
            message += "\n  "
    return message