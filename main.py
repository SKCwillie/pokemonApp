import pandas as pd


df = pd.read_csv('./pokemon.csv')
type_chart = pd.read_csv('./type_chart.csv')
"""
For type_chart, the rows represent offense modifiers for given type
                the columns represent defense modifiers for that given type
"""
index_key = {}
count = 0
for i in df['name']:
    index_key[i] = count
    count += 1


class Pokemon(object):
    def __init__(self, index):
        self.index = index
        self.name = df.at[self.index, 'name']
        self.type_1 = df.at[self.index, 'type_1']
        self.type_2 = df.at[self.index, 'type_2']

        if pd.isnull(self.type_2):
            self.num_types = 1

        else:
            self.num_types = 2

        self.ability_1 = df.at[self.index, 'ability_1']
        self.ability_2 = df.at[self.index, 'ability_2']
        if pd.isnull(self.ability_2):
            self.num_abilities = 1
        else:
            self.num_abilities = 2

        self.hidden = df.at[self.index, 'ability_hidden']

        self.defense = {}
        self.type_list = type_chart['Type'].to_list()
        self.defense_1 = type_chart[self.type_1].to_list()
        self.defense_2 = type_chart[self.type_2].to_list()

        if pd.isnull(self.type_2):
            for j in range(len(self.type_list)):
                self.defense[self.type_list[j]] = self.defense_1[j]
        else:
            for k in range(len(self.type_list)):
                self.defense[self.type_list[k]] = self.defense_1[k] * self.defense_2[k]

    def get_name(self):
        return self.name

    def get_types(self):
        if pd.isnull(self.type_2):
            self.num_types = 1
            return self.type_1
        else:
            self.num_types = 2
            return self.type_1, self.type_2

    def get_abilities(self):
        if pd.isnull(self.ability_2):
            return self.ability_1
        else:
            return self.ability_1, self.ability_2

    def get_hidden(self):
        if pd.isnull(self.hidden):
            return 'None'
        else:
            return self.hidden

    def get_defense(self):
        return self.defense


def get_index():
    user_input = input("Enter Pokemon name:  ").title()
    try:
        index = index_key[user_input]
    except KeyError:
        print("Not a valid pokemon. Please try again.")
        return get_index()
    return index


myIndex = get_index()
myMon = Pokemon(myIndex)
print(myMon.get_name())
print(myMon.get_types())
print(myMon.get_defense())
