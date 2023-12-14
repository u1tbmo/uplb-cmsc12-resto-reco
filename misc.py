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
    os.system("cls" if os.name == "nt" else "clear")


def continue_prompt() -> None:
    """Prompts the user to press enter to continue."""
    getpass.getpass(f"{c.BOLD}{c.BLINK2}  Press Enter to continue...{c.END}")
    clear_screen()


def info(message: str) -> None:
    """Prints an info message."""
    print(f"{c.GREEN}  INFO: {message}{c.END}")


def raise_err(message: str) -> None:
    """Prints an error message and prompts the user to press enter to continue."""
    print(f"{c.RED}  ERROR: {message}{c.END}")
    continue_prompt()


def print_err(message: str) -> None:
    """Prints an error message."""
    print(f"{c.RED}  ERROR: {message}{c.END}")


def load_colors() -> None:
    """Ensures that the terminal supports ANSI escape sequences."""
    os.system("")


def check_window_size() -> None:
    """Checks if the window size is at least 128 columns."""

    while True:
        clear_screen()
        current_size_cols = os.get_terminal_size().columns
        current_size_rows = os.get_terminal_size().lines
        if current_size_cols < 128 or current_size_rows < 22:
            message = (
                f"{c.C1}═══════════════════════════════════════════════════\n"
                "        Please resize your window to ensure        \n"
                "          you get the intended experience          \n"
                f"═══════════════════════════════════════════════════{c.CE}\n"
            )
            if current_size_cols < 128:
                message += f"{c.RED}  Columns: {current_size_cols} < 128 {c.CE}\n"
            if current_size_rows < 22:
                message += f"{c.RED}  Rows: {current_size_rows} < 22 {c.CE}\n"
            print("".join(message), end="")
            continue_prompt()
        else:
            break
