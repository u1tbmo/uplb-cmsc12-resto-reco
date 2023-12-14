"""
This program recommends dining place/s based on the preferences of the user.
"""
# Tabamo, Euan Jed S.   B-1L
# Project

# Local Module Imports
import save_load as sl
import gusto as g
import resto as r
import reco as rc
import help as h
from colors import C1, C2, CE, CD
from misc import (
    clear_screen,
    continue_prompt,
    raise_err,
    load_colors,
    check_window_size,
)

# Global Variables
restos: dict[str, list] = {}
gustos: dict[str, list] = {}


def exit_program() -> None:
    """Prints an exit message."""
    clear_screen()
    message = (
        "═══════════════════════════════════════════════════\n"
        f"                {C1}See you next time!{CE}                \n",
        f"              {C2}From Euan's Resto Reco!{CE}             \n",
        "═══════════════════════════════════════════════════\n",
    )
    print("".join(message), end="")
    sl.save(restos, gustos)
    exit()


def print_main_menu() -> str:
    """Prints the main menu and prompts the user for a choice.

    Returns:
        str: the choice of the user
    """
    print(
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}Main Menu{CE}                     \n",
        "═══════════════════════════════════════════════════\n",
        "  1   Manage Gustos                                \n",
        "  2   Manage Restos                                \n",
        "  3   Get Recos                                    \n",
        "  A   About                                        \n",
        "  H   Help                                         \n",
        "  X   Exit                                         \n",
        "═══════════════════════════════════════════════════\n",
        f"{CE}",
        sep="",
        end="",
    )
    return input("  Enter choice: ")


def print_gusto_menu() -> str:
    """Prints the menu for managing gustos and prompts the user for a choice.

    Returns:
        str: the choice of the user
    """
    clear_screen()
    print(
        f"{CD}",
        "═══════════════════════════════════════════════════\n",
        "                     Main Menu                     \n",
        "═══════════════════════════════════════════════════\n",
        f"  {C1}1   Manage Gustos{CD}                                \n",
        "  2   Manage Restos                                \n",
        "  3   Get Recos                                    \n",
        "  A   About                                        \n",
        "  H   Help                                         \n",
        "  X   Exit                                         \n",
        "═══════════════════════════════════════════════════\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        "═══════════════════════════════════════════════════\n",
        f"                   {C1}Manage Gustos{CE}                   \n",
        "═══════════════════════════════════════════════════\n",
        "  1   Add Gusto                                    \n",
        "  2   Edit Gusto                                   \n",
        "  3   Delete Gusto                                 \n",
        "  4   Display Gustos                               \n",
        "  5   View a Gusto                                 \n",
        "  B   Back to Main Menu                            \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    return input("  Enter choice: ")


def print_resto_menu() -> str:
    """Prints the menu for managing restos and prompts the user for a choice.

    Returns:
        str: the choice of the user
    """
    clear_screen()
    print(
        f"{CD}",
        "═══════════════════════════════════════════════════\n",
        "                     Main Menu                     \n",
        "═══════════════════════════════════════════════════\n",
        "  1   Manage Gustos                                \n",
        f"  {C1}2   Manage Restos{CD}                                \n",
        "  3   Get Recos                                    \n",
        "  A   About                                        \n",
        "  H   Help                                         \n",
        "  X   Exit                                         \n",
        "═══════════════════════════════════════════════════\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        "═══════════════════════════════════════════════════\n",
        f"                   {C1}Manage Restos{CE}                   \n",
        "═══════════════════════════════════════════════════\n",
        "  1   Add Resto                                    \n",
        "  2   Edit Resto                                   \n",
        "  3   Delete Resto                                 \n",
        "  4   Display Restos                               \n",
        "  5   View a Resto                                 \n",
        "  B   Back to Main Menu                            \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    return input("  Enter choice: ")


def print_about_screen() -> None:
    """Prints the about screen."""
    clear_screen()
    print(
        "═══════════════════════════════════════════════════\n",
        f"                       {C1}About{CE}                       \n",
        "═══════════════════════════════════════════════════\n",
        "             Euan's UPLB Resto Reco!               \n",
        "        Programmed by: Tabamo, Euan Jed S.         \n",
        "           Started on November 7, 2023             \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    continue_prompt()


def manage_gustos(gustos_dict: dict[str, list]) -> dict[str, list]:
    """Manages the gustos dictionary.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos to be managed

    Returns:
        dict[str, list]: the dictionary of gustos after possible changes
    """
    while True:
        choice = print_gusto_menu()
        match choice:
            case "1":
                g.add_gustos(gustos_dict)
                break
            case "2":
                g.edit_gustos(gustos_dict)
                break
            case "3":
                g.delete_gustos(gustos_dict)
                break
            case "4":
                clear_screen()
                g.display_gustos(gustos_dict)
                if gustos_dict:
                    continue_prompt()
                break
            case "5":
                g.view_gusto(gustos_dict)
                break
            case "B" | "b":
                break
            case _:
                raise_err("Invalid choice!")
                continue
    return gustos_dict


def manage_restos(restos_dict: dict[str, list]) -> dict[str, list]:
    """Manages the restos dictionary.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos to be managed

    Returns:
        dict[str, list]: the dictionary of restos after possible changes
    """
    while True:
        choice = print_resto_menu()
        match choice:
            case "1":
                r.add_restos(restos_dict)
                break
            case "2":
                r.edit_restos(restos_dict)
                break
            case "3":
                r.delete_restos(restos_dict)
                break
            case "4":
                clear_screen()
                r.display_restos(restos_dict)
                if restos_dict:
                    continue_prompt()
                    break
            case "5":
                r.view_resto(restos_dict)
                break
            case "B" | "b":
                break
            case _:
                raise_err("Invalid choice!")
                continue
    return restos_dict


def main() -> None:
    """The main function."""
    load_colors()
    sl.load(restos, gustos)
    check_window_size()
    while True:
        clear_screen()
        choice = print_main_menu()
        match choice:
            case "X" | "x":
                exit_program()
                break
            case "1":
                manage_gustos(gustos)
            case "2":
                manage_restos(restos)
            case "3":
                rc.get_recos(restos, gustos)
            case "A" | "a":
                print_about_screen()
            case "H" | "h":
                h.help_screen()
            case "C" | "c":
                clear_screen()
            case _:
                raise_err("Invalid choice!")
                clear_screen()
        sl.save(restos, gustos)


if __name__ == "__main__":
    main()
