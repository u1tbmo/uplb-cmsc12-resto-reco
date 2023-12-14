"""
This module contains the functions for adding, editing, deleting, and displaying restos.
"""
# Local Module Imports
import user_inputs as ui
from misc import clear_screen, continue_prompt, info, raise_err
from colors import C1, C2, CE
import colors as c

# Global Variables / Constants
NAME_LENGTH = 16


def display_resto_details(resto: str, restos_dict: dict[str, list]) -> None:
    """Displays the details of a resto

    Args:
        resto (str): the resto
        restos_dict (dict[str, list]): the dictionary of restos
    """
    distance = restos_dict[resto][0]
    cuisine_type = ", ".join(restos_dict[resto][1])
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
    print(f"  Cost per Person: ₱{cost}")
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
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}View Resto{CE}                    \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    name = input("  Enter resto name: ").strip().upper()
    print("═══════════════════════════════════════════════════")
    if name not in restos_dict:
        raise_err(f"Resto {name} does not exist!")
        return
    clear_screen()
    print(
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}View Resto{CE}                    \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    display_resto_details(name, restos_dict)
    print("═══════════════════════════════════════════════════")
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
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}Add Resto{CE}                     \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    name = ui.get_string("  Enter name: ").upper()

    if name in restos_dict:
        raise_err(f"Resto {name} already exists.")
        return restos_dict
    elif len(name) > NAME_LENGTH:
        raise_err(f"Name cannot exceed {NAME_LENGTH} characters.")
        return restos_dict

    distance = ui.get_float("  Enter distance from UPLB gate (in meters): ")
    info("For cuisine/s and meal types, enter a comma-separated list of values.")
    ui.print_valid_cuisines()
    cuisine_type = ui.get_list_of_cuisine_types(
        "  Enter cuisine/s: "
    )
    meal_type = ui.get_list_of_meal_types("  Enter meal type/s (Breakfast, Lunch, and/or Dinner): ")
    cost = ui.get_float("  Enter typical cost of a meal (in pesos): ")
    rating = ui.get_rating("  Enter rating (1-5): ")
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
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}Edit Resto{CE}                    \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )

    name = input("  Enter resto name: ").strip().upper()
    previous_name = name

    if name not in restos_dict:
        raise_err(f'Resto "{name}" does not exist!')
        return restos_dict

    clear_screen()
    print(
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}Edit Resto{CE}                    \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )

    distance, cuisine_type, meal_type, cost, rating = restos_dict[name]

    display_resto_details(name, restos_dict)
    print("═══════════════════════════════════════════════════")
    info(f"Press [ENTER] to keep current value.")
    print("═══════════════════════════════════════════════════")

    name = ui.edit_string("  Enter name: ", name)
    name = name.upper()
    if name in restos_dict and previous_name != name:
        raise_err(f"Resto {name} already exists.")
        return restos_dict
    distance = ui.edit_float(
        "  Enter distance from UPLB gate (m): ", distance
    )
    info("For cuisine types and meal types, enter a comma-separated list of values.")
    ui.print_valid_cuisines()
    cuisine_type = ui.edit_list_of_cuisine_types(
        "  Enter cuisine type/s: ", cuisine_type
    )
    meal_type = ui.edit_list_of_meal_types(
        "  Enter meal type/s (Breakfast, Lunch, and/or Dinner): ", meal_type
    )
    cost = ui.edit_float("  Enter typical cost of a meal: ", cost)
    rating = ui.edit_rating("  Enter rating (1-5): ", rating)
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
        "═══════════════════════════════════════════════════\n",
        f"                    {C1}Delete Resto{CE}                   \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )

    name = input("  Enter resto name: ").strip().upper()
    print("═══════════════════════════════════════════════════")
    if name not in restos_dict:
        raise_err(f'Resto "{name}" does not exist!')
        return restos_dict
    clear_screen()
    print(
        "═══════════════════════════════════════════════════\n",
        f"                    {C1}Delete Resto{CE}                   \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    display_resto_details(name, restos_dict)
    print("═══════════════════════════════════════════════════")
    print(f"{c.RED}  Are you sure you want to delete {name}?{c.END}")
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
    """Displays the gusto labels and their descriptions.

    Args:
        restos_dict (dict[str, list]): the dictionary of gustos
    """
    if not restos_dict:
        raise_err("No restos to display! Add a resto!")
        clear_screen()
        return
    print(
        "═══════════════════════════════════════════════════\n",
        f"{C1}                       Restos                      {CE}\n",
        "═══════════════════════════════════════════════════\n",
        f"{C2}{c.ITALIC}        Name                   Cuisines            {CE}\n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    for resto in restos_dict:
        name = resto
        list_of_cuisines = restos_dict[resto][1]
        print(f"  {name:<16}   {list_of_cuisines[0] if len(list_of_cuisines) == 1 else "┬ "+list_of_cuisines[0]:<28}")
        for idx, cuisine in enumerate(list_of_cuisines[1:]):
            cuisine = f"├ {cuisine}" if idx != len(list_of_cuisines[1:]) - 1 else f"└ {cuisine}"
            print(f"  {'':<16}   {cuisine:<28}")


def display_restos(restos_dict: dict[str, list]) -> None:
    """Displays the gustos in the gustos dictionary.

    Args:
        restos_dict (dict[str, list]): the dictionary of gustos
    """
    if not restos_dict:
        raise_err("No restos to display! Add a resto!")
        clear_screen()
        return
    print(
        "═════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        f"{C1}                                                  Restos                                                {CE}\n",
        "═════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        f"{C2}{c.ITALIC}        Name           Distance         Cuisines               Meal Types              Cost      Rating  {CE}\n"
        "═════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    for resto in restos_dict:
        label = resto
        distance = f"{restos_dict[resto][0]:.2f}m"
        list_of_cuisines = restos_dict[resto][1]
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
        cost = f"₱{restos_dict[resto][3]:.2f}"
        rating = f"{restos_dict[resto][4]:.1f}"
        print(
            f"  {label:<16}   {distance:<12}   {list_of_cuisines[0] if len(list_of_cuisines) == 1 else "┬ "+list_of_cuisines[0]:<16}   {meal_types:<26}   {cost:>10}   {rating:^6}  "
        )
        for idx, cuisine in enumerate(list_of_cuisines[1:]):
            cuisine = f"├ {cuisine}" if idx != len(list_of_cuisines[1:]) - 1 else f"└ {cuisine}"
            filler = f""
            print(f"  {filler:<16}   {filler:<12}   {cuisine:<16}   {filler:<26}   {filler:>10}   {filler:^6}  ")
    print(
        "═════════════════════════════════════════════════════════════════════════════════════════════════════════"
    )
