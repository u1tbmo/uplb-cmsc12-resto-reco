"""
This module contains miscellaneous functions.
"""

# Standard Library Imports
import os


def clear_screen() -> None:
    """Clears the screen, depending on the OS."""
    os.system("cls" if os.name == "nt" else "clear")


def continue_prompt() -> None:
    """Prompts the user to press enter to continue."""
    input("| Press Enter to continue...")
    clear_screen()


def raise_er(message: str) -> None:
    """Prints an error message and prompts the user to press enter to continue."""
    print(f"| ERROR: {message}")
    continue_prompt()
