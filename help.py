"""
This module contains the functions that display the help menu.
"""

# File Imports
from misc import clear_screen, continue_prompt, raise_er
from colors import C1, CE, CD


def help_screen() -> None:
    """Prints the help menu, asks for a choice, and prints the corresponding help screen."""
    clear_screen()
    print(
        f"{CD}",
        "---------------------------------------------------\n",
        "                     Main Menu                     \n",
        "---------------------------------------------------\n",
        "  1   Manage Gustos                                \n",
        "  2   Manage Restos                                \n",
        "  3   Get Recos                                    \n",
        "  A   About                                        \n",
        f"  {C1}H   Help{CD}                                         \n",
        "  0   Exit                                         \n",
        "---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        "---------------------------------------------------\n",
        f"                        {C1}Help{CE}                       \n",
        "---------------------------------------------------\n",
        "  1   Gustos                                       \n",
        "  2   Restos                                       \n",
        "  3   Recos                                        \n",
        "  0   Back to Main Menu                            \n",
        "---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    choice = input("  Enter choice: ")
    if choice == "1":
        help_gustos()
    elif choice == "2":
        help_restos()
    elif choice == "3":
        help_recos()
    elif choice == "0":
        clear_screen()
    else:
        raise_er("Invalid choice!")


def help_gustos() -> None:
    """Displays the help menu for gustos."""
    clear_screen()
    print(
        f"{CD}",
        "---------------------------------------------------\n",
        "                     Main Menu                     \n",
        "---------------------------------------------------\n",
        "  1   Manage Gustos                                \n",
        "  2   Manage Restos                                \n",
        "  3   Get Recos                                    \n",
        "  A   About                                        \n",
        f"  {C1}H   Help{CD}                                         \n",
        "  0   Exit                                         \n",
        "---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        f"{CD}",
        "---------------------------------------------------\n",
        "                        Help                       \n",
        "---------------------------------------------------\n",
        f"  {C1}1   Gustos{CD}                                       \n",
        "  2   Restos                                       \n",
        "  3   Recos                                        \n",
        "  0   Back to Main Menu                            \n",
        "---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        "---------------------------------------------------------------------------\n",
        f"  {C1}Gustos{CE} are preference profiles that contain the following attributes:    \n",
        "---------------------------------------------------------------------------\n",
        "  Label = the unique identifier of the gusto                               \n",
        "  Description = the description of the gusto                               \n",
        "  Group Size = the number of people the gusto is for                       \n",
        "  Meal Type = the meal type the gusto is for (breakfast, lunch, dinner)    \n",
        "  Budget = the budget of the gusto (in pesos)                              \n",
        "  Max Distance = the maximum distance of the resto from UPLB gate          \n",
        "  Cuisine Type = the type of cuisine the resto serves                      \n",
        "  Min Rating = the minimum rating of the resto                             \n",
        "---------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    continue_prompt()


def help_restos() -> None:
    """Displays the help menu for restos."""
    clear_screen()
    print(
        f"{CD}",
        "---------------------------------------------------\n",
        "                     Main Menu                     \n",
        "---------------------------------------------------\n",
        "  1   Manage Gustos                                \n",
        "  2   Manage Restos                                \n",
        "  3   Get Recos                                    \n",
        "  A   About                                        \n",
        f"  {C1}H   Help{CD}                                         \n",
        "  0   Exit                                         \n",
        "---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        f"{CD}",
        "---------------------------------------------------\n",
        "                        Help                       \n",
        "---------------------------------------------------\n",
        "  1   Gustos                                       \n",
        f"  {C1}2   Restos{CD}                                       \n",
        "  3   Recos                                        \n",
        "  0   Back to Main Menu                            \n",
        "---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        "---------------------------------------------------------------------------\n",
        f"  {C1}Restos{CE} are dining places with the following attributes:                  \n",
        "---------------------------------------------------------------------------\n",
        "  Name = the unique identifier of the resto                                \n",
        "  Distance = the distance from UPLB gate to the resto                      \n",
        "  Cuisine Type = the type of cuisine the resto serves                      \n",
        "  Meal Type = the meal types the resto serves (breakfast, lunch, dinner)   \n",
        "  Cost = the average cost of a meal in the resto                           \n",
        "  Rating = the average rating of the resto                                 \n",
        "---------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    continue_prompt()


def help_recos() -> None:
    """Displays the help menu for recos."""
    clear_screen()
    print(
        f"{CD}",
        "---------------------------------------------------\n",
        "                     Main Menu                     \n",
        "---------------------------------------------------\n",
        "  1   Manage Gustos                                \n",
        "  2   Manage Restos                                \n",
        "  3   Get Recos                                    \n",
        "  A   About                                        \n",
        f"  {C1}H   Help{CD}                                         \n",
        "  0   Exit                                         \n",
        "---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        f"{CD}",
        "---------------------------------------------------\n",
        "                        Help                       \n",
        "---------------------------------------------------\n",
        "  1   Gustos                                       \n",
        "  2   Restos                                       \n",
        f"  {C1}3   Recos{CD}                                        \n",
        "  0   Back to Main Menu                            \n",
        "---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        "---------------------------------------------------------------------------\n",
        f"  {C1}Recos{CE} are dining place/s recommended by the program based on the user's  \n",
        "  preferences. The program will recommend resto/s that are within the      \n",
        '  "gustos" or preference profile of the user.                              \n',
        "---------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    continue_prompt()
