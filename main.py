import mon_classes

def get_input():
    user_input = input("Enter final pokemon type/s: ").lower()
    if user_input == 'exit':
        return
    if user_input not in mon_classes.mon_types:
        print("Not a valid choice. Please try again.")
        print("Type 'Exit' to stop app.")
        return get_input()
    return user_input

user_input = get_input()
super_effective_list = mon_classes.mon_types_dict[user_input].super_effective
super_effective_against_list = mon_classes.mon_types_dict[user_input].super_effective_against

print(user_input.title(), "is super effective against", ", ".join(super_effective_list))
print(user_input.title(), "is super weak to", ", ".join(super_effective_against_list))
