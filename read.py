import pandas as pd


from utils import arrays, files

filenames = files.get_filenames()
total = []

for filename in filenames:
    df = pd.read_excel(filename)
    df.reset_index()
    print(filename)
    for index, row in df.iterrows():
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
