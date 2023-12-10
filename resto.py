"""
This module contains the functions for adding, editing, deleting, and displaying restos.
"""
# Local Module Imports
import user_inputs as ui
from misc import clear_screen, continue_prompt, info, raise_err
from colors import C1, C2, CE

# Global Variables / Constants
NAME_LENGTH = 16


def display_resto_details(resto: str, restos_dict: dict[str, list]) -> None:
    """Displays the details of a resto

    Args:
        resto (str): the resto
        restos_dict (dict[str, list]): the dictionary of restos
    """
    distance = restos_dict[resto][0]
    cuisine_type = restos_dict[resto][1].capitalize()
    meal_type = restos_dict[resto][2]
    meal_types = ""
    for char in meal_type:
        if char == "B":
            meal_types += "Breakfast, "
        elif char == "L":
            meal_types += "Lunch, "
        elif char == "D":
            meal_types += "Dinner, "
    meal_types = meal_types.rstrip(", ")
    cost = restos_dict[resto][3]
    rating = restos_dict[resto][4]

    print(f"  Name: {resto}")
    print(f"  Distance from UPLB gate: {distance} meters")
    print(f"  Cuisine Type: {cuisine_type}")
    print(f"  Meal Types: {meal_types}")
    print(f"  Cost: {cost} pesos")
    print(f"  Rating: {rating}")


def view_resto(restos_dict: dict[str, list]) -> None:
    """Displays the details of a resto.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos
    """
    if not restos_dict:
        raise_err("No restos to view. Add a resto!")
        return
    clear_screen()
    display_restos_simple(restos_dict)
    print(
        "---------------------------------------------------\n",
        f"                     {C1}View Resto{CE}                    \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    success, name = ui.get_string("  Enter name: ")
    name = name.upper()
    print("---------------------------------------------------")

    if not success:
        return
    if name not in restos_dict:
        raise_err(f"Resto {name} does not exist!")
        return
    clear_screen()
    print(
        "---------------------------------------------------\n",
        f"                     {C1}View Resto{CE}                    \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    display_resto_details(name, restos_dict)
    print("---------------------------------------------------")
    continue_prompt()


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
    success, name = ui.get_string("  Enter name: ", False)
    name = name.upper()
    if not success:
        return restos_dict
    elif name in restos_dict:
        raise_err(f"Resto {name} already exists.")
        return restos_dict
    elif len(name) > NAME_LENGTH:
        raise_err(f"Name cannot exceed {NAME_LENGTH} characters.")
        return restos_dict

    success, distance = ui.get_positive_float(
        "  Enter distance from UPLB gate (in meters): "
    )
    if not success:
        return restos_dict

    success, cuisine_type = ui.get_string("  Enter cuisine type: ")
    cuisine_type = cuisine_type.upper()
    if not success:
        return restos_dict

    info("Press [ENTER] if the Resto serves that meal type. Otherwise, enter [N].")
    meal_type = ""
    if input("  This resto serves breakfast [Enter/N]: ").strip().upper() != "N":
        meal_type += "B"
    if input("  This resto serves lunch [Enter/N]: ").strip().upper() != "N":
        meal_type += "L"
    if input("  This resto serves dinner [Enter/N]: ").strip().upper() != "N":
        meal_type += "D"
    if meal_type == "":
        raise_err("Resto must serve at least one meal type.")
        return restos_dict

    success, cost = ui.get_positive_float("  Enter typical cost of a meal (in pesos): ")
    if not success:
        return restos_dict

    success, rating = ui.get_valid_rating("  Enter rating (1-5): ")
    if not success:
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
        raise_err("No restos to edit. Add a resto!")
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

    success, name = ui.get_string("  Enter name: ")
    name = name.upper()
    previous_name = name
    if not success:
        return restos_dict
    elif name not in restos_dict:
        raise_err(f"Resto {name} does not exist!")
        return restos_dict

    clear_screen()
    print(
        "---------------------------------------------------\n",
        f"                     {C1}Edit Resto{CE}                    \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )

    distance, cuisine_type, meal_type, cost, rating = restos_dict[name]

    display_resto_details(name, restos_dict)
    print("---------------------------------------------------")
    info(f"Press [ENTER] to keep current value.")
    print("---------------------------------------------------")

    success, name = ui.edit_string("  Edit name: ", name)
    name = name.upper()
    if not success:
        return restos_dict
    elif name in restos_dict and previous_name != name:
        raise_err(f"Resto {name} already exists.")
        return restos_dict

    success, distance = ui.edit_positive_float(
        "  Edit distance from UPLB gate (in meters): ", distance
    )
    if not success:
        return restos_dict

    success, cuisine_type = ui.edit_string("  Edit cuisine type: ", cuisine_type)
    cuisine_type = cuisine_type.upper()
    if not success:
        return restos_dict

    info('Press "Enter" if the Resto serves that meal type. Otherwise, enter "N".')
    meal_type = ""
    if input("  This resto serves breakfast [Enter/N]: ").strip().upper() != "N":
        meal_type += "B"
    if input("  This resto serves lunch [Enter/N]: ").strip().upper() != "N":
        meal_type += "L"
    if input("  This resto serves dinner [Enter/N]: ").strip().upper() != "N":
        meal_type += "D"
    if meal_type == "":
        raise_err("Resto must serve at least one meal type.")
        return restos_dict

    success, cost = ui.edit_positive_float(
        "  Edit typical cost of a meal (in pesos): ", cost
    )
    if not success:
        return restos_dict

    success, rating = ui.edit_valid_rating("  Edit rating (1-5): ", rating)
    if not success:
        return restos_dict

    restos_dict[name] = [distance, cuisine_type, meal_type, cost, rating]

    if previous_name != name:
        info(f'Edited Resto "{previous_name} to {name}"')
    else:
        info(f'Edited Resto "{name}"')

    if previous_name != name:
        del restos_dict[previous_name]

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
        raise_err("No restos to delete. Add a resto!")
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

    success, name = ui.get_string("  Enter name: ")
    name = name.upper()
    print("---------------------------------------------------")

    if not success:
        return restos_dict
    if name not in restos_dict:
        raise_err(f"Resto {name} does not exist!")
        return restos_dict
    clear_screen()
    print(
        "---------------------------------------------------\n",
        f"                    {C1}Delete Resto{CE}                   \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    display_resto_details(name, restos_dict)
    print("---------------------------------------------------")
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
        raise_err("No restos to display. Add a resto!")
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
        raise_err("No restos to display. Add a resto!")
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
        cost = f"₱{value[3]:.2f}"
        rating = f"{value[4]} / 5"
        print(
            f"  {name:<16}   {value[0]:>22.2f}m   {value[1].capitalize():^13}   {meal_types:<24}   {cost:>10}   {rating:^10}  "
        )
    print(
        "-------------------------------------------------------------------------------------------------------------------"
    )
