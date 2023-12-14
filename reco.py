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
        meal_types = []
        for char in r_meal_type:
            if char == "B":
                meal_types.append("Breakfast")
            elif char == "L":
                meal_types.append("Lunch")
            elif char == "D":
                meal_types.append("Dinner")
        if g_meal_type not in meal_types:
            continue
        if budget is not None and budget < cost * group_size:
            continue
        if max_distance is not None and max_distance < distance:
            continue
        if g_cuisine_type is not None and g_cuisine_type not in r_cuisine_type:
            continue
        if min_rating is not None and rating < min_rating:
            continue
        recos.append(name)

    # while len(recos) > 3:
    #     recos.pop(random.randint(0, len(recos) - 1))
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
        "═══════════════════════════════════════════════════\n",
        "                     Main Menu                     \n",
        "═══════════════════════════════════════════════════\n",
        "  1   Manage Gustos                                \n",
        "  2   Manage Restos                                \n",
        f"  {C1}3   Get Recos{CD}                                    \n",
        "  A   About                                        \n",
        "  H   Help                                         \n",
        "  X   Exit                                         \n",
        "═══════════════════════════════════════════════════\n",
        f"{CE}",
        sep="",
        end="",
    )
    print(
        "═══════════════════════════════════════════════════\n",
        f"                     {C1}Get Recos{CE}                     \n",
        "═══════════════════════════════════════════════════\n",
        f"  {C2}1{CE}   Get Reco/s from an Existing Gusto            \n",
        f"  {C2}2{CE}   Get Reco/s from an Ad Hoc Gusto              \n",
        f"  {C2}B{CE}   Back to Main Menu                            \n",
        "═══════════════════════════════════════════════════\n",
        sep="",
        end="",
    )

    choice = input("  Enter choice: ")
    match choice:
        case "1":
            clear_screen()
            print(
                "═══════════════════════════════════════════════════\n",
                f"         {C1}Get Reco/s from an Existing Gusto{CE}         \n",
                "═══════════════════════════════════════════════════\n",
                sep="",
                end="",
            )
            g.display_gustos(gustos_dict)
            label = input("  Enter gusto label: ").strip().upper()
            if label not in gustos_dict:
                raise_err("Invalid gusto label!")
                return
            gusto = (label, gustos_dict[label])
            recos = recommend_restos(restos_dict, gusto)
        case "2":
            gusto = g.ad_hoc_gusto()
            if gusto is None:
                return
            recos = recommend_restos(restos_dict, gusto)
        case "B" | "b":
            clear_screen()
            return
        case _:
            raise_err("Invalid choice!")
            return

    if not recos:
        print(
            "═══════════════════════════════════════════════════\n",
            "  We cannot find a resto match for your gusto!     \n",
            "  Want to find a match? Try:                       \n",
            "  - Adding more Restos                             \n",
            "  - A different Gusto                              \n",
            "  - Increasing your Gusto's budget                 \n",
            "  - Increasing your Gusto's max distance           \n",
            "  - Changing your Gusto's cuisine type             \n",
            "  - Decreasing your Gusto's group size             \n",
            "  - Decreasing your Gusto's minimum rating         \n",
            "═══════════════════════════════════════════════════\n",
            sep="",
            end="",
        )
        continue_prompt()
        return

    clear_screen()
    print(
        "═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        f"                                 {C1}We Reco the Following Restos based on your Gusto!{CE}                                 \n",
        "═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    print(
        "═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        f"                                                       {C1}Gusto{CE}                                                       \n",
        "═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    label = gusto[0]
    description = gusto[1][0]
    group_size = gusto[1][1]
    meal_type = gusto[1][2].capitalize()
    budget = gusto[1][3] if gusto[1][3] != None else "Any"
    max_distance = gusto[1][4] if gusto[1][4] != None else "Any"
    cuisine_type = gusto[1][5] if gusto[1][5] != None else "Any"
    min_rating = gusto[1][6] if gusto[1][6] != None else "Any"

    if gusto[0] != None:
        print(f"  Gusto Label: {label}")
        print(f"  Description: {description}")
    print(f"  Number of People: {group_size}")
    print(f"  Meal Type: {meal_type}")
    print(f"  Budget: {budget}")
    print(f"  Maximum Distance: {max_distance}")
    print(f"  Cuisine Type: {cuisine_type}")
    print(f"  Minimum Rating: {min_rating}")
    print(
        "═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════"
    )
    print(
        "═════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        f"{C1}                                                  Restos                                                {CE}\n",
        "═════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        f"{C2}        Name           Distance         Cuisines               Meal Types              Cost      Rating  {CE}\n"
        "═════════════════════════════════════════════════════════════════════════════════════════════════════════\n",
        sep="",
        end="",
    )
    for resto in recos:
        label = resto
        distance = f"{restos_dict[resto][0]:.2f}m"
        list_of_cuisines = restos_dict[resto][1]
        meal_type = restos_dict[resto][2]
        meal_types = ""
        for char in meal_type:
            if char == "B":
                meal_types += "Breakfast, "
            elif char == "L":
                meal_types += "Lunch, "
            elif char == "D":
                meal_types += "Dinner, "
        meal_types = meal_types.rstrip(", ")
        cost = f"₱{restos_dict[resto][3]:.2f}"
        rating = f"{restos_dict[resto][4]:.1f}"
        print(
            f"  {label:<16}   {distance:<12}   {list_of_cuisines[0] if len(list_of_cuisines) == 1 else "┬ "+list_of_cuisines[0]:<16}   {meal_types:<26}   {cost:>10}   {rating:^6}  "
        )
        for idx, cuisine in enumerate(list_of_cuisines[1:]):
            cuisine = f"├ {cuisine}" if idx != len(list_of_cuisines[1:]) - 1 else f"└ {cuisine}"
            filler = f""
            print(f"  {filler:<16}   {filler:<12}   {cuisine:<16}   {filler:<26}   {filler:>10}   {filler:^6}  ")
    print(
        "═════════════════════════════════════════════════════════════════════════════════════════════════════════"
    )
    continue_prompt()
