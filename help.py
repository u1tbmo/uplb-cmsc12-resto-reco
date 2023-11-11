"""
This module contains the functions that display the help menu.
"""

# File Imports
from misc import clear_screen, continue_prompt
import colors as c


def help_gustos() -> None:
    print(
        "---------------------------------------------------------------------------\n",
        "  Gustos are preference profiles that contain the following attributes:    \n",
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
    print(
        "---------------------------------------------------------------------------\n",
        "  Restos are dining places with the following attributes:                  \n",
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
    clear_screen()
    print(
        "---------------------------------------------------------------------------\n",
        "  Recos are dining place/s recommended by the program based on the user's  \n",
        "  preferences. The program will recommend resto/s that are within the      \n",
        '  "gustos" or preference profile of the user.                              \n',
        "---------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    continue_prompt()
