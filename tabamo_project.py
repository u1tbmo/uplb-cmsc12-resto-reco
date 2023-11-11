"""
This program recommends dining place/s based on the preferences of the user.
"""
# Tabamo, Euan Jed S.   B-1L
# Project

# Standard Library Imports
import os

# File Imports
import save_load as sl
import gusto as g
import resto as r
import reco as rc
import colors as c
import help as h
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
        f"---------------------------------------------\n",
        f"                 {c.YELLOW2}Main Menu{c.END}                   \n",
        f"---------------------------------------------\n",
        f"  1   Manage Gustos                          \n",
        f"  2   Manage Restos                          \n",
        f"  3   Get Recos                              \n",
        f"  A   About                                  \n",
        f"  H   Help                                   \n",
        f"  0   Exit                                   \n",
        f"---------------------------------------------\n",
        sep="",
        end="",
    )
    return input(f"  Enter choice: ")


def gusto_menu() -> str:
    clear_screen()
    print(
        f"{c.GRAY}",
        f"---------------------------------------------\n",
        f"                 Main Menu                   \n",
        f"---------------------------------------------\n",
        f"  {c.YELLOW2}1   Manage Gustos{c.GRAY}                          \n",
        f"  2   Manage Restos                          \n",
        f"  3   Get Recos                              \n",
        f"  A   About                                  \n",
        f"  H   Help                                   \n",
        f"  0   Exit                                   \n",
        f"---------------------------------------------\n",
        f"{c.END}",
        sep="",
        end="",
    )
    print(
        f"---------------------------------------------\n",
        f"                {c.YELLOW2}Manage Gustos{c.END}                \n",
        f"---------------------------------------------\n",
        f"  1   Add Gusto                              \n",
        f"  2   Edit Gusto                             \n",
        f"  3   Delete Gusto                           \n",
        f"  4   Display Gustos (Simple)                \n",
        f"  5   Display Gustos (Detailed)              \n",
        f"  0   Back to Main Menu                      \n",
        f"---------------------------------------------\n",
        sep="",
        end="",
    )
    return input("  Enter choice: ")


def resto_menu() -> str:
    clear_screen()
    print(
        f"{c.GRAY}",
        f"---------------------------------------------\n",
        f"                 Main Menu                   \n",
        f"---------------------------------------------\n",
        f"  1   Manage Gustos                          \n",
        f"  {c.YELLOW2}2   Manage Restos{c.GRAY}                          \n",
        f"  3   Get Recos                              \n",
        f"  A   About                                  \n",
        f"  H   Help                                   \n",
        f"  0   Exit                                   \n",
        f"---------------------------------------------\n",
        f"{c.END}",
        sep="",
        end="",
    )
    print(
        f"---------------------------------------------\n",
        f"                {c.YELLOW2}Manage Restos{c.END}                \n",
        f"---------------------------------------------\n",
        f"  1   Add Resto                              \n",
        f"  2   Edit Resto                             \n",
        f"  3   Delete Resto                           \n",
        f"  4   Display Restos (Simple)                \n",
        f"  5   Display Restos (Detailed)              \n",
        f"  0   Back to Main Menu                      \n",
        f"---------------------------------------------\n",
        sep="",
        end="",
    )
    return input("  Enter choice: ")


def about() -> None:
    clear_screen()
    print(
        f"--------------------------------------------\n",
        f"                   {c.YELLOW2}About{c.END}                    \n",
        f"--------------------------------------------\n",
        f"          Euan's UPLB Resto Reco!           \n",
        f"     Programmed by: Tabamo, Euan Jed S.     \n",
        f"        Started on November 7, 2023         \n",
        f"--------------------------------------------\n",
        sep="",
        end="",
    )
    continue_prompt()


def help() -> None:
    clear_screen()
    print(
        f"{c.GRAY}",
        f"---------------------------------------------\n",
        f"                 Main Menu                   \n",
        f"---------------------------------------------\n",
        f"  1   Manage Gustos                          \n",
        f"  2   Manage Restos                          \n",
        f"  3   Get Recos                              \n",
        f"  A   About                                  \n",
        f"  {c.YELLOW2}H   Help{c.GRAY}                                   \n",
        f"  0   Exit                                   \n",
        f"---------------------------------------------\n",
        f"{c.END}",
        sep="",
        end="",
    )
    print(
        f"--------------------------------------------\n",
        f"                    {c.YELLOW2}Help{c.END}                    \n",
        f"--------------------------------------------\n",
        f"  1   Gustos                                \n",
        f"  2   Restos                                \n",
        f"  3   Recos                                 \n",
        f"  0   Back to Main Menu                     \n",
        f"--------------------------------------------\n",
        sep="",
        end="",
    )
    choice = input("  Enter choice: ")
    if choice == "1":
        h.help_gustos()
    elif choice == "2":
        h.help_restos()
    elif choice == "3":
        h.help_recos()
    elif choice == "0":
        clear_screen()
    else:
        raise_er("Invalid choice!")


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
