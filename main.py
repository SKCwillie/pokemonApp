import numpy as np
import pandas as pd

df = pd.read_csv('./pokemon.csv')
df.set_index('name', inplace=True)
type_chart = pd.read_csv('./type_chart.csv')
type_chart.set_index('Type', inplace=True)
type_chart = type_chart.astype(float)
"""
For type_chart, the rows represent offense modifiers for given type
                the columns represent defense modifiers for that given type
"""


class Pokemon(object):
    """
    Pokemon class has following attributes:
    self.name: str (title) of Mons name
    self.type_1: str (title) of mons type
    self.type_2: str (title) of mons name, NaN if Mon does not have 2nd type
    self.ability_1: str (title) of possible ability
    self.ability_2: str( title) of possible ability, NaN if Mon does not have 2nd ability
    self.hidden: str (title) of Mons hidden ability, NaN if Mon does not have hidden ability
    self.ability_list: list of possible abilities [1, 2, hidden], NaN if not available
    self.defense: dict, Type:defense modifier
    self.defense_list: list, defense modifier
    self.offense: dict, Type: dmg modifier
    self.offense_list: list, dmg modifier
    """

    def __init__(self, name):
        self.name = name
        self.type_1 = df.at[self.name, 'type_1']
        self.type_2 = df.at[self.name, 'type_2']

        if pd.isnull(self.type_2):
            self.num_types = 1

        else:
            self.num_types = 2

        self.ability_1 = df.at[self.name, 'ability_1']
        self.ability_2 = df.at[self.name, 'ability_2']
        if pd.isnull(self.ability_2):
            self.num_abilities = 1
        else:
            self.num_abilities = 2

        self.hidden = df.at[self.name, 'ability_hidden']
        self.ability_list = [self.ability_1, self.ability_2, self.hidden]
        self.defense = {}
        self.offense = {}
        self.defense_list = []
        self.offense_list = []
        self.type_list = type_chart.index.to_list()
        self.defense_1 = type_chart[self.type_1].to_list()
        self.offense_1 = type_chart.loc[self.type_1].to_list()

        try:
            self.defense_2 = type_chart[self.type_2].to_list()
            self.offense_2 = type_chart.loc[self.type_2].to_list()

        except KeyError:
            self.defense_2 = np.nan
            self.offense_2 = np.nan

        if pd.isnull(self.type_2):
            self.defense_list = self.defense_1
            self.offense_list = self.offense_1
            for j in range(len(self.type_list)):
                self.defense[self.type_list[j]] = self.defense_1[j]
                self.offense[self.type_list[j]] = self.offense_1[j]
        else:
            for k in range(len(self.type_list)):
                self.defense[self.type_list[k]] = self.defense_1[k] * self.defense_2[k]
                self.defense_list.append(self.defense_1[k] * self.defense_2[k])
                if self.offense_1[k] >= self.offense_2[k]:
                    self.offense[self.type_list[k]] = self.offense_1[k]
                    self.offense_list.append(self.offense_1[k])
                else:
                    self.offense[self.type_list[k]] = self.offense_2[k]
                    self.offense_list.append(self.offense_2[k])



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
        for l in range(len(self.ability_list) - 1):
            if pd.isnull(self.ability_list[l]):
                self.ability_list.pop(l)
        if pd.isnull(self.hidden):
            return tuple(self.ability_list)
        else:
            self.ability_list[-1] = "Hidden Ability: " + self.ability_list[-1]
            return tuple(self.ability_list)

    def get_hidden(self):
        if pd.isnull(self.hidden):
            return 'None'
        else:
            return self.hidden

    def get_defense(self):
        return self.defense

    def get_offense(self):
        return self.offense


def get_input():
    user_input = input("Enter Pokemon name:  ").title()
    if user_input not in df.index:
        print("Not a valid pokemon. Please try again.")
        return get_input()
    else:
        return user_input


if __name__ == "__main__":
    user_input = get_input()
    myMon = Pokemon(user_input)
    print(myMon.get_name())
    print(myMon.get_types())
    print(myMon.get_abilities())
    print(myMon.get_defense())
    print(myMon.get_offense())


