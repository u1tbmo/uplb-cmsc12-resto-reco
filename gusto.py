"""
This module contains the functions for adding, editing, deleting, and displaying gustos.
"""

# Local Module Imports
import user_inputs as ui
from misc import clear_screen, continue_prompt, info, raise_err
from colors import C1, C2, CE

# Global Variables / Constants
LABEL_LENGTH = 9


def display_gusto_details(gusto: str, gustos_dict: dict[str, list]) -> None:
    """Displays the details of a gusto.

    Args:
        gusto (str): the gusto to display
        gustos_dict (dict[str, list]): the dictionary of gustos
    """
    description = gustos_dict[gusto][0]
    group_size = gustos_dict[gusto][1]
    meal_type = gustos_dict[gusto][2].capitalize()
    budget = gustos_dict[gusto][3] if gustos_dict[gusto][3] != -1 else "Any"
    max_distance = gustos_dict[gusto][4] if gustos_dict[gusto][4] != -1 else "Any"
    cuisine_type = (
        gustos_dict[gusto][5].capitalize(
        ) if gustos_dict[gusto][5] != "ANY" else "Any"
    )
    min_rating = gustos_dict[gusto][6] if gustos_dict[gusto][6] != -1 else "Any"
    print(f"  Gusto Label: {gusto}")
    print(f"  Description: {description}")
    print(f"  Number of People: {group_size}")
    print(f"  Meal Type: {meal_type}")
    print(f"  Budget: {budget}")
    print(f"  Maximum Distance: {max_distance}")
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
        "---------------------------------------------------\n",
        f"                     {C1}View Gusto{CE}                     \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    success, gusto = ui.get_string("  Enter label: ")
    gusto = gusto.upper()
    if not success:
        return
    if gusto not in gustos_dict:
        raise_err(f'Gusto "{gusto}" does not exist!')
        return
    clear_screen()
    print(
        "---------------------------------------------------\n",
        f"                     {C1}View Gusto{CE}                     \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )
    display_gusto_details(gusto, gustos_dict)
    print("---------------------------------------------------")
    continue_prompt()


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
    info("* indicates optional fields")
    success, group_size = ui.get_positive_int("  Enter number of people: ")
    if not success:
        return None

    success, meal_type = ui.get_valid_meal_type(
        "  Enter type of meal (Breakfast, Lunch, or Dinner): "
    )
    if not success:
        return None

    success, budget = ui.get_positive_float("  *Enter budget: ", True)
    if not success:
        return None

    success, max_distance = ui.get_positive_float(
        "  *Enter maximum distance from UPLB (in meters): ", True
    )
    if not success:
        return None

    success, cuisine_type = ui.get_string("  *Enter cuisine type: ", True)
    if not success:
        return None

    success, min_rating = ui.get_valid_rating(
        "  *Enter minimum rating (1-5): ", True)
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
    info("* indicates optional fields")
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

    success, budget = ui.get_positive_float("  *Enter budget: ", True)
    if not success:
        return gustos_dict

    success, max_distance = ui.get_positive_float(
        "  *Enter maximum distance from UPLB (in meters): ", True
    )
    if not success:
        return gustos_dict

    success, cuisine_type = ui.get_string("  *Enter cuisine type: ", True)
    cuisine_type = cuisine_type.upper()
    if not success:
        return gustos_dict

    success, min_rating = ui.get_valid_rating(
        "  *Enter minimum rating (1-5): ", True)
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
    display_gusto_details(label, gustos_dict)
    print("---------------------------------------------------")
    info("Press [ENTER] to keep current value.")
    info('Type "ANY" to set a field to "ANY"')
    info("* indicates optional fields")
    print("---------------------------------------------------")

    success, label = ui.edit_string(f"  Enter label [{label}]: ", label)
    label = label.upper()
    if not success:
        return gustos_dict
    if label in gustos_dict and previous_label != label:
        raise_err(f'Gusto "{label}" already exists!')
        return gustos_dict
    if len(label) > LABEL_LENGTH:
        raise_err(f"Label must be {LABEL_LENGTH} characters or less!")
        return gustos_dict

    success, description = ui.edit_string(
        f"  Enter description [{description}]: ", description
    )
    if not success:
        return gustos_dict

    success, group_size = ui.edit_positive_int(
        f"  Enter group size [{group_size}]: ", group_size
    )
    if not success:
        return gustos_dict

    success, meal_type = ui.edit_valid_meal_type(
        f"  Enter meal type [{meal_type}]: ", meal_type
    )
    if not success:
        return gustos_dict

    success, budget = ui.edit_positive_float(
        f'  *Enter budget [{budget if budget != -1 else "Any"}]: ', budget, True
    )
    if not success:
        return gustos_dict

    success, max_distance = ui.edit_positive_float(
        f'  *Enter max distance [{max_distance if max_distance != -1 else "Any"}]: ', max_distance, True
    )
    if not success:
        return gustos_dict

    success, cuisine_type = ui.edit_string(
        f'  *Enter cuisine type [{cuisine_type if cuisine_type != "ANY" else "Any"}]: ', cuisine_type, True
    )
    cuisine_type = cuisine_type.upper()
    if not success:
        return gustos_dict

    success, min_rating = ui.edit_valid_rating(
        f'  *Enter min rating [{min_rating if min_rating != -1 else "Any"}]: ', min_rating, True
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
    display_gusto_details(label, gustos_dict)
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
        desc = value[0][:32] + "..." if len(value[0]) > 35 else value[0]
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
        desc = value[0][:17] + "..." if len(value[0]) > 20 else value[0]
        budget = "Any" if value[3] == -1 else f"₱{value[3]:.2f}"
        max_distance = "Any" if value[4] == -1 else f"{value[4]:.2f}m"
        min_rating = "Any" if value[6] == -1 else f"{value[6]} / 5"

        print(
            f"  {label:<9}   {desc:<20}   {value[1]:^3}   {value[2].capitalize():^11}   {budget:^10}   {max_distance:^15}   {value[5].capitalize():^13}   {min_rating:^10}  "
        )
    print(
        "-------------------------------------------------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
