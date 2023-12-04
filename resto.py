"""
This module contains the functions for adding, editing, deleting, and displaying restos.
"""
# File Imports
from misc import clear_screen, continue_prompt, info, raise_er
from colors import C1, C2, CE

# Global Variables / Constants
NAME_LENGTH = 16


def add_restos(restos_dict: dict[str, list]) -> dict[str, list]:
    """Adds a resto to the restos dictionary.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos

    Returns:
        dict[str, list]: the updated dictionary of restos that includes the new resto
    """
    clear_screen()
    print(
        "---------------------------------------------------\n",
        f"                     {C1}Add Resto{CE}                     \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    name = input("  Name: ").strip().upper()
    print("--------------------------------------------")
    if "," in name:
        raise_er("Name cannot contain commas.")
        return restos_dict
    elif name == "":
        raise_er("Name cannot be empty.")
        return restos_dict
    elif name in restos_dict:
        raise_er(f"Resto {name} already exists.")
        return restos_dict
    elif len(name) > NAME_LENGTH:
        raise_er(f"Name cannot exceed {NAME_LENGTH} characters.")
        return restos_dict
    else:
        distance = input("  Enter distance from UPLB gate (in meters): ").strip()
        if distance == "":
            raise_er("Distance cannot be empty.")
            return restos_dict
        elif not distance.replace(".", "", 1).isdigit():
            raise_er("Invalid distance.")
            return restos_dict
        distance = float(distance)
        if distance <= 0:
            raise_er("Distance must be greater than 0.")
            return restos_dict
        cuisine_type = input("  Enter cuisine type: ").strip().upper()
        if "," in cuisine_type:
            raise_er("Cuisine type cannot contain commas.")
            return restos_dict
        elif cuisine_type == "":
            raise_er("Cuisine type cannot be empty.")
            return restos_dict
        info('Press "Enter" if the Resto serves that meal type. Otherwise, enter "N".')
        meal_type = ""
        if input("  [Enter/N] This resto serves breakfast. > ").strip().lower() != "n":
            meal_type += "B"
        if input("  [Enter/N] This resto serves lunch. > ").strip().lower() != "n":
            meal_type += "L"
        if input("  [Enter/N] This resto serves dinner. > ").strip().lower() != "n":
            meal_type += "D"
        if meal_type == "":
            raise_er("Resto must serve at least one meal type.")
            return restos_dict
        cost = input("  Enter typical cost of a meal (in pesos): ").strip()
        if cost == "":
            raise_er("Cost cannot be empty.")
            return restos_dict
        elif not cost.replace(".", "", 1).isdigit():
            raise_er("Invalid cost.")
            return restos_dict
        cost = float(cost)
        if cost <= 0:
            raise_er("Cost must be greater than 0.")
            return restos_dict
        rating = input("  Enter rating (out of 5): ").strip()
        if rating == "":
            raise_er("Rating cannot be empty.")
            return restos_dict
        elif not rating.replace(".", "", 1).isdigit():
            raise_er("Invalid rating.")
            return restos_dict
        rating = float(rating)
        if rating > 5 or rating < 0:
            raise_er("Rating must be between 0 and 5.")
            return restos_dict
        restos_dict[name] = [distance, cuisine_type, meal_type, cost, rating]
        info(f'Added Resto "{name}"')
        continue_prompt()
        return restos_dict


def edit_restos(restos_dict: dict[str, list]) -> dict[str, list]:
    """Edits a resto in the restos dictionary.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos

    Returns:
        dict[str, list]: the updated dictionary of restos which has the resto edited
    """
    if not restos_dict:
        raise_er("No restos to edit. Add a resto!")
        return restos_dict
    clear_screen()
    display_restos_simple(restos_dict)
    print(
        "---------------------------------------------------\n",
        f"                     {C1}Edit Resto{CE}                    \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    name = input("  Name: ").strip().upper()
    previous_name = name
    print("--------------------------------------------")
    if "," in name or name == "":
        raise_er("Invalid name!")
        return restos_dict
    elif name not in restos_dict:
        raise_er(f"Resto {name} does not exist!")
        return restos_dict
    else:
        clear_screen()
        print(
            "---------------------------------------------------\n",
            f"                     {C1}Edit Resto{CE}                    \n",
            "---------------------------------------------------\n",
            sep="",
            end="",
        )
        info(f"Fetched Resto {name}!")
        print("--------------------------------------------")
        value = restos_dict[name]
        meal_types = ""
        for char in value[2]:
            if char == "B":
                meal_types += "Breakfast, "
            elif char == "L":
                meal_types += "Lunch, "
            elif char == "D":
                meal_types += "Dinner, "
        meal_types = meal_types.rstrip(", ")
        print(f"  Name: {name}")
        print(f"  Distance from UPLB gate: {restos_dict[name][0]} meters")
        print(f"  Cuisine Type: {restos_dict[name][1]}")
        print(f"  Meal Types: {meal_types}")
        print(f"  Cost: {restos_dict[name][3]} pesos")
        print(f"  Rating: {restos_dict[name][4]}")
        print("--------------------------------------------")
        name = input("  Edit name: ").strip().upper()
        if "," in name:
            raise_er("Name cannot contain commas.")
            return restos_dict
        elif name == "":
            raise_er("Name cannot be empty.")
            return restos_dict
        elif name in restos_dict and previous_name != name:
            raise_er(f"Resto {name} already exists.")
            return restos_dict
        distance = input("  Edit distance from UPLB gate (in meters): ").strip()
        if distance == "":
            raise_er("Distance cannot be empty.")
            return restos_dict
        elif not distance.replace(".", "", 1).isdigit():
            raise_er("Invalid distance.")
            return restos_dict
        distance = float(distance)
        if distance <= 0:
            raise_er("Distance must be greater than 0.")
            return restos_dict
        cuisine_type = input("  Edit cuisine type: ").strip().upper()
        if "," in cuisine_type:
            raise_er("Cuisine type cannot contain commas.")
            return restos_dict
        elif cuisine_type == "":
            raise_er("Cuisine type cannot be empty.")
            return restos_dict
        info('Press "Enter" if the Resto serves that meal type. Otherwise, enter "N".')
        meal_type = ""
        if input("  [Enter/N] This resto serves breakfast. > ").strip().lower() != "n":
            meal_type += "B"
        if input("  [Enter/N] This resto serves lunch. > ").strip().lower() != "n":
            meal_type += "L"
        if input("  [Enter/N] This resto serves dinner. > ").strip().lower() != "n":
            meal_type += "D"
        if meal_type == "":
            raise_er("Resto must serve at least one meal type.")
            return restos_dict
        cost = input("  Edit typical cost of a meal (in pesos): ").strip()
        if cost == "":
            raise_er("Cost cannot be empty.")
            return restos_dict
        elif not cost.replace(".", "", 1).isdigit():
            raise_er("Invalid cost.")
            return restos_dict
        cost = float(cost)
        if cost <= 0:
            raise_er("Cost must be greater than 0.")
            return restos_dict
        rating = input("  Edit rating (out of 5): ").strip()
        if rating == "":
            raise_er("Rating cannot be empty.")
            return restos_dict
        elif not rating.replace(".", "", 1).isdigit():
            raise_er("Invalid rating.")
            return restos_dict
        rating = float(rating)
        if rating > 5 or rating < 0:
            raise_er("Rating must be between 0 and 5.")
            return restos_dict
        if previous_name != name:
            del restos_dict[previous_name]
        restos_dict[name] = [distance, cuisine_type, meal_type, cost, rating]
        if previous_name != name:
            info(f'Edited Resto "{previous_name} to {name}"')
        else:
            info(f'Edited Resto "{name}"')
        continue_prompt()
        return restos_dict


def delete_restos(restos_dict: dict[str, list]) -> dict[str, list]:
    """Deletes a resto from the restos dictionary.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos

    Returns:
        dict[str, list]: the updated dictionary of restos which has the resto deleted
    """
    if not restos_dict:
        raise_er("No restos to delete. Add a resto!")
        return restos_dict
    clear_screen()
    display_restos_simple(restos_dict)
    print(
        "---------------------------------------------------\n",
        f"                    {C1}Delete Resto{CE}                   \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    name = input("  Enter name: ").strip().upper()
    print("--------------------------------------------")
    if "," in name or name == "":
        raise_er("Invalid name!")
        return restos_dict
    elif name not in restos_dict:
        raise_er(f"Resto {name} does not exist!")
        return restos_dict
    else:
        clear_screen()
        print(
            "---------------------------------------------------\n",
            f"                    {C1}Delete Resto{CE}                   \n",
            "---------------------------------------------------\n",
            sep="",
            end="",
        )
        info(f"Fetched Resto {name}!")
        print("--------------------------------------------")
        value = restos_dict[name]
        meal_types = ""
        for char in value[2]:
            if char == "B":
                meal_types += "Breakfast, "
            elif char == "L":
                meal_types += "Lunch, "
            elif char == "D":
                meal_types += "Dinner, "
        meal_types = meal_types.rstrip(", ")
        print(f"  Name: {name}")
        print(f"  Distance from UPLB gate: {restos_dict[name][0]} meters")
        print(f"  Cuisine Type: {restos_dict[name][1]}")
        print(f"  Meal Types: {meal_types}")
        print(f"  Cost: {restos_dict[name][3]} pesos")
        print(f"  Rating: {restos_dict[name][4]}")
        print("--------------------------------------------")
        print(f'  Are you sure you want to delete "{name}"?')
        print("  [Y] Yes")
        print("  [Any Key] No")
        choice = input("  Enter choice: ").upper()
        if choice == "Y":
            del restos_dict[name]
            info(f'Deleted Resto "{name}"')
            continue_prompt()
        else:
            info(f'Canceled. Expected "Y", got "{choice}"')
            continue_prompt()
    return restos_dict


def display_restos_simple(restos_dict: dict[str, list]) -> None:
    """Displays the restos in the restos dictionary.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos
    """
    if not restos_dict:
        raise_er("No restos to display. Add a resto!")
        return
    print(
        "---------------------------------------------------\n",
        f"                       {C1}Restos{CE}                      \n",
        "---------------------------------------------------\n",
        f"{C2}        Name                    Cuisine            {CE}\n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    for name, value in restos_dict.items():
        print(f"  {name:>16}   {value[1].capitalize():<28}  ")
    print("---------------------------------------------------")


def display_restos_detailed(restos_dict: dict[str, list]) -> None:
    """Displays the restos in the restos dictionary with more detail.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos
    """
    if not restos_dict:
        raise_er("No restos to display. Add a resto!")
        return
    print(
        "-------------------------------------------------------------------------------------------------------------------\n",
        f"                                                      {C1}Restos{CE}                                                       \n",
        "-------------------------------------------------------------------------------------------------------------------\n",
        f"{C2}        Name         Distance from UPLB Gate      Cuisine             Meal Types             Cost        Rating    {CE}\n",
        "-------------------------------------------------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    for name, value in restos_dict.items():
        meal_types = ""
        for choice in value[2]:
            if choice == "B":
                meal_types += "Breakfast, "
            elif choice == "L":
                meal_types += "Lunch, "
            elif choice == "D":
                meal_types += "Dinner, "
        meal_types = meal_types.rstrip(", ")
        print(
            f"  {name:<16}   {value[0]:>22.2f}m   {value[1].capitalize():<13}   {meal_types:<24}   {value[3]:>10.2f}   {value[4]:^10.1f}  "
        )
    print(
        "-------------------------------------------------------------------------------------------------------------------"
    )
