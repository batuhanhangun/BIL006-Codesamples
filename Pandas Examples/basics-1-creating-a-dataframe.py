import pandas


# A dictonary was defined to contain player data
player_list = { 'Server': ['Olympias', 'Arest', 'Xigentonon', 'Berasmus', 'Dieys'],
                'Player Name': ['warriorGuy34', 'xxLupinxx', 'LadyHealerUwU', 'fireDAMAGE', 'Inquisitor23'],
                'Level': [32, 44, 38, 27, 50],
                'Class': ['Warrior', 'Rogue', 'Priest', 'Mage', 'Paladin'],
                'Gold': [124, 543, 654, 234, 786]}

# Dictionary was converted into pandas DataFrame
player_list_df = pandas.DataFrame(player_list, columns = ['Server Name', 'Player Name', 'Level', 'Class', 'Gold'])

print("Player List DataFrame :\n", player_list_df)


