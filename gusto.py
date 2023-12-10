"""
This module contains the functions for adding, editing, deleting, and displaying gustos.
"""

# Local Module Imports
import user_inputs as ui
from misc import clear_screen, continue_prompt, info, raise_err
from colors import C1, C2, CE

# Global Variables / Constants
LABEL_LENGTH = 9


def ad_hoc_gusto() -> tuple[str, list] | None:
    """Prompts the user to enter the attributes of a gusto.

    Returns:
        tuple | None: a tuple containing the label and attributes of the gusto
    """
    clear_screen()
    print(
        "---------------------------------------------------\n",
        f"          {C1}Get Reco/s from an Ad Hoc Gusto{CE}          \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    success, group_size = ui.get_positive_int("  Enter number of people: ")
    if not success:
        return None

    success, meal_type = ui.get_valid_meal_type(
        "  Enter type of meal (Breakfast, Lunch, or Dinner): "
    )
    if not success:
        return None

    success, budget = ui.get_positive_float("  Enter budget: ")
    if not success:
        return None

    success, max_distance = ui.get_positive_float(
        "  Enter maximum distance from UPLB (in meters): "
    )
    if not success:
        return None

    success, cuisine_type = ui.get_string(
        '  Enter cuisine type ("ANY" for any cuisine): '
    )
    if not success:
        return None

    success, min_rating = ui.get_valid_rating("  Enter minimum rating (1-5): ")
    if not success:
        return None

    return (
        "AD,HOC",
        [
            "AD,HOC",
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
        "---------------------------------------------------\n",
        f"                     {C1}Add Gusto{CE}                     \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )

    success, label = ui.get_string("  Enter label: ")
    label = label.upper()
    if not success:
        return gustos_dict
    if len(label) > LABEL_LENGTH:
        raise_err(f"Label must be {LABEL_LENGTH} characters or less!")
        return gustos_dict
    if label in gustos_dict:
        raise_err(f'Gusto "{label}" already exists!')
        return gustos_dict

    success, description = ui.get_string("  Enter description: ")
    if not success:
        return gustos_dict

    success, group_size = ui.get_positive_int("  Enter number of people: ")
    if not success:
        return gustos_dict

    success, meal_type = ui.get_valid_meal_type(
        "  Enter type of meal (Breakfast, Lunch, or Dinner): "
    )
    if not success:
        return gustos_dict

    success, budget = ui.get_positive_float("  Enter budget: ")
    if not success:
        return gustos_dict

    success, max_distance = ui.get_positive_float(
        "  Enter maximum distance from UPLB (in meters): "
    )
    if not success:
        return gustos_dict

    success, cuisine_type = ui.get_string(
        '  Enter cuisine type ("ANY" for any cuisine): '
    )
    cuisine_type = cuisine_type.upper()
    if not success:
        return gustos_dict

    success, min_rating = ui.get_valid_rating("  Enter minimum rating (1-5): ")
    if not success:
        return gustos_dict

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
        "---------------------------------------------------\n",
        f"                     {C1}Edit Gusto{CE}                    \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )

    success, label = ui.get_string("  Enter label: ")
    label = label.upper()
    if not success:
        return gustos_dict
    if label.upper() not in gustos_dict:
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
        "---------------------------------------------------\n",
        f"                     {C1}Edit Gusto{CE}                    \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    print(f"  Gusto Label: {label}")
    print(f"  Description: {description}")
    print(f"  Number of People: {group_size}")
    print(f"  Meal Type: {meal_type.capitalize()}")
    print(f"  Budget: {budget}")
    print(f"  Maximum Distance: {max_distance}")
    print(f"  Cuisine Type: {cuisine_type}")
    print(f"  Minimum Rating: {min_rating}")
    print("---------------------------------------------------")
    info(f"Press [ENTER] to keep current value.")

    success, label = ui.edit_string("  Edit label: ", label)
    if not success:
        return gustos_dict
    if label in gustos_dict and previous_label != label:
        raise_err(f'Gusto "{label}" already exists!')
        return gustos_dict
    if len(label) > LABEL_LENGTH:
        raise_err(f"Label must be {LABEL_LENGTH} characters or less!")
        return gustos_dict

    success, description = ui.edit_string("  Edit description: ", description)
    if not success:
        return gustos_dict

    success, group_size = ui.edit_positive_int("  Edit number of people: ", group_size)
    if not success:
        return gustos_dict

    success, meal_type = ui.edit_valid_meal_type(
        "  Edit type of meal (Breakfast, Lunch, or Dinner): ", meal_type
    )
    if not success:
        return gustos_dict

    success, budget = ui.edit_positive_float("  Edit budget: ", budget)
    if not success:
        return gustos_dict

    success, max_distance = ui.edit_positive_float(
        "  Edit maximum distance from UPLB (in meters): ", max_distance
    )
    if not success:
        return gustos_dict

    success, cuisine_type = ui.edit_string(
        '  Edit cuisine type ("ANY" for any cuisine): ', cuisine_type
    )
    if not success:
        return gustos_dict

    success, min_rating = ui.edit_valid_rating(
        "  Edit minimum rating (1-5): ", min_rating
    )
    if not success:
        return gustos_dict

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
        "---------------------------------------------------\n",
        f"                    {C1}Delete Gusto{CE}                   \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    success, label = ui.get_string("  Enter label: ")
    label = label.upper()
    print("---------------------------------------------------")
    if not success:
        raise_err("Invalid label!")
        return gustos_dict
    if label not in gustos_dict:
        raise_err(f'Gusto "{label}" does not exist!')
        return gustos_dict
    clear_screen()
    print(
        "---------------------------------------------------\n",
        f"                    {C1}Delete Gusto{CE}                   \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    print(f"  Label: {label}")
    print(f"  Description: {gustos_dict[label][0]}")
    print(f"  Number of People: {gustos_dict[label][1]}")
    print(f"  Meal Type: {gustos_dict[label][2].capitalize()}")
    print(f"  Budget: {gustos_dict[label][3]}")
    print(f"  Maximum Distance: {gustos_dict[label][4]}")
    print(f"  Cuisine Type: {gustos_dict[label][5]}")
    print(f"  Minimum Rating: {gustos_dict[label][6]}")
    print("---------------------------------------------------")
    print(f"  Are you sure you want to delete {label}?")
    print(f"  [Y] Yes{CE}")
    print(f"  [Any Key] No{CE}")
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
    """Displays the gustos in the gustos dictionary.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos to display
    """
    if not gustos_dict:
        raise_err("No gustos to display! Add a gusto!")
        return
    print(
        "---------------------------------------------------\n",
        f"                       {C1}Gustos{CE}                      \n",
        "---------------------------------------------------\n",
        f"{C2}    Label                 Description              {CE}\n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    for label, value in gustos_dict.items():
        desc = ""
        if len(value[0]) > 35:
            desc = value[0][:32] + "..."
        else:
            desc = value[0]
        print(f"  {label:>9}   {desc:<35}  ")
    print("---------------------------------------------------")


def display_gustos_detailed(gustos_dict: dict[str, list]) -> None:
    """Displays the gustos in the gustos dictionary with more detail.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos to display
    """
    if not gustos_dict:
        raise_err("No gustos to display! Add a gusto!")
        return
    print(
        "-------------------------------------------------------------------------------------------------------------------\n",
        f"                                                      {C1}Gustos{CE}                                                       \n",
        "-------------------------------------------------------------------------------------------------------------------\n",
        f"{C2}    Label          Description        #     Meal Type      Budget      Max Distance       Cuisine      Min Rating  {CE}\n",
        "-------------------------------------------------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    for label, value in gustos_dict.items():
        desc = ""
        if len(value[0]) > 20:
            desc = value[0][:17] + "..."
        else:
            desc = value[0]
        print(
            f"  {label:<9}   {desc:<20}   {value[1]:>3}   {value[2].capitalize():<11}   P{value[3]:>9.2f}   {value[4]:>13.2f}m   {value[5].capitalize():^13}   {value[6]:^10.1f}  "
        )
    print(
        "-------------------------------------------------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
