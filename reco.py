"""
This module contains the functions for recommending restos.
"""

# Standard Library Imports
import random

# Local Module Imports
from misc import clear_screen, continue_prompt, raise_err
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
        if distance > max_distance and max_distance != -1:
            continue
        if r_cuisine_type != g_cuisine_type and g_cuisine_type != "ANY":
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
        if group_size * cost > budget and budget != -1:
            continue
        if rating < min_rating and min_rating != -1:
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
        raise_err("No Restos to Reco! Add some Restos first!")
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
            raise_err("Invalid gusto label!")
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
        raise_err("Invalid choice!")
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
    label = gusto[0]
    description = gusto[1][0]
    group_size = gusto[1][1]
    meal_type = gusto[1][2].capitalize()
    budget = gusto[1][3] if gusto[1][3] != -1 else "Any"
    max_distance = gusto[1][4] if gusto[1][4] != -1 else "Any"
    cuisine_type = gusto[1][5] if gusto[1][5] != "ANY" else "Any"
    min_rating = gusto[1][6] if gusto[1][6] != -1 else "Any"

    if gusto[0] != "AD,HOC":
        print(f"  Gusto Label: {label}")
        print(f"  Description: {description}")
    print(f"  Number of People: {group_size}")
    print(f"  Meal Type: {meal_type}")
    print(f"  Budget: {budget}")
    print(f"  Maximum Distance: {max_distance}")
    print(f"  Cuisine Type: {cuisine_type}")
    print(f"  Minimum Rating: {min_rating}")
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
        rating = f"{value[4]} / 5"
        cost = f"{value[3]:.2f}"
        print(
            f"  {name:<16}   {value[0]:>22.2f}m   {value[1].capitalize():^13}   {meal_types:<24}   {cost:>10}   {rating:^10}  "
        )
    print(
        "-------------------------------------------------------------------------------------------------------------------"
    )
    continue_prompt()
