"""
This file contains the functions for saving and loading the restos and gustos.
"""

# Standard Library Import
import os

# Paths for the data files
file_dir = os.path.dirname(__file__)
DATA_PATH = os.path.join(file_dir, "data")
RESTO_PATH = os.path.join(DATA_PATH, "resto.dat")
GUSTO_PATH = os.path.join(DATA_PATH, "gusto.dat")

if not os.path.exists(DATA_PATH):
    os.mkdir(DATA_PATH)


def load_restos(restos_dict: dict[str, list]) -> dict[str, list]:
    # Create resto.dat if it doesn't exist
    fh = open(RESTO_PATH, "a", encoding="utf-8")
    fh.close()

    # Read resto.dat
    fh = open(RESTO_PATH, "r", encoding="utf-8")
    for line in fh:
        name, distance, cuisine_type, meal_type, cost, rating = line.split(",")
        restos_dict[name] = [
            float(distance),
            cuisine_type,
            meal_type,
            float(cost),
            float(rating),
        ]
    fh.close()
    return restos_dict


def load_gustos(gustos_dict: dict[str, list]) -> dict[str, list]:
    # Create gusto.dat if it doesn't exist
    fh = open(GUSTO_PATH, "a", encoding="utf-8")
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
        ) = line.split(",")

        gustos_dict[label] = [
            description,
            int(group_size),
            meal_type,
            float(budget),
            float(max_distance),
            cuisine_type,
            float(min_rating),
        ]
    fh.close()
    return gustos_dict


def load(restos_dict: dict[str, list], gustos_dict: dict[str, list]) -> tuple:
    restos_dict = load_restos(restos_dict)
    gustos_dict = load_gustos(gustos_dict)
    return (restos_dict, gustos_dict)


def save_restos(restos_dict: dict[str, list]) -> None:
    fh = open(RESTO_PATH, "w", encoding="utf-8")
    for name, value in restos_dict.items():
        fh.write(f"{name},{value[0]},{value[1]},{value[2]},{value[3]},{value[4]}\n")
    fh.close()


def save_gustos(gustos_dict: dict[str, list]) -> None:
    fh = open(GUSTO_PATH, "w", encoding="utf-8")
    for label, value in gustos_dict.items():
        fh.write(
            f"{label},{value[0]},{value[1]},{value[2]},{value[3]},{value[4]},{value[5]},{value[6]}\n"
        )
    fh.close()


def save(restos_dict: dict[str, list], gustos_dict: dict[str, list]) -> None:
    save_restos(restos_dict)
    save_gustos(gustos_dict)
