"""
This module contains the functions for adding, editing, deleting, and displaying gustos.
"""

# Local Module Imports
import user_inputs as ui
from misc import clear_screen, continue_prompt, info, raise_err
import misc as m
from colors import C1, C2, CE
import colors as c


def display_gusto_details(gusto: str, gustos_dict: dict[str, list]) -> None:
    """Displays the details of a gusto.

    Args:
        gusto (str): the gusto to display
        gustos_dict (dict[str, list]): the dictionary of gustos
    """
    # Get the details of the gusto from the gustos dictionary
    description = gustos_dict[gusto][0]
    group_size = gustos_dict[gusto][1]
    meal_type = gustos_dict[gusto][2].capitalize()
    # Using ternary if-else statements to check if the value is None
    # If it is None, display "Any" instead of the value
    budget = f"₱{gustos_dict[gusto][3]:.2f}" if gustos_dict[gusto][3] != None else "Any"
    max_distance = (
        f"{gustos_dict[gusto][4]:.2f} meters"
        if gustos_dict[gusto][4] != None
        else "Any"
    )
    cuisine_type = (
        gustos_dict[gusto][5].capitalize() if gustos_dict[gusto][5] != None else "Any"
    )
    min_rating = gustos_dict[gusto][6] if gustos_dict[gusto][6] != None else "Any"

    # Display the details of the gusto
    print(f"  {C2}Gusto Label:{CE} {gusto}")
    print(f"  {C2}Description:{CE} {description}")
    print(f"  {C2}Number of People:{CE} {group_size}")
    print(f"  {C2}Meal Type:{CE} {meal_type}")
    print(f"  {C2}Budget:{CE} {budget}")
    print(f"  {C2}Maximum Distance from UPLB Gate:{CE} {max_distance}")
    print(f"  {C2}Cuisine Type:{CE} {cuisine_type}")
    print(f"  {C2}Minimum Rating:{CE} {min_rating}")


def view_gusto(gustos_dict: dict[str, list]) -> None:
    """Displays the details of a gusto.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos
    """

    # Raise an error if there are no gustos in the gustos dictionary
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

    # Prompt the user to enter the gusto to view
    # Raise an error if the gusto does not exist
    gusto = m.capitalize_words(input("  Enter gusto label: ").strip())
    if gusto not in gustos_dict:
        raise_err(f'Gusto "{gusto}" does not exist!')
        return
    clear_screen()

    # Display the details of the gusto
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


def ad_hoc_gusto() -> tuple[str, list]:
    """Prompts the user to enter the attributes of a gusto.

    Returns:
        tuple: a tuple containing the label and attributes of the gusto
    """
    clear_screen()
    print(
        "═══════════════════════════════════════════════════\n",
        f"          {C1}Get Reco/s from an Ad Hoc Gusto{CE}          \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )

    # Prompt the user to enter the attributes of the gusto
    info("* indicates optional fields, press [ENTER] to skip")
    group_size = ui.get_integer("  Enter number of people: ")
    meal_type = ui.get_meal_type("  Enter meal type (Breakfast, Lunch, or Dinner): ")
    budget = ui.get_float("  *Enter budget: ", False)
    max_distance = ui.get_float("  *Enter maximum distance from UPLB: ", False)
    ui.print_valid_cuisines()
    cuisine_type = ui.get_cuisine_type("  *Enter cuisine type: ", False)
    min_rating = ui.get_rating("  *Enter minimum rating (1-5): ", False)

    # Return a tuple containing the attributes of the gusto
    # None is used as a placeholder for the label and description
    return (
        None,
        [
            None,
            group_size,
            meal_type,
            budget,
            max_distance,
            cuisine_type,
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

    # Prompt the user to enter the attributes of the gusto
    info("* indicates optional fields, press [ENTER] to skip")
    label = m.capitalize_words(ui.get_string("  Enter label: "))
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

    # Add the gusto to the gustos dictionary
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

    # Raise an error if there are no gustos in the gustos dictionary
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

    # Prompt the user to enter the gusto to edit
    # Raise an error if the gusto does not exist
    label = m.capitalize_words(input("  Enter gusto label: "))
    if label not in gustos_dict:
        raise_err(f'Gusto "{label}" does not exist!')
        return gustos_dict

    # Setting previous_label to label to check if the label was changed
    # Get the details of the gusto from the gustos dictionary
    previous_label = label
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
    info('* indicates optional fields, type "Any" to skip')
    print("═══════════════════════════════════════════════════")

    # Prompt the user to enter the new attributes of the gusto
    label = m.capitalize_words(ui.edit_string("  Enter label: ", label))
    if label in gustos_dict and previous_label != label:
        raise_err(f'Gusto "{label}" already exists!')
        return gustos_dict
    description = ui.edit_string("  Enter description: ", description)
    group_size = ui.edit_integer("  Enter group size: ", group_size)
    meal_type = ui.edit_meal_type(
        "  Enter meal type (Breakfast, Lunch, or Dinner): ", meal_type
    )
    budget = ui.edit_float("  *Enter group budget: ", budget, False)
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

    # Update the details of the gusto in the gustos dictionary
    gustos_dict[label] = [
        description,
        group_size,
        meal_type,
        budget,
        max_distance,
        cuisine_type,
        min_rating,
    ]

    # Display a message depending on whether the label was changed or not
    if previous_label != label:
        info(f'Edited Gusto "{previous_label}" to "{label}"')
    else:
        info(f'Edited Gusto "{label}"')

    # Delete the old gusto if the label was changed
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
    # Raise an error if there are no gustos in the gustos dictionary
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

    # Prompt the user to enter the gusto to delete
    # Raise an error if the gusto does not exist
    label = m.capitalize_words(input("  Enter gusto label: "))
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

    # Ask the user to confirm the deletion of the gusto
    display_gusto_details(label, gustos_dict)
    print("═══════════════════════════════════════════════════")
    print(f"{c.RED}  Are you sure you want to delete {label}?{c.END}")
    print(f"  [Y] Yes")
    print(f"  [Any Key] No")
    choice = m.capitalize_words(input("  Enter choice: "))
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
    # Raise an error if there are no gustos in the gustos dictionary
    if not gustos_dict:
        raise_err("No gustos to display! Add a gusto!")
        return
    print(
        "═══════════════════════════════════════════════════\n",
        f"{C1}                       Gustos                     {CE}\n",
        "═══════════════════════════════════════════════════\n",
        f"{C2}{c.ITALIC}             Label              Description       {CE}\n",
        "───────────────────────────────────────────────────\n",
        sep="",
        end="",
    )
    # Loop through the gustos dictionary and display the gusto labels and descriptions
    for gusto in gustos_dict:
        # Truncate the label and description if they are too long
        label = gusto if len(gusto) <= 27 else gusto[:24] + "..."
        description = (
            gustos_dict[gusto][0]
            if len(gustos_dict[gusto][0]) <= 18
            else gustos_dict[gusto][0][:15] + "..."
        )
        print(f"  {label:<27}   {description:<41}  ")


def display_gustos(gustos_dict: dict[str, list]) -> None:
    """Displays the gustos in the gustos dictionary.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos
    """
    # Raise an error if there are no gustos in the gustos dictionary
    if not gustos_dict:
        raise_err("No gustos to display! Add a gusto!")
        return
    clear_screen()
    print(
        "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        f"{C1}                                                             Gustos                                                            {CE}\n",
        "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        f"{C2}{c.ITALIC}       Label                   Description              #     Meal Type      Budget      Distance         Cuisine       Rating  {CE}\n",
        "────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n",
        sep="",
        end="",
    )
    # Loop through the gustos dictionary and display the details of the gustos
    for gusto in gustos_dict:
        # Truncate the label and description if they are too long
        label = gusto if len(gusto) <= 16 else gusto[:13] + "..."
        description = (
            gustos_dict[gusto][0]
            if len(gustos_dict[gusto][0]) <= 31
            else gustos_dict[gusto][0][:29] + "..."
        )
        group_size = gustos_dict[gusto][1]
        meal_type = gustos_dict[gusto][2].capitalize()
        # Using ternary if-else statements to check if the value is None
        # If it is None, display "Any" instead of the value
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

        # Display the details of the gusto
        print(
            f"  {label:<16}   {description:<31}   {group_size:^3}   {meal_type:^11}   {budget:>10}   {max_distance:>10}   {cuisine_type:^16}   {min_rating:^6}  "
        )
    print(
        "════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════"
    )
