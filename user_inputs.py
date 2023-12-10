"""
This module contains functions for getting user inputs and validating them.
"""

# Local Module Imports
from misc import raise_err, info


def get_string(prompt: str, optional: bool = False) -> tuple[bool, str]:
    """Gets a string input from the user.

    Args:
        prompt (str): the prompt to be displayed
        optional (bool): specifies if the input is optional

    Returns:
        tuple[bool, str]: the success state and the input
    """
    user_input = input(prompt).strip()
    if user_input:
        return True, user_input
    elif optional:
        info("Set to ANY!")
        return True, "ANY"
    elif "," in user_input:
        raise_err("Input cannot contain commas!")
        return False, ""
    else:
        raise_err("Input cannot be empty!")
        return False, ""


def get_positive_int(prompt: str) -> tuple[bool, int]:
    """Gets a positive integer input from the user.

    Args:
        prompt (str): the prompt to be displayed
        optional (bool): specifies if the input is optional

    Returns:
        tuple[bool, int]: the success state and the input
    """
    user_input = input(prompt)
    if not user_input.isdigit():
        raise_err("Input must be a positive number!")
        return False, 0
    elif int(user_input) <= 0:
        raise_err("Input must be greater than 0!")
        return False, 0
    else:
        return True, int(user_input)


def get_positive_float(prompt: str, optional: bool = False) -> tuple[bool, float]:
    """Gets a positive float input from the user.

    Args:
        prompt (str): the prompt to be displayed
        optional (bool): specifies if the input is optional

    Returns:
        tuple[bool, float]: the success state and the input
    """
    user_input = input(prompt)
    if user_input:
        return True, float(user_input)
    if not user_input and optional:
        info("Set to ANY!")
        return True, -1
    if not user_input.replace(".", "", 1).isdigit():
        raise_err("Input must be a positive number!")
        return False, 0.0
    elif float(user_input) <= 0:
        raise_err("Input must be greater than 0!")
        return False, 0.0


def get_valid_meal_type(prompt: str) -> tuple[bool, str]:
    """Gets a valid meal type input from the user.

    Args:
        prompt (str): the prompt to be displayed

    Returns:
        tuple[bool, str]: the success state and the input
    """
    user_input = input(prompt)
    if user_input.upper().strip() in ["BREAKFAST", "LUNCH", "DINNER"]:
        return True, user_input.upper().strip()
    else:
        raise_err("Input must be Breakfast, Lunch, or Dinner!")
        return False, ""


def get_valid_rating(prompt: str, optional: bool = False) -> tuple[bool, int]:
    """Gets a valid rating input from the user.

    Args:
        prompt (str): the prompt to be displayed
        optional (bool): specifies if the input is optional

    Returns:
        tuple[bool, int]: the success state and the input
    """
    user_input = input(prompt)
    if user_input:
        return True, int(user_input)
    elif not user_input and optional:
        info("Set to ANY!")
        return True, -1
    if not user_input.isdigit():
        raise_err("Input must be an integer between 1 and 5!")
        return False, 0
    elif int(user_input) < 1 or int(user_input) > 5:
        raise_err("Input must be an integer between 1 and 5!")
        return False, 0


def edit_string(
    prompt: str, existing_value: str, optional: bool = False
) -> tuple[bool, str]:
    """Edits a string input from the user.

    Args:
        prompt (str): the prompt to be displayed
        existing_value (str): the existing value to return if the input is empty
        optional (bool): specifies if the input is optional

    Returns:
        tuple[bool, str]: the success state and the input or the existing value
    """
    user_input = input(prompt).strip()
    if "," in user_input:
        raise_err("Input cannot contain commas!")
        return False, ""
    elif user_input.upper() == "REMOVE" and optional:
        info(f'Removing value: {existing_value if existing_value != "ANY" else "ANY"}')
        return True, "ANY"
    elif user_input.upper() == "REMOVE" and not optional:
        raise_err("You cannot remove a required input!")
        return False, ""
    elif not user_input:
        info(f'Keeping value: {existing_value if existing_value != "ANY" else "ANY"}')
        return True, existing_value
    elif user_input:
        return True, user_input


def edit_positive_int(prompt: str, existing_value: int) -> tuple[bool, int]:
    """Edits a positive integer input from the user.

    Args:
        prompt (str): the prompt to be displayed
        existing_value (int): the existing value to return if the input is empty

    Returns:
        tuple[bool, int]: the success state and the input or the existing value
    """
    user_input = input(prompt)
    if not user_input:
        info(f'Keeping value: {existing_value if existing_value != -1 else "ANY"}')
        return True, existing_value
    elif not user_input.isdigit():
        raise_err("Input must be a positive number!")
        return False, 0
    elif int(user_input) <= 0:
        raise_err("Input must be greater than 0!")
        return False, 0
    else:
        return True, int(user_input)


def edit_positive_float(
    prompt: str, existing_value: float, optional: bool = False
) -> tuple[bool, float] | str:
    """Edits a positive float input from the user.

    Args:
        prompt (str): the prompt to be displayed
        existing_value (float): the existing value to return if the input is empty
        optional (bool): specifies if the input is optional

    Returns:
        tuple[bool, float]: the success state and the input or the existing value
    """
    user_input = input(prompt)
    if not user_input:
        info(f'Keeping value: {existing_value if existing_value != -1 else "ANY"}')
        return True, existing_value
    elif user_input.upper() == "ANY" and optional:
        info(f'Removing value: {existing_value if existing_value != -1 else "ANY"}')
        return True, -1
    elif user_input.upper() == "ANY" and not optional:
        raise_err("You cannot remove a required input!")
        return False, 0.0
    elif float(user_input) <= 0:
        raise_err("Input must be greater than 0!")
        return False, 0.0
    elif not user_input.replace(".", "", 1).isdigit():
        raise_err("Input must be a positive number!")
        return False, 0.0
    elif user_input:
        return True, float(user_input)


def edit_valid_meal_type(prompt: str, existing_value: str) -> tuple[bool, str]:
    """Edits a valid meal type input from the user.

    Args:
        prompt (str): the prompt to be displayed
        existing_value (str): the existing value to return if the input is empty

    Returns:
        tuple[bool, str]: the success state and the input or the existing value
    """
    user_input = input(prompt).strip()
    if not user_input:
        info(f'Keeping value: {existing_value if existing_value != -1 else "ANY"}')
        return True, existing_value
    elif user_input.upper().strip() in ["BREAKFAST", "LUNCH", "DINNER"]:
        return True, user_input.upper()
    else:
        raise_err("Input must be Breakfast, Lunch, or Dinner!")
        return False, ""


def edit_valid_rating(
    prompt: str, existing_value: float, optional: bool = False
) -> tuple[bool, int | str]:
    """Edits a valid rating input from the user.

    Args:
        prompt (str): the prompt to be displayed
        existing_value (int): the existing value to return if the input is empty
        optional (bool): specifies if the input is optional

    Returns:
        tuple[bool, int]: the success state and the input or the existing value
    """
    user_input = input(prompt)
    if not user_input:
        info(f'Keeping value: {existing_value if existing_value != -1 else "ANY"}')
        return True, existing_value
    elif user_input.upper() == "ANY" and optional:
        info(f'Removing value: {existing_value if existing_value != -1 else "ANY"}')
        return True, -1
    elif user_input.upper() == "ANY" and not optional:
        raise_err("You cannot remove a required input!")
        return False, 0.0
    elif not user_input.replace(".", "", 1).isdigit():
        raise_err("Input must be a positive number!")
        return False, 0.0
    elif int(user_input) < 1 or int(user_input) > 5:
        raise_err("Input must be between 1 and 5!")
        return False, 0.0
    elif user_input:
        return True, int(user_input)
