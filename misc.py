"""
This module contains miscellaneous functions.
"""

# Standard Library Imports
import os

# File Imports
import colors as c


def clear_screen() -> None:
    """Clears the screen, depending on the OS."""
    os.system("cls" if os.name == "nt" else "clear")


def continue_prompt() -> None:
    """Prompts the user to press enter to continue."""
    input(f"{c.BLINK2}  Press Enter to continue...{c.END}")
    clear_screen()


def info(message: str) -> None:
    """Prints an info message."""
    print(f"{c.GREEN}  INFO: {message}{c.END}")


def raise_er(message: str) -> None:
    """Prints an error message and prompts the user to press enter to continue."""
    print(f"{c.RED}  ERROR: {message}{c.END}")
    continue_prompt()


def print_format_table():
    """Prints table of formatted text format options."""
    x = 0
    for i in range(24):
        colors = ""
        for j in range(5):
            code = str(x + j)
            colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
        print(colors)
        x = x + 5


if __name__ == "__main__":
    raise_er("You are running a module: misc.py")
