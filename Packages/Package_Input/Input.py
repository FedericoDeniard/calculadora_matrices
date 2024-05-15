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