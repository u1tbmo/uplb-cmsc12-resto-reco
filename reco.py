"""
This module contains the functions for recommending restos.
"""

# Standard Library Imports
import random

# File Imports
import colors as c
from misc import clear_screen, continue_prompt, raise_er
import gusto as g


def recommend_restos(restos_dict: dict[str, list], gusto: tuple) -> list:
    recos = []
    label, [
        description,
        group_size,
        g_meal_type,
        budget,
        max_distance,
        g_cuisine_type,
        min_rating,
    ] = gusto
    for name, [
        distance,
        r_cuisine_type,
        r_meal_type,
        cost,
        rating,
    ] in restos_dict.items():
        if distance > max_distance:
            continue
        if g_cuisine_type != "ANY" and r_cuisine_type != g_cuisine_type:
            continue

        meal_types = []
        for choice in r_meal_type:
            if choice == "B":
                meal_types.append("BREAKFAST")
            elif choice == "L":
                meal_types.append("LUNCH")
            elif choice == "D":
                meal_types.append("DINNER")
        if g_meal_type not in meal_types:
            continue
        if group_size * cost > budget:
            continue
        if rating < min_rating:
            continue
        recos.append(name)

    while len(recos) > 3:
        recos.pop(random.randint(0, len(recos) - 1))
    return recos


def get_recos(restos_dict: dict[str, list], gustos_dict: dict[str, list]) -> None:
    if not restos_dict:
        raise_er("No Restos to Reco! Add some Restos first!")
        return
    clear_screen()
    print(
        f"{c.GRAY}",
        f"---------------------------------------------\n",
        f"                 Main Menu                   \n",
        f"---------------------------------------------\n",
        f"  1   Manage Gustos                          \n",
        f"  2   Manage Restos                          \n",
        f"  {c.YELLOW2}3   Get Recos{c.GRAY}                              \n",
        f"  A   About                                  \n",
        f"  H   Help                                   \n",
        f"  0   Exit                                   \n",
        f"---------------------------------------------\n",
        f"{c.END}",
        sep="",
        end="",
    )
    print(
        f"---------------------------------------------------\n",
        f"                     {c.YELLOW2}Get Recos{c.END}                     \n",
        f"---------------------------------------------------\n",
        f"  1   Get Reco/s from an Existing Gusto            \n",
        f"  2   Get Reco/s from an Ad Hoc Gusto              \n",
        f"  0   Back to Main Menu                            \n",
        f"---------------------------------------------------\n",
        sep="",
        end="",
    )

    choice = input("  Enter choice: ")
    if choice == "1":
        clear_screen()
        print(
            f"---------------------------------------------------\n",
            f"         {c.YELLOW2}Get Reco/s from an Existing Gusto{c.END}         \n",
            f"---------------------------------------------------\n",
            sep="",
            end="",
        )
        g.display_gustos_simple(gustos_dict)
        label = input("  Enter gusto label: ").strip().upper()
        if label not in gustos_dict:
            raise_er("Invalid gusto label!")
            return
        gusto = (label, gustos_dict[label])
        recos = recommend_restos(restos_dict, gusto)
    elif choice == "2":
        gusto = g.ad_hoc_gusto()
        if gusto is None:
            return
        recos = recommend_restos(restos_dict, gusto)
    elif choice == "0":
        clear_screen()
        return
    else:
        raise_er("Invalid choice!")
        return

    if not recos:
        print("---------------------------------------------------")
        print("  We cannot find a resto match for your gusto!     ")
        print("  Want to find a match? Try:                       ")
        print("  - Adding more Restos                             ")
        print("  - A different Gusto                              ")
        print("  - Increasing your Gusto's budget                 ")
        print("  - Increasing your Gusto's max distance           ")
        print("  - Changing your Gusto's cuisine type             ")
        print("  - Decreasing your Gusto's group size             ")
        print("  - Decreasing your Gusto's minimum rating         ")
        print("---------------------------------------------------")
        continue_prompt()
        return

    clear_screen()
    print("--------------------------------------------")
    print("    We Reco these Restos for your Gusto!    ")
    print("--------------------------------------------")
    print("                   Gusto                    ")
    print("--------------------------------------------")
    if gusto[0] != "AD,HOC":
        print(f"  Label: {gusto[0]}")
        print(f"  Description: {gusto[1][0]}")
    print(f"  Group Size: {gusto[1][1]}")
    print(f"  Meal Type: {gusto[1][2]}")
    print(f"  Budget: {gusto[1][3]}")
    print(f"  Max Distance: {gusto[1][4]}")
    print(f"  Cuisine Type: {gusto[1][5]}")
    print(f"  Min Rating: {gusto[1][6]}")
    print("--------------------------------------------")
    print("                   Recos                    ")
    print("--------------------------------------------")
    for name in recos:
        meal_types = []
        for choice in restos_dict[name][2]:
            if choice == "B":
                meal_types.append("BREAKFAST")
            elif choice == "L":
                meal_types.append("LUNCH")
            elif choice == "D":
                meal_types.append("DINNER")
        print(f"  Resto: {name}")
        print(f"  Distance: {restos_dict[name][0]}")
        print(f"  Cuisine Type: {restos_dict[name][1]}")
        print(f"  Meal Type: {", ".join(meal_types)}")
        print(f"  Cost: {restos_dict[name][3]}")
        print(f"  Rating: {restos_dict[name][4]}")
        print("--------------------------------------------")
    continue_prompt()


if __name__ == "__main__":
    raise_er("You are running a module: reco.py")
