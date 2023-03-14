import pandas as pd

# Get list of files in same folder
# iterate through files and get data together
# create new sheet with combined data

dt1 = pd.read_excel('10.03.2023.xlsx')
dt1.reset_index()

dt2 = pd.read_excel('17.03.2023.xlsx')
dt2.reset_index()

total = []
weeks = 2

def is_in_previous(two_dimensional_list, value):
    return any(
        value in nested_list
        for nested_list in two_dimensional_list
    )

def get_index(list, value):
    x = [x for x in list if value in x][0]
    return list.index(x)



for index, row in dt1.iterrows():
    total.append([row['Student Number'],row['Sessions missed'],row['Firstname'], row['Surname'], row['Form']])

for index, row in dt2.iterrows():
    if(is_in_previous(total, row['Student Number'])):
        index = get_index(total, row['Student Number'])
        total[index][1] = row['Sessions missed'] + total[index][1]
    else:
        total.append([row['Student Number'],row['Sessions missed'],row['Firstname'], row['Surname'], row['Form']])

w_df = pd.DataFrame(total)
writer = pd.ExcelWriter('total.xlsx', engine='xlsxwriter')
w_df.to_excel(writer, sheet_name='Total', index=False)
writer.save()

print(total)
    