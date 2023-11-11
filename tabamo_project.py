"""
This program recommends dining place/s based on the preferences of the user.
"""
# Tabamo, Euan Jed S. | B-1L
# Project

# Standard Library Imports
import os

# File Imports
import save_load as sl
import gusto as g
import resto as r
import reco as rc
import colors as c
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
        g.display_gustos_simple(gustos_dict)
        continue_prompt()
    elif choice == "5":
        g.display_gustos_detailed(gustos_dict)
        continue_prompt()
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
        r.display_restos_simple(restos_dict)
        continue_prompt()
    elif choice == "5":
        r.display_restos_detailed(restos_dict)
        continue_prompt()
    elif choice == "0":
        clear_screen()
    else:
        raise_er("Invalid choice!")
    return restos_dict


def main_menu() -> str:
    print(
        "+-------------------------------------------+\n",
        "|                Main Menu                  |\n",
        "+-------------------------------------------+\n",
        "| 1 | Manage Gustos                         |\n",
        "| 2 | Manage Restos                         |\n",
        "| 3 | Get Recos                             |\n",
        "| A | About                                 |\n",
        "| H | Help                                  |\n",
        "| 0 | Exit                                  |\n",
        "+-------------------------------------------+\n",
        sep="",
        end="",
    )
    return input(f"| Enter choice: ")


def gusto_menu() -> str:
    clear_screen()
    print(
        f"{c.GRAY}",
        "+-------------------------------------------+\n",
        "|                Main Menu                  |\n",
        "+-------------------------------------------+\n",
        f"| {c.YELLOW2}1 | Manage Gustos{c.GRAY}                         |\n",
        "| 2 | Manage Restos                         |\n",
        "| 3 | Get Recos                             |\n",
        "| A | About                                 |\n",
        "| H | Help                                  |\n",
        "| 0 | Exit                                  |\n",
        "+-------------------------------------------+\n",
        f"{c.END}",
        sep="",
        end="",
    )
    print(
        "+-------------------------------------------+\n",
        "|               Manage Gustos               |\n",
        "+-------------------------------------------+\n",
        "| 1 | Add Gusto                             |\n",
        "| 2 | Edit Gusto                            |\n",
        "| 3 | Delete Gusto                          |\n",
        "| 4 | Display Gustos (Simple)               |\n",
        "| 5 | Display Gustos (Detailed)             |\n",
        "| 0 | Back to Main Menu                     |\n",
        "+-------------------------------------------+\n",
        sep="",
        end="",
    )
    return input("| Enter choice: ")


def resto_menu() -> str:
    clear_screen()
    print(
        f"{c.GRAY}",
        "+-------------------------------------------+\n",
        "|                Main Menu                  |\n",
        "+-------------------------------------------+\n",
        "| 1 | Manage Gustos                         |\n",
        f"| {c.YELLOW2}2 | Manage Restos{c.GRAY}                         |\n",
        "| 3 | Get Recos                             |\n",
        "| A | About                                 |\n",
        "| H | Help                                  |\n",
        "| 0 | Exit                                  |\n",
        "+-------------------------------------------+\n",
        f"{c.END}",
        sep="",
        end="",
    )
    print(
        "+-------------------------------------------+\n",
        "|               Manage Restos               |\n",
        "+-------------------------------------------+\n",
        "| 1 | Add Resto                             |\n",
        "| 2 | Edit Resto                            |\n",
        "| 3 | Delete Resto                          |\n",
        "| 4 | Display Restos (Simple)               |\n",
        "| 5 | Display Restos (Detailed)             |\n",
        "| 0 | Back to Main Menu                     |\n",
        "+-------------------------------------------+\n",
        sep="",
        end="",
    )
    return input("| Enter choice: ")


def about() -> None:
    clear_screen()
    print(
        "+------------------------------------------+\n",
        "|                  About                   |\n",
        "+------------------------------------------+\n",
        "|         Euan's UPLB Resto Reco!          |\n",
        "|    Programmed by: Tabamo, Euan Jed S.    |\n",
        "|       Started on November 7, 2023        |\n",
        "+------------------------------------------+\n",
        sep="",
        end="",
    )
    continue_prompt()


def help() -> None:
    clear_screen()
    print(
        "+------------------------------------------+\n",
        "|                   Help                   |\n",
        "+------------------------------------------+\n",
        "| 1 | Gustos                               |\n",
        "| 2 | Restos                               |\n",
        "| 3 | Recos                                |\n",
        "| 0 | Back to Main Menu                    |\n",
        "+------------------------------------------+\n",
        sep="",
        end="",
    )
    choice = input("| Enter choice: ")
    if choice == "1":
        help_gustos()
    elif choice == "2":
        help_restos()
    elif choice == "3":
        help_recos()
    elif choice == "0":
        clear_screen()
    else:
        print("| ERROR: Invalid choice!")
        continue_prompt()


def help_gustos() -> None:
    clear_screen()
    print(
        "+-------------------------------------------------------------------------+\n",
        "| Gustos are preference profiles that contain the following attributes:   |\n",
        "+-------------------------------------------------------------------------+\n",
        "| Label = the unique identifier of the gusto                              |\n",
        "| Description = the description of the gusto                              |\n",
        "| Group Size = the number of people the gusto is for                      |\n",
        "| Meal Type = the meal type the gusto is for (breakfast, lunch, dinner)   |\n",
        "| Budget = the budget of the gusto (in pesos)                             |\n",
        "| Max Distance = the maximum distance of the resto from UPLB gate         |\n",
        "| Cuisine Type = the type of cuisine the resto serves                     |\n",
        "| Min Rating = the minimum rating of the resto                            |\n",
        "+-------------------------------------------------------------------------+\n",
        sep="",
        end="",
    )
    continue_prompt()


def help_restos() -> None:
    clear_screen()
    print(
        f"{c.YELLOW2}"
        "+-------------------------------------------------------------------------+\n",
        "| Restos are dining places with the following attributes:                 |\n",
        "+-------------------------------------------------------------------------+\n",
        "| Name = the unique identifier of the resto                               |\n",
        "| Distance = the distance from UPLB gate to the resto                     |\n",
        "| Cuisine Type = the type of cuisine the resto serves                     |\n",
        "| Meal Type = the meal types the resto serves (breakfast, lunch, dinner)  |\n",
        "| Cost = the average cost of a meal in the resto                          |\n",
        "| Rating = the average rating of the resto                                |\n",
        "+-------------------------------------------------------------------------+\n",
        sep="",
        end="",
    )
    continue_prompt()


def help_recos() -> None:
    clear_screen()
    print(
        "+-------------------------------------------------------------------------+\n",
        "| Recos are dining place/s recommended by the program based on the user's |\n",
        "| preferences. The program will recommend resto/s that are within the     |\n",
        '| "gustos" or preference profile of the user.                             |\n',
        "+-------------------------------------------------------------------------+\n",
        sep="",
        end="",
    )
    continue_prompt()


def exit() -> None:
    clear_screen()
    message = f"{c.ITALIC}See you next time!{c.END}"
    print(f"{message}")


def load_colors() -> None:
    os.system("")


def main():
    load_colors()
    sl.load(restos, gustos)
    clear_screen()
    while True:
        choice = main_menu()
        if choice == "0":
            exit()
            break
        elif choice == "1":
            manage_gustos(gustos)
        elif choice == "2":
            manage_restos(restos)
        elif choice == "3":
            rc.get_recos(restos, gustos)
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
