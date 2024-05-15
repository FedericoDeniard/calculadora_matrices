from Packages.Package_Input.Validate import *
from os import system

def get_int(message: str, error_message = "Error", attempts = 0, min = True, max = True,) -> int|None:
    """Obtains an integer from the user.

    Args:
        message (str): The prompt for user input.
        error_message (str): The error message to display if validation fails.
        min (int): The minimum value for the number's range. (Optional)
        max (int): The maximum value for the number's range. (Optional)
        attempts (int): The number of attempts allowed for user input. (Optional)

    Returns:
        int|None: Returns an interger if succesfull, or None otherwise.
    """
    attempt = 1
    number = input(message)
    number = int(number)
    while not validate_number(number=number, min=min, max=max):
        if attempt == attempts:
            number = None
            break
        print(error_message)
        system("pause")
        system("cls")
        number = input(message)
        number = int(number)
        attempt +=1
        
    return number


def get_float(message: str, error_message: str,  attempts = 0, min = True, max = True) -> float|None:
    """Obtains a float from the user

    Args:
        message (str): The prompt for user input.
        error_message (str): The error message to display if validation fails.
        min (float): The minimum value for the number's range. (Optional)
        max (float): The maximum value for the number's range. (Optional)
        attempts (float): The number of attempts allowed for user input. (Optional)

    Returns:
        float|None: Returns a float if succesfull, or None otherwise.
    """
    attempt = 1
    number = input(message)
    number = float(number)
    while not validate_number(number=number, min=min, max=max):
        if attempt == attempts:
            number = None
            break
        else:
            pass
        print(error_message)
        number = input(message)
        number = float(number)
        attempt +=1
        
    return number

def get_string( message: str, max_length = True , min_length = True) -> str:
    """Obtains a string from the user

    Args:
        message (str): The prompt for user input.
        max_length (int): Maximum length of the string. (Optional)

    Returns:
        str|None: Returns a string.
    """
    text = input(message)
    if type(max_length) == int or (max_length) == int:
        while not check_max_length(max_length, text) or not check_min_length(min_length,text):
            if type(min_length) == int and type(max_length) == int:
                print(f"El texto debe tener por lo menos {min_length} caracteres y {max_length} como maximo")
            elif type(min_length) == int:
                print(f"El texto debe tener por lo menos {min_length} caracteres")
            else:
                print(f"El texto debe tener {max_length} como maximo")
            text = input(message)
    return text


def get_max_number(list: list) -> int:
    """Returns de max value from a list

    Args:
        list (list): The array of numbers you are going to compare

    Returns:
        int: The max value
    """
    number = 0
    for i in range(len(list)):
        if list[i] > number or i == 1:
            number = list[i]
    return number