"""
This module contains the functions for adding, editing, deleting, and displaying restos.
"""

"""
Resto: a resto is a dining place with the following attributes:
Restos Format:
    restos = {
        name: [distance, cuisine_type, meal_type, cost, rating]
    }
    name: str = the unique identifier of the resto
    distance: float = the distance from UPLB gate to the resto (in meters)
    cuisine_type: str = the type of cuisine the resto serves
    meal_type: str = the meal types the resto serves (breakfast, lunch, dinner)
    cost: float = the average cost of a meal in the resto (in pesos)
    rating: float = the average rating of the resto (out of 5)
"""
# Global Variables / Constants
NAME_LENGTH = 22

# File Imports
import save_load as sl
from misc import clear_screen, continue_prompt, raise_er


def add_restos(restos_dict: dict[str, list]) -> dict[str, list]:
    # Clear the screen
    clear_screen()

    # Print the header
    print("+------------------------------------------+")
    print("|                Add Resto                 |")
    print("+------------------------------------------+")

    # User Input: Name
    name = input("| Name: ").strip().upper()
    print("+------------------------------------------+")
    # Validation: Name
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
        # User Input: Distance
        distance = input("| Enter distance from UPLB gate (in meters): ").strip()
        # Validation: Distance
        if distance == "":
            raise_er("Distance cannot be empty.")
            return restos_dict
        elif not distance.replace(".", "", 1).isdigit():
            raise_er("Invalid distance.")
            return restos_dict
        distance = float(distance)

        # User Input: Cuisine Type
        cuisine_type = input("| Enter cuisine type: ").strip().upper()
        # Validation: Cuisine Type
        if "," in cuisine_type:
            raise_er("Cuisine type cannot contain commas.")
            return restos_dict
        elif cuisine_type == "":
            raise_er("Cuisine type cannot be empty.")
            return restos_dict

        # User Input: Meal Type
        print('| Enter y if the resto serves the meal type, Press "Enter" if not.')
        meal_type = ""
        if input("| Does the resto serve breakfast?: ").strip().lower() == "y":
            meal_type += "B"
        if input("| Does the resto serve lunch?: ").strip().lower() == "y":
            meal_type += "L"
        if input("| Does the resto serve dinner?: ").strip().lower() == "y":
            meal_type += "D"
        # Validation: Meal Type
        if meal_type == "":
            raise_er("Resto must serve at least one meal type.")
            return restos_dict

        # User Input: Cost
        cost = input("| Enter typical cost of a meal (in pesos): ").strip()
        # Validation: Cost
        if cost == "":
            raise_er("Cost cannot be empty.")
            return restos_dict
        elif not cost.replace(".", "", 1).isdigit():
            raise_er("Invalid cost.")
            return restos_dict
        cost = float(cost)

        # User Input: Rating
        rating = input("| Enter rating (out of 5): ").strip()
        # Validation: Rating
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

        # Add resto to restos_dict
        restos_dict[name] = [distance, cuisine_type, meal_type, cost, rating]

        # Save restos and print success message
        sl.save_restos(restos_dict)
        print(f'| Added "{name}" to Restos!')
        continue_prompt()
        return restos_dict


def edit_restos(restos_dict: dict[str, list]) -> dict[str, list]:
    # Check if there are restos to edit
    if not restos_dict:
        raise_er("No restos to edit. Add a resto!")
        return restos_dict
    # Clear the screen
    clear_screen()

    # Display restos
    display_restos(restos_dict)

    # Print the header
    print("+------------------------------------------+")
    print("|                Edit Resto                |")
    print("+------------------------------------------+")

    # User Input: Name
    name = input("| Name: ").strip().upper()
    previous_name = name
    print("+------------------------------------------+")
    # Validation: Name
    if "," in name:
        raise_er("Name cannot contain commas.")
        return restos_dict
    elif name == "":
        raise_er("Name cannot be empty.")
        return restos_dict
    elif name not in restos_dict:
        raise_er(f"Resto {name} does not exist.")
        return restos_dict
    else:
        # Display Resto Info
        print(f"| Name: {name}")
        print(f"| Distance from UPLB gate: {restos_dict[name][0]} meters")
        print(f"| Cuisine Type: {restos_dict[name][1]}")
        print(f"| Meal Type: {restos_dict[name][2]}")
        print(f"| Cost: {restos_dict[name][3]} pesos")
        print(f"| Rating: {restos_dict[name][4]}")
        print("+------------------------------------------+")
        # User Input: Name
        name = input("| Edit name: ").strip().upper()
        # Validation: Name
        if "," in name:
            raise_er("Name cannot contain commas.")
            return restos_dict
        elif name == "":
            raise_er("Name cannot be empty.")
            return restos_dict
        elif name in restos_dict and previous_name != name:
            raise_er(f"Resto {name} already exists.")
            return restos_dict
        # User Input: Distance
        distance = input("| Edit distance from UPLB gate (in meters): ").strip()
        # Validation: Distance
        if distance == "":
            raise_er("Distance cannot be empty.")
            return restos_dict
        elif not distance.replace(".", "", 1).isdigit():
            raise_er("Invalid distance.")
            return restos_dict
        distance = float(distance)

        # User Input: Cuisine Type
        cuisine_type = input("| Edit cuisine type: ").strip().upper()
        # Validation: Cuisine Type
        if "," in cuisine_type:
            raise_er("Cuisine type cannot contain commas.")
            return restos_dict
        elif cuisine_type == "":
            raise_er("Cuisine type cannot be empty.")
            return restos_dict

        # User Input: Meal Type
        print('| Edit y if the resto serves the meal type, Press "Enter" if not.')
        meal_type = ""
        if input("| Does the resto serve breakfast?: ").strip().lower() == "y":
            meal_type += "B"
        if input("| Does the resto serve lunch?: ").strip().lower() == "y":
            meal_type += "L"
        if input("| Does the resto serve dinner?: ").strip().lower() == "y":
            meal_type += "D"
        # Validation: Meal Type
        if meal_type == "":
            raise_er("Resto must serve at least one meal type.")
            return restos_dict

        # User Input: Cost
        cost = input("| Edit typical cost of a meal (in pesos): ").strip()
        # Validation: Cost
        if cost == "":
            raise_er("Cost cannot be empty.")
            return restos_dict
        elif not cost.replace(".", "", 1).isdigit():
            raise_er("Invalid cost.")
            return restos_dict
        cost = float(cost)

        # User Input: Rating
        rating = input("| Edit rating (out of 5): ").strip()
        # Validation: Rating
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

        # Change name by deleting previous name if name is changed
        if previous_name != name:
            del restos_dict[previous_name]

        # Add resto to restos_dict
        restos_dict[name] = [distance, cuisine_type, meal_type, cost, rating]

        # Save restos and print success message
        sl.save_restos(restos_dict)
        if previous_name != name:
            print(f'| Edited Resto "{previous_name} to {name}"')
        else:
            print(f'| Edited Resto "{name}"')
        continue_prompt()
        return restos_dict


def delete_restos(restos_dict: dict[str, list]) -> dict[str, list]:
    clear_screen()
    display_restos(restos_dict)
    print("+------------------------------------------+")
    print("|              Delete Resto                |")
    print("+------------------------------------------+")
    name = input("Name: ").strip().upper()
    if name not in restos_dict:
        raise_er(f"Resto {name} does not exist.")
        return restos_dict
    else:
        print(f"| Name: {name}")
        print(f"| Distance from UPLB gate: {restos_dict[name][0]} meters")
        print(f"| Cuisine Type: {restos_dict[name][1]}")
        print(f"| Meal Type: {restos_dict[name][2]}")
        print(f"| Cost: {restos_dict[name][3]} pesos")
        print(f"| Rating: {restos_dict[name][4]}")
        print("+------------------------------------------+")
        print(f'| Are you sure you want to delete "{name}"?')
        print("| [Y] Yes")
        print("| [Any Key] No")
        choice = input("| Enter choice: ").upper()
        if choice == "Y":
            del restos_dict[name]
            sl.save_gustos(restos_dict)
            print(f'| Deleted "{name}"!')
            continue_prompt()
        else:
            print(f'| Canceled. Expected "Y", got "{choice}"')
            continue_prompt()
    return restos_dict


def display_restos(restos_dict: dict[str, list]) -> None:
    clear_screen()

    if not restos_dict:
        raise_er("No restos to display. Add a resto!")
        return
    print(
        "+-----------------------------------------------------------------------------------------------------------------------+"
    )
    print(
        "|                                                        Restos                                                         |"
    )
    print(
        "+-----------------------------------------------------------------------------------------------------------------------+"
    )
    print(
        #                                                                   | Breakfast, Lunch, Dinner |
        "|          Name          | Distance from UPLB Gate |    Cuisine    |        Meal Types        |    Cost    |   Rating   |"
    )
    for name, value in restos_dict.items():
        meal_types = ""
        for c in value[2]:
            if c == "B":
                meal_types += "Breakfast, "
            elif c == "L":
                meal_types += "Lunch, "
            elif c == "D":
                meal_types += "Dinner, "
        meal_types = meal_types.rstrip(", ")
        if value[2] != "BLD":
            meal_types = f" {meal_types} "
        print(
            f"| {name:<22} | {value[0]:>22.2f}m | {value[1]:^13} | {meal_types:^24} | {value[3]:>10.2f} | {value[4]:^10.1f} |"
        )
    print(
        "+-----------------------------------------------------------------------------------------------------------------------+"
    )
    continue_prompt()
