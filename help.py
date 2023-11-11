"""
This module contains the functions that display the help menu.
"""

# File Imports
from misc import clear_screen, continue_prompt
import colors as c


def help_gustos() -> None:
    clear_screen()
    print(
        f"{c.GRAY}" f"---------------------------------------------\n",
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
        f"{c.GRAY}" f"--------------------------------------------\n",
        f"                    Help                    \n",
        f"--------------------------------------------\n",
        f"  {c.YELLOW2}1   Gustos{c.GRAY}                                \n",
        f"  2   Restos                                \n",
        f"  3   Recos                                 \n",
        f"  0   Back to Main Menu                     \n",
        f"--------------------------------------------\n",
        f"{c.END}",
        sep="",
        end="",
    )
    print(
        f"---------------------------------------------------------------------------\n",
        f"  {c.YELLOW2}Gustos{c.END} are preference profiles that contain the following attributes:    \n",
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
        f"{c.GRAY}" f"---------------------------------------------\n",
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
        f"{c.GRAY}" f"--------------------------------------------\n",
        f"                    Help                    \n",
        f"--------------------------------------------\n",
        f"  1   Gustos                                \n",
        f"  {c.YELLOW2}2   Restos{c.GRAY}                                \n",
        f"  3   Recos                                 \n",
        f"  0   Back to Main Menu                     \n",
        f"--------------------------------------------\n",
        f"{c.END}",
        sep="",
        end="",
    )
    print(
        f"---------------------------------------------------------------------------\n",
        f"  {c.YELLOW2}Restos{c.END} are dining places with the following attributes:                  \n",
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
        f"{c.GRAY}" f"---------------------------------------------\n",
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
        f"{c.GRAY}" f"--------------------------------------------\n",
        f"                    Help                    \n",
        f"--------------------------------------------\n",
        f"  1   Gustos                                \n",
        f"  2   Restos                                \n",
        f"  {c.YELLOW2}3   Recos{c.GRAY}                                 \n",
        f"  0   Back to Main Menu                     \n",
        f"--------------------------------------------\n",
        f"{c.END}",
        sep="",
        end="",
    )
    print(
        f"---------------------------------------------------------------------------\n",
        f"  {c.YELLOW2}Recos{c.END} are dining place/s recommended by the program based on the user's  \n",
        f"  preferences. The program will recommend resto/s that are within the      \n",
        f'  "gustos" or preference profile of the user.                              \n',
        f"---------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    continue_prompt()
