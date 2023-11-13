"""
This module contains the functions for adding, editing, deleting, and displaying gustos.
"""

"""
Gusto: a gusto is a preference profile with the following attributes:
    gustos = {
        label: [description, group_size, meal_type, budget, max_distance, cuisine_type, min_rating]
    }
    label: str = the unique identifier of the gusto
    description: str = the description of the gusto
    group_size: int = the number of people the gusto is for
    meal_type: str = the meal type the gusto is for (breakfast, lunch, dinner)
    budget: float = the budget of the gusto (in pesos)
    max_distance: float = the maximum distance of the resto from UPLB gate (in meters)
    cuisine_type: str = the type of cuisine the resto serves
    min_rating: float = the minimum rating of the resto (out of 5)
"""
# Global Variables / Constants
LABEL_LENGTH = 9

# File Imports
import save_load as sl
from misc import clear_screen, continue_prompt, info, raise_er
import colors as c
from colors import C1, C2, CE, CD


def ad_hoc_gusto() -> tuple | None:
    clear_screen()
    print(
        f"---------------------------------------------------\n",
        f"          {C1}Get Reco/s from an Ad Hoc Gusto{CE}          \n",
        f"---------------------------------------------------\n",
        sep="",
        end="",
    )
    group_size = input("  Enter number of people: ")
    if group_size == "":
        raise_er("Group size cannot be empty!")
        return None
    if not group_size.isdigit():
        raise_er("Invalid group size!")
        return None
    group_size = int(group_size)
    if group_size <= 0:
        raise_er("Group size must be greater than 0!")
        return None
    meal_type = input("  Enter type of meal (Breakfast, Lunch, Dinner): ").upper()
    if meal_type.strip() not in ["BREAKFAST", "LUNCH", "DINNER"]:
        raise_er("Invalid meal type!")
        return None
    budget = input("  Enter budget: ")
    if budget == "":
        raise_er("Budget cannot be empty!")
        return None
    if not budget.replace(".", "", 1).isdigit():
        raise_er("Invalid budget!")
        return None
    budget = float(budget)
    if budget <= 0:
        raise_er("Budget must be greater than 0!")
        return None
    max_distance = input("  Enter maximum distance from UPLB (in meters): ")
    if max_distance == "":
        raise_er("Maximum distance cannot be empty!")
        return None
    if not max_distance.replace(".", "", 1).isdigit():
        raise_er("Invalid maximum distance!")
        return None
    max_distance = float(max_distance)
    if max_distance <= 0:
        raise_er("Maximum distance must be greater than 0!")
        return None
    cuisine_type = (
        input('  Enter cuisine type ("ANY" for any cuisine): ').strip().upper()
    )
    if "," in cuisine_type:
        raise_er("Cuisine type cannot contain commas!")
        return None
    if cuisine_type == "":
        raise_er("Cuisine type cannot be empty!")
        return None
    min_rating = input("  Enter minimum rating (out of 5): ")
    if min_rating == "":
        raise_er("Minimum rating cannot be empty!")
        return None
    if not min_rating.replace(".", "", 1).isdigit():
        raise_er("Invalid minimum rating!")
        return None
    min_rating = float(min_rating)
    if min_rating < 0 or min_rating > 5:
        raise_er("Minimum rating must be between 0 and 5!")
        return None

    return (
        "AD,HOC",
        [
            "AD,HOC",
            group_size,
            meal_type,
            budget,
            max_distance,
            cuisine_type,
            min_rating,
        ],
    )


def add_gustos(gustos_dict: dict[str, list]) -> dict[str, list]:
    clear_screen()
    print(
        f"---------------------------------------------------\n",
        f"                     {C1}Add Gusto{CE}                     \n",
        f"---------------------------------------------------\n",
        sep="",
        end="",
    )
    label = input("  Enter label: ").strip().upper()
    print("--------------------------------------------")
    if "," in label:
        raise_er("Label cannot contain commas!")
        return gustos_dict
    elif label == "":
        raise_er("Label cannot be empty!")
        return gustos_dict
    elif len(label) > LABEL_LENGTH:
        raise_er(f"Label cannot exceed {LABEL_LENGTH} characters!")
        return gustos_dict
    elif label in gustos_dict:
        raise_er(f'Gusto "{label}" already exists!')
        return gustos_dict
    else:
        description = input("  Enter description: ").strip()
        if "," in description:
            raise_er("Description cannot contain commas!")
            return gustos_dict
        if description == "":
            raise_er("Description cannot be empty!")
            return gustos_dict
        group_size = input("  Enter number of people: ")
        if group_size == "":
            raise_er("Group size cannot be empty!")
            return gustos_dict
        if not group_size.isdigit():
            raise_er("Invalid group size!")
            return gustos_dict
        group_size = int(group_size)
        if group_size <= 0:
            raise_er("Group size must be greater than 0!")
            return gustos_dict
        meal_type = input("  Enter type of meal (Breakfast, Lunch, Dinner): ").upper()
        if meal_type.strip() not in ["BREAKFAST", "LUNCH", "DINNER"]:
            raise_er("Invalid meal type!")
            return gustos_dict
        budget = input("  Enter budget: ")
        if budget == "":
            raise_er("Budget cannot be empty!")
            return gustos_dict
        if not budget.replace(".", "", 1).isdigit():
            raise_er("Invalid budget!")
            return gustos_dict
        budget = float(budget)
        if budget <= 0:
            raise_er("Budget must be greater than 0!")
            return gustos_dict
        max_distance = input("  Enter maximum distance from UPLB (in meters): ")
        if max_distance == "":
            raise_er("Maximum distance cannot be empty!")
            return gustos_dict
        if not max_distance.replace(".", "", 1).isdigit():
            raise_er("Invalid maximum distance!")
            return gustos_dict
        max_distance = float(max_distance)
        if max_distance <= 0:
            raise_er("Maximum distance must be greater than 0!")
            return gustos_dict
        cuisine_type = (
            input('  Enter cuisine type ("ANY" for any cuisine): ').strip().upper()
        )
        if "," in cuisine_type:
            raise_er("Cuisine type cannot contain commas!")
            return gustos_dict
        if cuisine_type == "":
            raise_er("Cuisine type cannot be empty!")
            return gustos_dict
        min_rating = input("  Enter minimum rating (out of 5): ")
        if min_rating == "":
            raise_er("Minimum rating cannot be empty!")
            return gustos_dict
        if not min_rating.replace(".", "", 1).isdigit():
            raise_er("Invalid minimum rating!")
            return gustos_dict
        min_rating = float(min_rating)
        if min_rating < 0 or min_rating > 5:
            raise_er("Minimum rating must be between 0 and 5!")
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
        sl.save_gustos(gustos_dict)
        info(f'Added Gusto "{label}"')
        continue_prompt()
        return gustos_dict


def edit_gustos(gustos_dict: dict[str, list]) -> dict[str, list]:
    if not gustos_dict:
        raise_er("No gustos to edit! Add a gusto!")
        return gustos_dict
    clear_screen()
    display_gustos_simple(gustos_dict)
    print(
        f"---------------------------------------------------\n",
        f"                     {C1}Edit Gusto{CE}                    \n",
        f"---------------------------------------------------\n",
        sep="",
        end="",
    )
    label = input("  Enter label: ").strip().upper()
    previous_label = label
    print("--------------------------------------------")
    if "," in label or label == "":
        raise_er("Invalid label!")
        return gustos_dict
    elif label not in gustos_dict:
        raise_er(f'Gusto "{label}" does not exist!')
        return gustos_dict
    else:
        clear_screen()
        print(
            f"---------------------------------------------------\n",
            f"                     {C1}Edit Gusto{CE}                    \n",
            f"---------------------------------------------------\n",
            sep="",
            end="",
        )
        info(f"Fetched Gusto {label}!")
        print("---------------------------------------------------")
        print(f"  Gusto Label: {label}")
        print(f"  Description: {gustos_dict[label][0]}")
        print(f"  Number of People: {gustos_dict[label][1]}")
        print(f"  Meal Type: {gustos_dict[label][2]}")
        print(f"  Budget: {gustos_dict[label][3]}")
        print(f"  Maximum Distance: {gustos_dict[label][4]}")
        print(f"  Cuisine Type: {gustos_dict[label][5]}")
        print(f"  Minimum Rating: {gustos_dict[label][6]}")
        print("---------------------------------------------------")
        label = input(f"  Edit label: ").strip().upper()
        if "," in label:
            raise_er("Label cannot contain commas!")
            return gustos_dict
        elif label == "":
            raise_er("Label cannot be empty!")
            return gustos_dict
        elif label in gustos_dict and previous_label != label:
            raise_er(f'Gusto "{label}" already exists!')
            return gustos_dict
        description = input(f"  Edit description: ").strip()
        if "," in description:
            raise_er("Description cannot contain commas!")
            return gustos_dict
        elif description == "":
            raise_er("Description cannot be empty!")
            return gustos_dict
        group_size = input(f"  Edit number of people: ")
        if group_size == "":
            raise_er("Group size cannot be empty!")
            return gustos_dict
        elif not group_size.isdigit():
            raise_er("Invalid group size!")
            return gustos_dict
        group_size = int(group_size)
        if group_size <= 0:
            raise_er("Group size must be greater than 0!")
            return gustos_dict
        meal_type = input("  Edit type of meal (Breakfast, Lunch, Dinner): ").upper()
        if meal_type.strip() not in ["BREAKFAST", "LUNCH", "DINNER"]:
            raise_er("Invalid meal type!")
            return gustos_dict
        elif meal_type == "":
            raise_er("Meal type cannot be empty!")
            return gustos_dict
        budget = input("  Edit budget: ")
        if budget == "":
            raise_er("Budget cannot be empty!")
            return gustos_dict
        elif not budget.replace(".", "", 1).isdigit():
            raise_er("Invalid budget!")
            return gustos_dict
        budget = float(budget)
        if budget <= 0:
            raise_er("Budget must be greater than 0!")
            return gustos_dict
        max_distance = input("  Edit maximum distance (in meters): ")
        if max_distance == "":
            raise_er("Maximum distance cannot be empty!")
            return gustos_dict
        elif not max_distance.replace(".", "", 1).isdigit():
            raise_er("Invalid maximum distance!")
            return gustos_dict
        max_distance = float(max_distance)
        if max_distance <= 0:
            raise_er("Maximum distance must be greater than 0!")
            return gustos_dict
        cuisine_type = (
            input('  Edit cuisine type ("ANY" for any cuisine): ').strip().upper()
        )
        if "," in cuisine_type:
            raise_er("Cuisine type cannot contain commas!")
            return gustos_dict
        elif cuisine_type == "":
            raise_er("Cuisine type cannot be empty!")
            return gustos_dict
        min_rating = input("  Edit minimum rating (out of 5): ")
        if min_rating == "":
            raise_er("Minimum rating cannot be empty!")
            return gustos_dict
        elif not min_rating.replace(".", "", 1).isdigit():
            raise_er("Invalid minimum rating!")
            return gustos_dict
        min_rating = float(min_rating)
        if min_rating < 0 or min_rating > 5:
            raise_er("Minimum rating must be between 0 and 5!")
            return gustos_dict
        if label != previous_label:
            del gustos_dict[previous_label]
        gustos_dict[label] = [
            description,
            group_size,
            meal_type,
            budget,
            max_distance,
            cuisine_type,
            min_rating,
        ]
        sl.save_gustos(gustos_dict)
        if previous_label != label:
            info(f'Edited Gusto "{previous_label}" to "{label}"')
        else:
            info(f'Edited Gusto "{label}"')
        continue_prompt()
        return gustos_dict


def delete_gustos(gustos_dict: dict[str, list]) -> dict[str, list]:
    if not gustos_dict:
        raise_er("No gustos to delete! Add a gusto!")
        return gustos_dict

    clear_screen()

    display_gustos_simple(gustos_dict)

    print(
        f"---------------------------------------------------\n",
        f"                    {C1}Delete Gusto{CE}                   \n",
        f"---------------------------------------------------\n",
        sep="",
        end="",
    )
    label = input("  Enter label: ").strip().upper()
    print("--------------------------------------------")
    if "," in label or label == "":
        raise_er("Invalid label!")
        return gustos_dict
    if label not in gustos_dict:
        raise_er(f'Gusto "{label}" does not exist!')
    else:
        clear_screen()
        print(
            f"---------------------------------------------------\n",
            f"                    {C1}Delete Gusto{CE}                   \n",
            f"---------------------------------------------------\n",
            sep="",
            end="",
        )
        info(f"Fetched Gusto {label}!")
        print("---------------------------------------------------")
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
            sl.save_gustos(gustos_dict)
            info(f'Deleted Gusto "{label}"')
            continue_prompt()
        else:
            info(f'Canceled. Expected "Y", got "{choice}"')
            continue_prompt()
    return gustos_dict


def display_gustos_simple(gustos_dict: dict[str, list]) -> None:
    if not gustos_dict:
        raise_er("No gustos to display! Add a gusto!")
        return
    print(
        f"---------------------------------------------------\n",
        f"                       {C1}Gustos{CE}                      \n",
        f"---------------------------------------------------\n",
        f"{C2}    Label                 Description              {CE}\n",
        f"---------------------------------------------------\n",
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
    if not gustos_dict:
        raise_er("No gustos to display! Add a gusto!")
        return
    print(
        f"-------------------------------------------------------------------------------------------------------------------\n",
        f"                                                      {C1}Gustos{CE}                                                       \n",
        f"-------------------------------------------------------------------------------------------------------------------\n",
        f"{C2}    Label          Description        #     Meal Type      Budget      Max Distance       Cuisine      Min Rating  {CE}\n",
        f"-------------------------------------------------------------------------------------------------------------------\n",
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
            f"  {label:<9}   {desc:<20}   {value[1]:>3}   {value[2]:^11}   {value[3]:>10.2f}   {value[4]:>13.2f}m   {value[5].capitalize():^13}   {value[6]:^10.1f}  "
        )
    print(
        "-------------------------------------------------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
