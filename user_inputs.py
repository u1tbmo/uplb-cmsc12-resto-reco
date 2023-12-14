"""
This module contains functions for getting user inputs and validating them.
"""

# Local Module Imports
from misc import print_err
import colors as c

# Global Variable
cuisines_list = [
    "None",
    "Filipino",
    "American",
    "Japanese",
    "Korean",
    "Indian",
    "Thai",
    "Chinese",
    "Malaysian",
    "Mediterranean",
    "Middle Eastern",
    "Italian",
    "French",
    "German",
    "British",
    "Spanish",
    "African",
]

meal_types_sorter = {
    "B": 0,
    "L": 1,
    "D": 2,
}


def print_valid_cuisines() -> None:
    print(
        "═══════════════════════════════════════════════════\n",
        f"{c.C1}                   Valid Cuisines                  {c.CE}\n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    for i in range(0, len(cuisines_list), 3):
        try:
            cuisine1 = cuisines_list[i]
            cuisine2 = cuisines_list[i + 1]
            cuisine3 = cuisines_list[i + 2]
        except IndexError:
            try:
                cuisine1 = cuisines_list[i]
                cuisine2 = cuisines_list[i + 1]
                cuisine3 = ""
            except IndexError:
                cuisine1 = cuisines_list[i]
                cuisine2 = ""
                cuisine3 = ""
        print(
            f"  {cuisine1:<14} {cuisine2:<14} {cuisine3:<14}  \n",
            sep="",
            end="",
        )
    print("═══════════════════════════════════════════════════")


def get_string(prompt: str, required: bool = True) -> str:
    while True:
        string = input(prompt).strip()
        if required and string == "":
            print_err("Input cannot be blank.")
            continue
        else:
            return string


def get_integer(prompt: str, required: bool = True) -> int:
    while True:
        integer = input(prompt).strip()
        if required and integer == "":
            print_err("Input cannot be blank.")
            continue
        elif not required and integer == "":
            return None
        try:
            integer = int(integer)
            if integer <= 0:
                print_err("Input must be greater than 0.")
                continue
            else:
                return integer
        except ValueError:
            print_err("Input must be an integer.")
            continue


def get_float(prompt: str, required: bool = True) -> float:
    while True:
        float_num = input(prompt).strip()
        if required and float_num == "":
            print_err("Input cannot be blank.")
            continue
        elif not required and float_num == "":
            return None
        try:
            float_num = float(float_num)
            if float_num <= 0:
                print_err("Input must be greater than 0.")
                continue
            else:
                return float_num
        except ValueError:
            print_err("Input must be a float.")
            continue


def get_meal_type(prompt: str, required: bool = True) -> str:
    while True:
        meal_type = input(prompt).strip().capitalize()
        if required and meal_type == "":
            print_err("Input cannot be blank.")
            continue
        elif not required and meal_type == "":
            return None
        elif meal_type not in ["Breakfast", "Lunch", "Dinner"]:
            print_err("Input must be either Breakfast, Lunch, or Dinner.")
            continue
        else:
            return meal_type


def get_list_of_meal_types(prompt: str, required: bool = True) -> str:
    while True:
        meal_types = input(prompt).strip()
        if required and meal_types == "":
            print_err("Input cannot be blank.")
            continue
        elif not required and meal_types == "":
            return None
        meal_type_lst = []
        for meal_type in meal_types.split(","):
            meal_type = meal_type.strip().capitalize()
            if meal_type in ["Breakfast", "Lunch", "Dinner"]:
                meal_type_lst.append(meal_type[0])
        if len(meal_type_lst) == 0:
            print_err("Input must have at least one valid meal type.")
            continue
        else:
            break
    meal_type_lst.sort(key=lambda x: meal_types_sorter[x])
    return "".join(meal_type_lst)


def get_cuisine_type(prompt: str, required: bool = True) -> str:
    while True:
        cuisine_type = input(prompt).strip().capitalize()
        if required and cuisine_type == "":
            print_err("Input cannot be blank.")
            continue
        elif not required and cuisine_type == "":
            return None
        elif cuisine_type not in cuisines_list:
            print_err("Input must be a valid cuisine type.")
            continue
        else:
            return cuisine_type


def get_list_of_cuisine_types(prompt: str, required: bool = True) -> str:
    while True:
        cuisine_types = input(prompt).strip()
        if required and cuisine_types == "":
            print_err("Input cannot be blank.")
            continue
        elif not required and cuisine_types == "":
            return None
        cuisine_type_list = []
        for cuisine_type in cuisine_types.split(","):
            cuisine_type = cuisine_type.strip().capitalize()
            if cuisine_type in cuisines_list:
                cuisine_type_list.append(cuisine_type)
        if len(cuisine_type_list) == 0:
            print_err("Input must have at least one valid cuisine type.")
            continue
        else:
            break
    return cuisine_type_list


def get_rating(prompt: str, required: bool = True) -> float:
    while True:
        rating = input(prompt).strip()
        if required and rating == "":
            print_err("Input cannot be blank.")
            continue
        elif not required and rating == "":
            return None
        try:
            rating = float(rating)
            if rating < 1 or rating > 5:
                print_err("Input must be between 1 and 5.")
                continue
            else:
                return rating
        except ValueError:
            print_err("Input must be a float.")
            continue


def edit_string(prompt: str, old_value: str, required: bool = True) -> str:
    while True:
        string = input(prompt).strip()
        if string == "":
            return old_value
        elif string.capitalize() == "Any" and not required:
            return None
        elif string.capitalize() == "Any" and required:
            print_err("Input is required.")
            continue
        else:
            return string


def edit_integer(prompt: str, old_value: int, required: bool = True) -> int:
    while True:
        integer = input(prompt).strip()
        if integer == "":
            return old_value
        elif integer.capitalize() == "Any" and not required:
            return None
        elif integer.capitalize() == "Any" and required:
            print_err("Input is required.")
            continue
        try:
            integer = int(integer)
            if integer <= 0:
                print_err("Input must be greater than 0.")
                continue
            else:
                return integer
        except ValueError:
            print_err("Input must be an integer.")
            continue


def edit_float(prompt: str, old_value: float, required: bool = True) -> float:
    while True:
        float_num = input(prompt).strip()
        if float_num == "":
            return old_value
        elif float_num.capitalize() == "Any" and not required:
            return None
        elif float_num.capitalize() == "Any" and required:
            print_err("Input is required.")
            continue
        try:
            float_num = float(float_num)
            if float_num <= 0:
                print_err("Input must be greater than 0.")
                continue
            else:
                return float_num
        except ValueError:
            print_err("Input must be a float.")
            continue


def edit_meal_type(prompt: str, old_value: str, required: bool = True) -> str:
    while True:
        meal_type = input(prompt).strip().capitalize()
        if meal_type == "":
            return old_value
        elif meal_type.capitalize() == "Any" and not required:
            return None
        elif meal_type.capitalize() == "Any" and required:
            print_err("Input is required.")
            continue
        elif meal_type not in ["Breakfast", "Lunch", "Dinner"]:
            print_err("Input must be either Breakfast, Lunch, or Dinner.")
            continue
        else:
            return meal_type


def edit_list_of_meal_types(prompt: str, old_value: str) -> str:
    while True:
        meal_types = input(prompt).strip()
        if meal_types == "":
            return old_value
        meal_type_lst = []
        for meal_type in meal_types.split(","):
            meal_type = meal_type.strip().capitalize()
            if meal_type in ["Breakfast", "Lunch", "Dinner"]:
                meal_type_lst.append(meal_type[0])
        if len(meal_type_lst) == 0:
            print_err("Input must have at least one valid meal type.")
            continue
        else:
            break
    meal_type_lst.sort(key=lambda x: meal_types_sorter[x])
    return "".join(meal_type_lst)


def edit_cuisine_type(prompt: str, old_value: str, required: bool = True) -> str:
    while True:
        cuisine_type = input(prompt).strip().capitalize()
        if cuisine_type == "":
            return old_value
        elif cuisine_type.capitalize() == "Any" and not required:
            return None
        elif cuisine_type.capitalize() == "Any" and required:
            print_err("Input is required.")
            continue
        elif cuisine_type not in cuisines_list:
            print_err("Input must be a valid cuisine type.")
            continue
        else:
            return cuisine_type


def edit_list_of_cuisine_types(prompt: str, old_value: str) -> str:
    while True:
        cuisine_types = input(prompt).strip()
        if cuisine_types == "":
            return old_value
        cuisine_type_list = []
        for cuisine_type in cuisine_types.split(","):
            cuisine_type = cuisine_type.strip().capitalize()
            if cuisine_type in cuisines_list:
                cuisine_type_list.append(cuisine_type)
        if len(cuisine_type_list) == 0:
            print_err("Input must have at least one valid cuisine type.")
            continue
        else:
            break
    return cuisine_type_list


def edit_rating(prompt: str, old_value: float, required: bool = True) -> float:
    while True:
        rating = input(prompt).strip()
        if rating == "":
            return old_value
        elif rating.capitalize() == "Any" and not required:
            return None
        elif rating.capitalize() == "Any" and required:
            print_err("Input is required.")
            continue
        try:
            rating = float(rating)
            if rating < 1 or rating > 5:
                print_err("Input must be between 1 and 5.")
                continue
            else:
                return rating
        except ValueError:
            print_err("Input must be a float.")
            continue
