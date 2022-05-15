# CSV files tribute: https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
#                    https://github.com/rishabh89007/Time_Series_Datasets
from numpy import NaN
import pandas

file_path = 'Pandas Examples\\ren_energ_texas.csv'
ren_energy_df = pandas.read_csv(file_path)
print(ren_energy_df)
[rows, cols] = ren_energy_df.shape
print(f"{'Total Rows:'} {rows} { 'Total Cols:'} {cols}")
print(type(ren_energy_df))
print('\n')

#Deleting row(s) from dataframe
index = 0
ren_energy_new_df = pandas.DataFrame.drop(ren_energy_df, index)
print(ren_energy_new_df)
[rows, cols] = ren_energy_new_df.shape
print(f"{'Total Rows:'} {rows} { 'Total Cols:'} {cols}")
print(type(ren_energy_new_df))
print('\n')

ren_energy_new_df = pandas.DataFrame.drop(ren_energy_new_df, [1, 2, 3])
print(ren_energy_new_df)
[rows, cols] = ren_energy_new_df.shape
print(f"{'Total Rows:'} {rows} { 'Total Cols:'} {cols}")
print(type(ren_energy_new_df))
print('\n')

#Conditional delete
ren_energy_new_df = ren_energy_new_df.loc[ren_energy_new_df["Energy Production"] >=70000]
print(ren_energy_new_df)
[rows, cols] = ren_energy_new_df.shape
print(f"{'Total Rows:'} {rows} { 'Total Cols:'} {cols}")
print(type(ren_energy_new_df))
print('\n')

#Inserting new column
ren_energy_new_df.insert(2, 'Type', NaN)
print(ren_energy_new_df)
[rows, cols] = ren_energy_new_df.shape
print(f"{'Total Rows:'} {rows} { 'Total Cols:'} {cols}")
print(type(ren_energy_new_df))
print('\n')

new_entry = {'Year': ['2021'], 'Energy Production': ['99999'], 'Type': ['Wind']}
new_entry_df = pandas.DataFrame(new_entry, columns = ['Year', 'Energy Production', 'Type'])
[rows, cols] = new_entry_df.shape
print(new_entry_df)
print(f"{'Total Rows:'} {rows} { 'Total Cols:'} {cols}")
print(type(new_entry_df))

ren_energy_new_df = pandas.concat([ren_energy_new_df, new_entry_df])
[rows, cols] = ren_energy_new_df.shape
print(ren_energy_new_df)
print(f"{'Total Rows:'} {rows} { 'Total Cols:'} {cols}")
print(type(ren_energy_new_df))
print('\n')
