"""
This module contains the functions for recommending restos.
"""

# Standard Library Imports
import random

# Local Module Imports
from misc import clear_screen, continue_prompt, raise_er
import gusto as g
from colors import C1, C2, CE, CD


def recommend_restos(restos_dict: dict[str, list], gusto: tuple) -> list:
    """Recommends restos based on the given gusto.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos
        gusto (tuple): the gusto to be used for recommending restos

    Returns:
        list: the list of recommended restos
    """
    recos = []
    _, [
        _,
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
        for char in r_meal_type:
            if char == "B":
                meal_types.append("BREAKFAST")
            elif char == "L":
                meal_types.append("LUNCH")
            elif char == "D":
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
    """Gets the recos from the user.

    Args:
        restos_dict (dict[str, list]): the dictionary of restos
        gustos_dict (dict[str, list]): the dictionary of gustos
    """
    if not restos_dict:
        raise_er("No Restos to Reco! Add some Restos first!")
        return
    clear_screen()
    print(
        f"{CD}",
        "---------------------------------------------------\n",
        "                     Main Menu                     \n",
        "---------------------------------------------------\n",
        "  1   Manage Gustos                                \n",
        "  2   Manage Restos                                \n",
        f"  {C1}3   Get Recos{CD}                                    \n",
        "  A   About                                        \n",
        "  H   Help                                         \n",
        "  0   Exit                                         \n",
        "---------------------------------------------------\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        "---------------------------------------------------\n",
        f"                     {C1}Get Recos{CE}                     \n",
        "---------------------------------------------------\n",
        "  1   Get Reco/s from an Existing Gusto            \n",
        "  2   Get Reco/s from an Ad Hoc Gusto              \n",
        "  0   Back to Main Menu                            \n",
        "---------------------------------------------------\n",
        sep="",
        end="",
    )

    choice = input("  Enter choice: ")
    if choice == "1":
        clear_screen()
        print(
            "---------------------------------------------------\n",
            f"         {C1}Get Reco/s from an Existing Gusto{CE}         \n",
            "---------------------------------------------------\n",
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
        print(
            "---------------------------------------------------\n",
            "  We cannot find a resto match for your gusto!     \n",
            "  Want to find a match? Try:                       \n",
            "  - Adding more Restos                             \n",
            "  - A different Gusto                              \n",
            "  - Increasing your Gusto's budget                 \n",
            "  - Increasing your Gusto's max distance           \n",
            "  - Changing your Gusto's cuisine type             \n",
            "  - Decreasing your Gusto's group size             \n",
            "  - Decreasing your Gusto's minimum rating         \n",
            "---------------------------------------------------\n",
            sep="",
            end="",
        )
        continue_prompt()
        return

    clear_screen()
    print(
        "-------------------------------------------------------------------------------------------------------------------\n",
        f"                                 {C1}We Reco the Following Restos based on your Gusto!{CE}                                 \n",
        "-------------------------------------------------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    print(
        "-------------------------------------------------------------------------------------------------------------------\n",
        f"                                                       {C1}Gusto{CE}                                                       \n",
        "-------------------------------------------------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    if gusto[0] != "AD,HOC":
        print(f"  Label: {gusto[0]}")
        print(f"  Description: {gusto[1][0]}")
    print(f"  Group Size: {gusto[1][1]}")
    print(f"  Meal Type: {gusto[1][2].capitalize()}")
    print(f"  Budget: {gusto[1][3]}")
    print(f"  Max Distance: {gusto[1][4]}")
    print(f"  Cuisine Type: {gusto[1][5]}")
    print(f"  Min Rating: {gusto[1][6]}")
    print(
        "-------------------------------------------------------------------------------------------------------------------"
    )
    print(
        "-------------------------------------------------------------------------------------------------------------------\n",
        f"                                                       {C1}Recos{CE}                                                       \n",
        "-------------------------------------------------------------------------------------------------------------------\n",
        f"{C2}        Name         Distance from UPLB Gate      Cuisine             Meal Types             Cost        Rating    {CE}\n",
        "-------------------------------------------------------------------------------------------------------------------\n",
        sep="",
        end="",
    )
    for name in recos:
        value = restos_dict[name]
        meal_types = ""
        for char in value[2]:
            if char == "B":
                meal_types += "Breakfast, "
            elif char == "L":
                meal_types += "Lunch, "
            elif char == "D":
                meal_types += "Dinner, "
        meal_types = meal_types.rstrip(", ")
        if value[2] != "BLD":
            meal_types = f" {meal_types} "
        print(
            f"  {name:<16}   {value[0]:>22.2f}m   {value[1]:^13}   {meal_types:^24}   {value[3]:>10.2f}   {value[4]:^10.1f}  "
        )
    print(
        "-------------------------------------------------------------------------------------------------------------------"
    )
    continue_prompt()
