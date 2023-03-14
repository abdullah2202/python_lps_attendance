import pandas as pd


from utils import arrays

# Get list of files in same folder
# iterate through files and get data together
# create new sheet with combined data

dt1 = pd.read_excel('10.03.2023.xlsx')
dt1.reset_index()

dt2 = pd.read_excel('17.03.2023.xlsx')
dt2.reset_index()

total = []
weeks = 2


for index, row in dt1.iterrows():
    total.append([row['Student Number'],row['Sessions missed'],row['Firstname'], row['Surname'], row['Form']])

for index, row in dt2.iterrows():
    if(arrays.is_in_previous(total, row['Student Number'])):
        index = arrays.get_index(total, row['Student Number'])
        total[index][1] = row['Sessions missed'] + total[index][1]
    else:
        total.append([row['Student Number'],row['Sessions missed'],row['Firstname'], row['Surname'], row['Form']])

w_df = pd.DataFrame(total)
w_df.columns = ['Student Number', 'Sessions Missed', 'Firstname', 'Surname', 'Form']
w_df = w_df.sort_values(by="Sessions Missed", ascending=False)

# print(w_df)

writer = pd.ExcelWriter('total.xlsx', engine='xlsxwriter')
w_df.to_excel(writer, sheet_name='Total', index=False)
writer.save()
