"""
This file contains the functions for saving and loading the restos and gustos.
"""

# Standard Library Import
import os

# Data Paths
file_dir = os.path.dirname(__file__)
DATA_PATH = os.path.join(file_dir, "data")
RESTO_PATH = os.path.join(DATA_PATH, "resto.dat")
GUSTO_PATH = os.path.join(DATA_PATH, "gusto.dat")

# Creates a directory for data if it doesn't exist
if not os.path.exists(DATA_PATH):
    os.mkdir(DATA_PATH)


def load_restos(restos_dict: dict[str, list]) -> dict[str, list]:
    """Loads the restos from resto.dat.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos

    Returns:
        dict[str, list]: the dictionary of restos
    """
    # Create resto.dat if it doesn't exist
    open(RESTO_PATH, "a", encoding="utf-8").close()

    # Read resto.dat
    fh = open(RESTO_PATH, "r", encoding="utf-8")
    for line in fh:
        name, distance, cuisine_type, meal_type, cost, rating = line.split("~")
        restos_dict[name] = [
            float(distance),
            cuisine_type.split(","),
            meal_type,
            float(cost),
            float(rating),
        ]
    fh.close()
    return restos_dict


def load_gustos(gustos_dict: dict[str, list]) -> dict[str, list]:
    """Loads the gustos from gusto.dat.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos

    Returns:
        dict[str, list]: the dictionary of gustos
    """
    # Create gusto.dat if it doesn't exist
    open(GUSTO_PATH, "a", encoding="utf-8").close()

    # Read gusto.dat
    fh = open(GUSTO_PATH, "r", encoding="utf-8")
    for line in fh:
        (
            label,
            description,
            group_size,
            meal_type,
            budget,
            max_distance,
            cuisine_type,
            min_rating,
        ) = line.split("~")

        gustos_dict[label] = [
            description,
            int(group_size),
            meal_type,
            float(budget) if budget != "None" else None,
            float(max_distance) if max_distance != "None" else None,
            cuisine_type if cuisine_type != "None" else None,
            float(min_rating) if min_rating != "None\n" else None,
        ]
    fh.close()
    return gustos_dict


def load(restos_dict: dict[str, list], gustos_dict: dict[str, list]) -> tuple:
    """Loads the restos and gustos from their respective files.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos
        gustos_dict (dict[str, list]): the dictionary of gustos

    Returns:
        tuple: the dictionary of restos and gustos
    """

    # This function simply calls load_restos and load_gustos
    restos_dict = load_restos(restos_dict)
    gustos_dict = load_gustos(gustos_dict)
    return (restos_dict, gustos_dict)


def save_restos(restos_dict: dict[str, list]) -> None:
    """Saves the restos to resto.dat.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos
    """
    fh = open(RESTO_PATH, "w", encoding="utf-8")
    for name, value in restos_dict.items():
        fh.write(
            f"{name}~{value[0]}~{','.join(value[1])}~{value[2]}~{value[3]}~{value[4]}\n"
        )
    fh.close()


def save_gustos(gustos_dict: dict[str, list]) -> None:
    """Saves the gustos to gusto.dat.

    Args:
        gustos_dict (dict[str, list]): the dictionary of gustos
    """
    fh = open(GUSTO_PATH, "w", encoding="utf-8")
    for label, value in gustos_dict.items():
        fh.write(
            f"{label}~{value[0]}~{value[1]}~{value[2]}~{value[3]}~{value[4]}~{value[5]}~{value[6]}\n"
        )
    fh.close()


def save(restos_dict: dict[str, list], gustos_dict: dict[str, list]) -> None:
    """Saves the restos and gustos to their respective files.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos
        gustos_dict (dict[str, list]): the dictionary of gustos
    """

    # This function simply calls save_restos and save_gustos
    save_restos(restos_dict)
    save_gustos(gustos_dict)
