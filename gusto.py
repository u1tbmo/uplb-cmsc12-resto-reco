"""
This module contains the functions for adding, editing, deleting, and displaying gustos.
"""

# Local Module Imports
import user_inputs as ui
from misc import clear_screen, continue_prompt, info, raise_err
from colors import C1, C2, CE
import colors as c

# Global Variables / Constants
LABEL_LENGTH = 10


def display_gusto_details(gusto: str, gustos_dict: dict[str, list]) -> None:
    """Displays the details of a gusto.

    Args:
        gusto (str): the gusto to display
        gustos_dict (dict[str, list]): the dictionary of gustos
    """
    description = gustos_dict[gusto][0]
    group_size = gustos_dict[gusto][1]
    meal_type = gustos_dict[gusto][2].capitalize()
    budget = f"₱{gustos_dict[gusto][3]}" if gustos_dict[gusto][3] != None else "Any"
    max_distance = (
        f"{gustos_dict[gusto][4]} meters" if gustos_dict[gusto][4] != None else "Any"
    )
    cuisine_type = (
        gustos_dict[gusto][5].capitalize() if gustos_dict[gusto][5] != None else "Any"
    )
    min_rating = gustos_dict[gusto][6] if gustos_dict[gusto][6] != None else "Any"
    print(f"  Gusto Label: {gusto}")
    print(f"  Description: {description}")
    print(f"  Number of People: {group_size}")
    print(f"  Meal Type: {meal_type}")
    print(f"  Budget: {budget}")
    print(f"  Maximum Distance from UPLB Gate: {max_distance}")
    print(f"  Cuisine Type: {cuisine_type}")
    print(f"  Minimum Rating: {min_rating}")


def view_gusto(gustos_dict: dict[str, list]) -> None:
    """Displays the details of a gusto.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos
    """
    if not gustos_dict:
        raise_err("No gustos to view! Add a gusto!")
        return
    clear_screen()
    display_gustos_simple(gustos_dict)
    print(
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}View Gusto{CE}                     \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    gusto = input("  Enter gusto label: ").strip().upper()
    if gusto not in gustos_dict:
        raise_err(f'Gusto "{gusto}" does not exist!')
        return
    clear_screen()
    print(
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}View Gusto{CE}                     \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    display_gusto_details(gusto, gustos_dict)
    print("═══════════════════════════════════════════════════")
    continue_prompt()


def ad_hoc_gusto() -> tuple[str, list] | None:
    """Prompts the user to enter the attributes of a gusto.

    Returns:
        tuple | None: a tuple containing the label and attributes of the gusto
    """
    clear_screen()
    print(
        "═══════════════════════════════════════════════════\n",
        f"          {C1}Get Reco/s from an Ad Hoc Gusto{CE}          \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    info("* indicates optional fields")
    group_size = ui.get_integer("  Enter number of people: ")
    meal_type = ui.get_meal_type("  Enter meal type (Breakfast, Lunch, or Dinner): ")
    budget = ui.get_float("  *Enter budget: ", False)
    max_distance = ui.get_float("  *Enter maximum distance from UPLB: ", False)
    cuisine_type = ui.get_string("  *Enter cuisine type: ", False)
    min_rating = ui.get_rating("  *Enter minimum rating (1-5): ", False)

    return (
        None,
        [
            None,
            group_size,
            meal_type,
            budget,
            max_distance,
            cuisine_type.upper(),
            min_rating,
        ],
    )


def add_gustos(gustos_dict: dict[str, list]) -> dict[str, list]:
    """Adds a gusto to the gustos dictionary.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos

    Returns:
        dict[str, list]: the updated dictionary of gustos that includes the new gusto
    """
    clear_screen()
    print(
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}Add Gusto{CE}                     \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    info("* indicates optional fields")
    label = ui.get_string("  Enter label: ")
    label = label.upper()
    if len(label) > LABEL_LENGTH:
        raise_err(f"Label must be {LABEL_LENGTH} characters or less!")
        return gustos_dict
    if label in gustos_dict:
        raise_err(f'Gusto "{label}" already exists!')
        return gustos_dict
    description = ui.get_string("  Enter description: ")
    group_size = ui.get_integer("  Enter group size: ")
    meal_type = ui.get_meal_type("  Enter meal type (Breakfast, Lunch, or Dinner): ")
    budget = ui.get_float("  *Enter group budget: ", False)
    max_distance = ui.get_float("  *Enter maximum distance from UPLB Gate (m): ", False)
    ui.print_valid_cuisines()
    cuisine_type = ui.get_cuisine_type("  *Enter cuisine: ", False)
    min_rating = ui.get_rating("  *Enter minimum rating (1-5): ", False)
    gustos_dict[label] = [
        description,
        group_size,
        meal_type,
        budget,
        max_distance,
        cuisine_type,
        min_rating,
    ]
    info(f'Added Gusto "{label}"')
    continue_prompt()
    return gustos_dict


def edit_gustos(gustos_dict: dict[str, list]) -> dict[str, list]:
    """Edits a gusto in the gustos dictionary.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos

    Returns:
        dict[str, list]: the updated dictionary of gustos which has the gusto edited
    """
    if not gustos_dict:
        raise_err("No gustos to edit! Add a gusto!")
        return gustos_dict
    clear_screen()
    display_gustos_simple(gustos_dict)

    print(
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}Edit Gusto{CE}                    \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    label = input("  Enter gusto label: ").upper()
    if label not in gustos_dict:
        raise_err(f'Gusto "{label}" does not exist!')
        return gustos_dict
    previous_label = label.upper()
    (
        description,
        group_size,
        meal_type,
        budget,
        max_distance,
        cuisine_type,
        min_rating,
    ) = gustos_dict[label]
    clear_screen()
    print(
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}Edit Gusto{CE}                    \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    display_gusto_details(label, gustos_dict)
    print("═══════════════════════════════════════════════════")
    info("Press [ENTER] to keep current value.")
    info('Type "Any" to set a field to "Any"')
    info("* indicates optional fields")
    print("═══════════════════════════════════════════════════")
    label = ui.edit_string("  Enter label: ", label)
    label = label.upper()
    if label in gustos_dict and previous_label != label:
        raise_err(f'Gusto "{label}" already exists!')
        return gustos_dict
    if len(label) > LABEL_LENGTH:
        raise_err(f"Label must be {LABEL_LENGTH} characters or less!")
        return gustos_dict

    description = ui.edit_string("  Enter description: ", description)
    group_size = ui.edit_integer("  Enter group size: ", group_size)
    meal_type = ui.edit_meal_type(
        "  Enter meal type (Breakfast, Lunch, or Dinner): ", meal_type
    )
    budget = ui.edit_float("  *Enter group budget: ", budget, True)
    max_distance = ui.edit_float(
        "  *Enter maximum distance from UPLB Gate (m): ",
        max_distance,
        False,
    )
    ui.print_valid_cuisines()
    cuisine_type = ui.edit_cuisine_type(
        "  *Enter cuisine: ",
        cuisine_type,
        False,
    )
    min_rating = ui.edit_rating(
        "  *Enter minimum rating (1-5): ",
        min_rating,
        False,
    )
    gustos_dict[label] = [
        description,
        group_size,
        meal_type,
        budget,
        max_distance,
        cuisine_type,
        min_rating,
    ]
    if previous_label != label:
        info(f'Edited Gusto "{previous_label}" to "{label}"')
    else:
        info(f'Edited Gusto "{label}"')
    if label != previous_label:
        del gustos_dict[previous_label]
    continue_prompt()
    return gustos_dict


def delete_gustos(gustos_dict: dict[str, list]) -> dict[str, list]:
    """Deletes a gusto from the gustos dictionary.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos

    Returns:
        dict[str, list]: the updated dictionary of gustos which has the gusto deleted
    """
    if not gustos_dict:
        raise_err("No gustos to delete! Add a gusto!")
        return gustos_dict

    clear_screen()
    display_gustos_simple(gustos_dict)
    print(
        "═══════════════════════════════════════════════════\n",
        f"                    {C1}Delete Gusto{CE}                   \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    label = input("  Enter gusto label: ").upper()
    print("═══════════════════════════════════════════════════")
    if label not in gustos_dict:
        raise_err(f'Gusto "{label}" does not exist!')
        return gustos_dict
    clear_screen()
    print(
        "═══════════════════════════════════════════════════\n",
        f"                    {C1}Delete Gusto{CE}                   \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    display_gusto_details(label, gustos_dict)
    print("═══════════════════════════════════════════════════")
    print(f"{c.RED}  Are you sure you want to delete {label}?{c.END}")
    print(f"  [Y] Yes")
    print(f"  [Any Key] No")
    choice = input("  Enter choice: ").upper()
    if choice == "Y":
        del gustos_dict[label]
        info(f'Deleted Gusto "{label}"')
        continue_prompt()
    else:
        info(f'Canceled. Expected "Y", got "{choice}"')
        continue_prompt()

    return gustos_dict


def display_gustos_simple(gustos_dict: dict[str, list]) -> None:
    """Displays the gusto labels and their descriptions.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos
    """
    if not gustos_dict:
        raise_err("No gustos to display! Add a gusto!")
        clear_screen()
        return
    print(
        "═══════════════════════════════════════════════════\n",
        f"{C1}                       Gustos                      {CE}\n",
        "═══════════════════════════════════════════════════\n",
        f"{C2}{c.ITALIC}     Label                 Description             {CE}\n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    for gusto in gustos_dict:
        label = gusto
        description = (
            gustos_dict[gusto][0]
            if len(gustos_dict[gusto][0]) <= 33
            else gustos_dict[gusto][0][:30] + "..."
        )
        print(f"  {label:<10}   {description}  ")


def display_gustos(gustos_dict: dict[str, list]) -> None:
    """Displays the gustos in the gustos dictionary.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos
    """
    if not gustos_dict:
        raise_err("No gustos to display! Add a gusto!")
        clear_screen()
        return
    print(
        "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        f"{C1}                                                             Gustos                                                            {CE}\n",
        "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        f"{C2}{c.ITALIC}    Label                   Description                 #     Meal Type      Budget      Distance         Cuisine       Rating  {CE}\n",
        "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    for gusto in gustos_dict:
        label = gusto
        description = (
            gustos_dict[gusto][0]
            if len(gustos_dict[gusto][0]) <= 37
            else gustos_dict[gusto][0][:34] + "..."
        )
        group_size = gustos_dict[gusto][1]
        meal_type = gustos_dict[gusto][2].capitalize()
        budget = (
            f"₱{gustos_dict[gusto][3]:.2f}" if gustos_dict[gusto][3] != None else "Any"
        )
        max_distance = (
            f"{gustos_dict[gusto][4]:.2f}m" if gustos_dict[gusto][4] != None else "Any"
        )
        cuisine_type = (
            gustos_dict[gusto][5].capitalize()
            if gustos_dict[gusto][5] != None
            else "Any"
        )
        min_rating = (
            f"{gustos_dict[gusto][6]:.1f}" if gustos_dict[gusto][6] != None else "Any"
        )

        print(
            f"  {label:<10}   {description:<37}   {group_size:^3}   {meal_type:^11}   {budget:>10}   {max_distance:>10}   {cuisine_type:^16}   {min_rating:^6}  "
        )
    print(
        "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════"
    )
