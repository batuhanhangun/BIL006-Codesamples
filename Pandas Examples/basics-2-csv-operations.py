# CSV files tribute: https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
import pandas

file_path = 'addresses.csv'

#How to read a simple CSV file
addresses_pandas_dataframe = pandas.read_csv(file_path)
print(addresses_pandas_dataframe)
print('\n')

file_path = 'letter_frequency.csv'
letter_freqs_pandas_dataframe = pandas.read_csv(file_path)
print(letter_freqs_pandas_dataframe)
print('\n')

file_path = 'faithful.csv'
geyser_pandas_dataframe = pandas.read_csv(file_path)
print(geyser_pandas_dataframe)
print('\n')

#How to get number of rows and columns in a CSV file
[rows, cols] = geyser_pandas_dataframe.shape
print(f"{'Total Rows:'} {rows} { 'Total Cols:'} {cols}")
print('\n')

#Getting name of columns(keys) into a container-1 (total number of keys is known)
[key1, key2, key3] = geyser_pandas_dataframe.columns.tolist()
print(f"{'Keys: '} {key1} {' '} {key2} {' '} {key3}")
print('\n')

#Getting name of columns(keys) into a container-2 (total number of keys is unknown)
key_list = list()
for key in geyser_pandas_dataframe.columns.tolist():
    key_list.append(key)
print(f"{'Keys: '} {key_list}")
print('\n')

#Iterating each row of data frame -1 (total number of keys is known) [Using index]
for data_frame_rows in geyser_pandas_dataframe.index:
    f_str1 = f"{geyser_pandas_dataframe[key1][data_frame_rows]}{' '}"
    f_str2 = f"{geyser_pandas_dataframe[key2][data_frame_rows]}{' '}"
    f_str3 = f"{geyser_pandas_dataframe[key3][data_frame_rows]}{' '}"
    print(f_str1, f_str2, f_str3)
print('\n')

# #Iterating each row of data frame -2 (total number of keys is unknown) [Using index]
for data_frame_rows in geyser_pandas_dataframe.index:
    f_str1 = ''
    for key in key_list:
        f_str1 = f_str1 + f"{geyser_pandas_dataframe[key][data_frame_rows]}{' '}"
    print(f_str1)
print('\n')

#Iterating each row of data frame -3 (total number of keys is known) [Using loc]
for data_frame_rows in range(len(geyser_pandas_dataframe)):
    f_str1 = f"{geyser_pandas_dataframe.loc[data_frame_rows, key1]}{' '}"
    f_str2 = f"{geyser_pandas_dataframe.loc[data_frame_rows, key2]}{' '}"
    f_str3 = f"{geyser_pandas_dataframe.loc[data_frame_rows, key3]}{' '}"
    print(f_str1, f_str2, f_str3)
print('\n')

#Iterating each row of data frame -4 (total number of keys is unknown) [Using loc]
for data_frame_rows in range(len(geyser_pandas_dataframe)):
    f_str1 = ''
    for key in key_list:
        f_str1 = f_str1 + f"{geyser_pandas_dataframe.loc[data_frame_rows, key]}{' '}"
    print(f_str1)
print('\n')
    

#Iterating each row of data frame -5 (total number of keys is unknown and select specific keys(Server, Player Name, Level)) [Using iloc]
player_list = { 'Server': ['Olympias', 'Arest', 'Xigentonon', 'Berasmus', 'Dieys'],
                'Player Name': ['warriorGuy34', 'xxLupinxx', 'LadyHealerUwU', 'fireDAMAGE', 'Inquisitor23'],
                'Level': [32, 44, 38, 27, 50],
                'Class': ['Warrior', 'Rogue', 'Priest', 'Mage', 'Paladin'],
                'Gold': [124, 543, 654, 234, 786]}
player_list_df = pandas.DataFrame(player_list, columns = ['Server', 'Player Name', 'Level', 'Class', 'Gold'])

for key in range(len(player_list_df)):
    f_str1 = f"{player_list_df.iloc[key, 0]}{'  '}"
    f_str2 = f"{player_list_df.iloc[key, 1]}{'  '}"
    f_str3 = f"{player_list_df.iloc[key, 2]}{'  '}"
    f_str4 = f_str1 + f_str2 + f_str3
    print(f_str4)    
print('\n')

#Iterating each row of data frame -6 (total number of keys is unknown and select specific keys(Server, Player Name)) [Using iterrows]
for df_index, df_row in player_list_df.iterrows():
    print (df_row["Server"], df_row["Player Name"])
print('\n')
    
#Iterating each row of data frame -7 (total number of keys is unknown and select specific keys(Player Name, Level)) [Using iterrows]
for df_row in player_list_df.itertuples():
    print (df_row[2], df_row[3]) #In df_row, dataFrame contents starts from index 1
print('\n')

print('\n')