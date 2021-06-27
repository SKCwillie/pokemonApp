import mon_types as mon

def get_input():
    user_input = input("Enter final pokemon type/s: ").lower()
    if user_input == 'exit':
        return
    if user_input not in mon.mon_types:
        print("Not a valid choice. Please try again.")
        print("Type 'Exit' to stop app.")
        return get_input()
    return user_input

def get_defense(mon_type):
    count = 0
    return_list = []
    defense_list = mon.mon_info[mon_type][1]

    for i in defense_list:
        if i == 2:
            return_list.append(mon.mon_types[count])
        count +=1
    return return_list


mon_type = get_input()
x = get_defense(mon_type)
print(mon_type.title(), "is weak to", ', '.join(x).title(), "types.")