"""
This module contains miscellaneous functions.
"""

# Standard Library Imports
import os
import getpass

# Local Module Imports
import colors as c


def clear_screen() -> None:
    """Clears the screen, depending on the OS."""

    # Uses the cls command if the OS is Windows, otherwise uses the clear command
    # This is for compatibility with cmd, which doesn't support clear.
    os.system("cls" if os.name == "nt" else "clear")


def continue_prompt() -> None:
    """Prompts the user to press enter to continue."""

    # Uses the getpass module to hide the input of the user.
    # This is to prevent the user from seeing the input and to simulate a pause.
    getpass.getpass(f"{c.BOLD}{c.BLINK2}  Press Enter to continue...{c.END}")
    clear_screen()


def info(message: str) -> None:
    """Prints an info message."""

    # Predefined format for info messages
    print(f"{c.GREEN}  INFO: {message}{c.END}")


def raise_err(message: str) -> None:
    """Prints an error message and prompts the user to press enter to continue."""

    # Predefined format for error messages
    print(f"{c.RED}  ERROR: {message}{c.END}")
    continue_prompt()


def print_err(message: str) -> None:
    """Prints an error message."""

    # Predefined format for error messages
    print(f"{c.RED}  ERROR: {message}{c.END}")


def load_colors() -> None:
    """Ensures that the terminal supports ANSI escape sequences."""

    # System call to set the terminal to support ANSI escape sequences
    # Stack Overflow: https://stackoverflow.com/a/54955094

    # Colors Tested on Windows Terminal: Powershell 7, Windows Powershell, Windows Command Prompt, Ubuntu on WSL
    os.system("")


def check_window_size() -> None:
    """Checks if the window size is the intended size."""

    # Since displayed tables can be quite large, we need to ensure that the window size is large enough to display the table.
    # This function checks if the window size is large enough to display the table.
    while True:
        clear_screen()
        current_size_cols = os.get_terminal_size().columns
        current_size_rows = os.get_terminal_size().lines
        if current_size_cols < 128 or current_size_rows < 25:
            message = (
                f"{c.C1}═══════════════════════════════════════════════════\n"
                "        Please resize your window to ensure        \n"
                "          you get the intended experience          \n"
                f"═══════════════════════════════════════════════════{c.CE}\n"
            )
            if current_size_cols < 128:
                message += f"{c.RED}  Columns: {current_size_cols} < 128 {c.CE}\n"
            if current_size_rows < 25:
                message += f"{c.RED}  Rows: {current_size_rows} < 25 {c.CE}\n"
            print("".join(message), end="")
            continue_prompt()
        else:
            break


def capitalize_words(string: str) -> None:
    """Capitalizes words in a string.

    Args:
        string (str): The capitalized string.
    """

    # Splits the string into words, capitalizes each word, and joins the words back together.
    if not string:
        return ""
    words = string.split(" ")
    for idx, word in enumerate(words):
        words[idx] = word.capitalize()
    return " ".join(words)
