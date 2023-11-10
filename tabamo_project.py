"""
This program recommends dining place/s based on the preferences of the user.
"""
# Tabamo, Euan Jed S. | B-1L
# Project

# Standard Library Imports
import random
import time

# File Imports
import save_load as sl
import gusto as g
import resto as r
import reco as rc
from misc import clear_screen, continue_prompt, raise_er

# Global Variables
restos: dict[str, list] = {}
gustos: dict[str, list] = {}


def manage_gustos(gustos_dict: dict[str, list]) -> dict[str, list]:
    choice = gusto_menu()
    if choice == "1":
        g.add_gustos(gustos_dict)
    elif choice == "2":
        g.edit_gustos(gustos_dict)
    elif choice == "3":
        g.delete_gustos(gustos_dict)
    elif choice == "4":
        g.display_gustos(gustos_dict)
    elif choice == "0":
        clear_screen()
    else:
        raise_er("Invalid choice!")
    return gustos_dict


def manage_restos(restos_dict: dict[str, list]) -> dict[str, list]:
    choice = resto_menu()
    if choice == "1":
        r.add_restos(restos_dict)
    elif choice == "2":
        r.edit_restos(restos_dict)
    elif choice == "3":
        r.delete_restos(restos_dict)
    elif choice == "4":
        r.display_restos(restos_dict)
    elif choice == "0":
        clear_screen()
    else:
        raise_er("Invalid choice!")
    return restos_dict


def main_menu() -> str:
    print(
        "+------------------------------------------+",
        "|          Welcome to Euan's UPLB          |",
        "|               Resto Reco!                |",
        "+------------------------------------------+",
        "|                   Menu                   |",
        "+------------------------------------------+",
        "| [1] Manage Gustos                        |",
        "| [2] Manage Restos                        |",
        "| [3] Get Recos                            |",
        "| [A] About                                |",
        "| [H] Help                                 |",
        "| [0] Exit                                 |",
        "+------------------------------------------+",
        sep="\n",
        end="\n",
    )
    return input("| Enter choice: ")


def gusto_menu() -> str:
    print(
        "+------------------------------------------+",
        "|           Menu > Manage Gustos           |",
        "+------------------------------------------+",
        "| [1] Add Gusto                            |",
        "| [2] Edit Gusto                           |",
        "| [3] Delete Gusto                         |",
        "| [4] Display Gustos                       |",
        "| [0] Back to Main Menu                    |",
        "+------------------------------------------+",
        sep="\n",
        end="\n",
    )
    return input("| Enter choice: ")


def resto_menu() -> str:
    print(
        "+------------------------------------------+",
        "|           Menu > Manage Restos           |",
        "+------------------------------------------+",
        "| [1] Add Resto                            |",
        "| [2] Edit Resto                           |",
        "| [3] Delete Resto                         |",
        "| [4] Display Restos                       |",
        "| [0] Back to Main Menu                    |",
        "+------------------------------------------+",
        sep="\n",
        end="\n",
    )
    return input("| Enter choice: ")


def about() -> None:
    clear_screen()
    print(
        "+------------------------------------------+",
        "|                  About                   |",
        "+------------------------------------------+",
        "|         Euan's UPLB Resto Reco!          |",
        "|    Programmed by: Tabamo, Euan Jed S.    |",
        "|       Started on November 7, 2023        |",
        "+------------------------------------------+",
        sep="\n",
        end="\n",
    )
    continue_prompt()


def help() -> None:
    clear_screen()
    print(
        "+------------------------------------------+",
        "|               Menu > Help                |",
        "+------------------------------------------+",
        "| [1] Gustos                               |",
        "| [2] Restos                               |",
        "| [3] Recos                                |",
        "+------------------------------------------+",
        sep="\n",
        end="\n",
    )
    choice = input("| Enter choice: ")
    if choice == "1":
        help_gustos()
    elif choice == "2":
        help_restos()
    elif choice == "3":
        help_recos()
    else:
        print("| ERROR: Invalid choice!")
        continue_prompt()


def help_gustos() -> None:
    clear_screen()
    print(
        "+-------------------------------------------------------------------------+",
        "| Gustos are preference profiles that contain the following attributes:   |",
        "+-------------------------------------------------------------------------+",
        "| Label = the unique identifier of the gusto                              |",
        "| Description = the description of the gusto                              |",
        "| Group Size = the number of people the gusto is for                      |",
        "| Meal Type = the meal type the gusto is for (breakfast, lunch, dinner)   |",
        "| Budget = the budget of the gusto (in pesos)                             |",
        "| Max Distance = the maximum distance of the resto from UPLB gate         |",
        "| Cuisine Type = the type of cuisine the resto serves                     |",
        "| Min Rating = the minimum rating of the resto                            |",
        "+-------------------------------------------------------------------------+",
        sep="\n",
        end="\n",
    )
    continue_prompt()


def help_restos() -> None:
    clear_screen()
    print(
        "+-------------------------------------------------------------------------+",
        "| Restos are dining places with the following attributes:                 |",
        "+-------------------------------------------------------------------------+",
        "| Name = the unique identifier of the resto                               |",
        "| Distance = the distance from UPLB gate to the resto                     |",
        "| Cuisine Type = the type of cuisine the resto serves                     |",
        "| Meal Type = the meal types the resto serves (breakfast, lunch, dinner)  |",
        "| Cost = the average cost of a meal in the resto                          |",
        "| Rating = the average rating of the resto                                |",
        "+-------------------------------------------------------------------------+",
        sep="\n",
        end="\n",
    )
    continue_prompt()


def help_recos() -> None:
    clear_screen()
    print(
        "+-------------------------------------------------------------------------+",
        "| Recos are dining place/s recommended by the program based on the user's |",
        "| preferences. The program will recommend resto/s that are within the     |",
        '| "gustos" or preference profile of the user.                             |',
        "+-------------------------------------------------------------------------+",
        sep="\n",
        end="\n",
    )
    continue_prompt()


def exit() -> None:
    clear_screen()
    message = "See you next time!     "
    for i in range(len(message)):
        rotate = message[i % len(message) :] + message[: i % len(message)]
        print(rotate)
        time.sleep(0.02)
        clear_screen()
    print(message)


def main():
    sl.load(restos, gustos)
    clear_screen()
    while True:
        choice = main_menu()
        if choice == "1":
            gustos_dict = manage_gustos(gustos)
        elif choice == "2":
            restos_dict = manage_restos(restos)
        elif choice == "3":
            rc.get_recos(restos, gustos)
        elif choice == "0":
            exit()
            break
        elif choice.upper() == "A":
            about()
        elif choice.upper() == "H":
            help()
        elif choice.upper() == "C":
            clear_screen()
        else:
            raise_er("Invalid choice!")
            clear_screen()


if __name__ == "__main__":
    main()
