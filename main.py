import mon_classes
mon_types_dict = mon_classes.mon_types_dict
mon_types = mon_classes.mon_types

def get_input():
    user_input = input("Enter Pokemon type: ").lower()
    if user_input == 'exit':
        return
    return user_input

def check_input(user_input):
    if user_input not in mon_classes.mon_types:
        print("Not a valid choice. Please try again.")
        print("Type 'Exit' to stop app.")
        return get_input()

def get_second_type():
    check = input("Do you want to enter another type? [Y/n]: ")
    if check.upper() == 'Y':
        return get_input()
    elif check.upper() == 'N':
        return
    else:
        print("Not a valid choice. Please try again")
        return get_second_type()

def get_defense(type1, type2):
    """Return a list of lists of damge modifiers[4x, 2x, 1x, 1/2x, 1/4x, 0]
    Keyword Arguments:
        type1 -- type, as a string
        type2 -- type, as a string, or None if not applicable
    """
    dmg_4 = []
    dmg_2 = []
    dmg_1 = []
    dmg_half = []
    dmg_quarter = []
    dmg_0 = []
    added_to = []

    type1_super_effective = mon_types_dict[type1].super_effective_against
    type1_effective = mon_types_dict[type1].effective_against
    type1_not_very_effective = mon_types_dict[type1].not_very_effective_against
    type1_no_effect = mon_types_dict[type1].no_effect_against

    if type2 != None:
        type2_super_effective = mon_types_dict[type2].super_effective_against
        type2_effective = mon_types_dict[type2].effective_against
        type2_not_very_effective = mon_types_dict[type2].not_very_effective_against
        type2_no_effect = mon_types_dict[type2].no_effect_against
        for i in type1_super_effective:
            if i in type2_super_effective:
                dmg_4.append(i)
                added_to.append(i)
        for i in type1_super_effective:
            if i in type2_effective:
                dmg_2.append(i)
                added_to.append(i)
        for i in type2_super_effective:
            if i in type1_effective:
                dmg_2.append(i)
                added_to.append(i)
        for i in type1_not_very_effective:
            if i in type2_effective:
                dmg_half.append(i)
                added_to.append(i)
        for i in type2_not_very_effective:
            if i in type1_effective:
                dmg_half.append(i)
                added_to.append(i)
        for i in type1_not_very_effective:
            if i in type2_not_very_effective:
                dmg_quarter.append(i)
                added_to.append(i)
        for i in type1_no_effect:
            dmg_0.append(i)
            added_to.append(i)
        for i in type2_no_effect:
            dmg_0.append(i)
            added_to.append(i)
        for i in mon_types:
            if i not in added_to:
                dmg_1.append(i)
        return [dmg_4, dmg_2, dmg_1, dmg_half, dmg_quarter, dmg_0]
    else:
        dmg_2 = mon_types_dict[type1].super_effective_against
        dmg_1 = mon_types_dict[type1].effective_against
        dmg_half = mon_types_dict[type1].not_very_effective_against
        dmg_0 = mon_types_dict[type1].no_effect_against
        return [dmg_4, dmg_2, dmg_1, dmg_half, dmg_quarter, dmg_0]

def print_defense(defense_list):
    defense_values = ["4x", "2x", "1x", "1/2x", "1/4x", "0x"]
    count = 0
    for i in defense_list:
        if len(defense_list[count])>=1:
            print(defense_values[count], "damage from types", ", ".join(defense_list[count]))

        count +=1


type1 = get_input()
check_input(type1)
type2 = get_second_type()
defense = get_defense(type1, type2)
print_defense(defense)

