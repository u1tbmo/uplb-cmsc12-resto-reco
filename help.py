"""
This module contains the functions that display the help menu.
"""

# File Imports
from misc import clear_screen, continue_prompt, raise_er
import colors as c
from colors import C1, C2, CE, CD


def help_gustos() -> None:
    clear_screen()
    print(
        f"{CD}",
        f"---------------------------------------------------\n",
        f"                     Main Menu                     \n",
        f"---------------------------------------------------\n",
        f"  1   Manage Gustos                                \n",
        f"  2   Manage Restos                                \n",
        f"  3   Get Recos                                    \n",
        f"  A   About                                        \n",
        f"  {C1}H   Help{CD}                                         \n",
        f"  0   Exit                                         \n",
        f"---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        f"{CD}",
        f"---------------------------------------------------\n",
        f"                        Help                       \n",
        f"---------------------------------------------------\n",
        f"  {C1}1   Gustos{CD}                                       \n",
        f"  2   Restos                                       \n",
        f"  3   Recos                                        \n",
        f"  0   Back to Main Menu                            \n",
        f"---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        f"---------------------------------------------------------------------------\n",
        f"  {C1}Gustos{CE} are preference profiles that contain the following attributes:    \n",
        f"---------------------------------------------------------------------------\n",
        f"  Label = the unique identifier of the gusto                               \n",
        f"  Description = the description of the gusto                               \n",
        f"  Group Size = the number of people the gusto is for                       \n",
        f"  Meal Type = the meal type the gusto is for (breakfast, lunch, dinner)    \n",
        f"  Budget = the budget of the gusto (in pesos)                              \n",
        f"  Max Distance = the maximum distance of the resto from UPLB gate          \n",
        f"  Cuisine Type = the type of cuisine the resto serves                      \n",
        f"  Min Rating = the minimum rating of the resto                             \n",
        f"---------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    continue_prompt()


def help_restos() -> None:
    clear_screen()
    print(
        f"{CD}",
        f"---------------------------------------------------\n",
        f"                     Main Menu                     \n",
        f"---------------------------------------------------\n",
        f"  1   Manage Gustos                                \n",
        f"  2   Manage Restos                                \n",
        f"  3   Get Recos                                    \n",
        f"  A   About                                        \n",
        f"  {C1}H   Help{CD}                                         \n",
        f"  0   Exit                                         \n",
        f"---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        f"{CD}",
        f"---------------------------------------------------\n",
        f"                        Help                       \n",
        f"---------------------------------------------------\n",
        f"  1   Gustos                                       \n",
        f"  {C1}2   Restos{CD}                                       \n",
        f"  3   Recos                                        \n",
        f"  0   Back to Main Menu                            \n",
        f"---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        f"---------------------------------------------------------------------------\n",
        f"  {C1}Restos{CE} are dining places with the following attributes:                  \n",
        f"---------------------------------------------------------------------------\n",
        f"  Name = the unique identifier of the resto                                \n",
        f"  Distance = the distance from UPLB gate to the resto                      \n",
        f"  Cuisine Type = the type of cuisine the resto serves                      \n",
        f"  Meal Type = the meal types the resto serves (breakfast, lunch, dinner)   \n",
        f"  Cost = the average cost of a meal in the resto                           \n",
        f"  Rating = the average rating of the resto                                 \n",
        f"---------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    continue_prompt()


def help_recos() -> None:
    clear_screen()
    print(
        f"{CD}",
        f"---------------------------------------------------\n",
        f"                     Main Menu                     \n",
        f"---------------------------------------------------\n",
        f"  1   Manage Gustos                                \n",
        f"  2   Manage Restos                                \n",
        f"  3   Get Recos                                    \n",
        f"  A   About                                        \n",
        f"  {C1}H   Help{CD}                                         \n",
        f"  0   Exit                                         \n",
        f"---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        f"{CD}",
        f"---------------------------------------------------\n",
        f"                        Help                       \n",
        f"---------------------------------------------------\n",
        f"  1   Gustos                                       \n",
        f"  2   Restos                                       \n",
        f"  {C1}3   Recos{CD}                                        \n",
        f"  0   Back to Main Menu                            \n",
        f"---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        f"---------------------------------------------------------------------------\n",
        f"  {C1}Recos{CE} are dining place/s recommended by the program based on the user's  \n",
        f"  preferences. The program will recommend resto/s that are within the      \n",
        f'  "gustos" or preference profile of the user.                              \n',
        f"---------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    continue_prompt()


if __name__ == "__main__":
    raise_er("You are running a module: help.py")
