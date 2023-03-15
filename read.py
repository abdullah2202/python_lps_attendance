import pandas as pd

from utils import arrays, files

filenames = files.get_filenames()
total = []
weeks = 0

columns = ['Student Number', 
           'Firstname', 
           'Surname', 
           'Form',
           'Total Sessions Missed', 
           'Total Attendance %',
          ]

for filename in filenames:
    # Increment week number
    weeks += 1
    txt_weeks = f'W{weeks}'

    # Calculate the index of new columns
    index_sessions_missed = 6 + ((weeks * 2) -1)
    index_reasons = 6 + (weeks * 2)

    # Add Weekly Column Names
    columns.extend([txt_weeks, f'{txt_weeks} Reason'])

    # Read Excel file
    df = pd.read_excel(filename)
    df.reset_index()

    # Iterate through the rows
    for index, row in df.iterrows():
        
        # Check if the student number already exists from previous weeks
        if(arrays.is_in_previous(total, row['Student Number'])):
            index = arrays.get_index(total, row['Student Number'])

            # Sum up the sessions missed, make note of index for 'Session missed'
            total[index][4] += row['Sessions missed']

            # Sum up the Total Attendance %
            total[index][5] = (row['Attendance %'] + total[index][5]) / 2

            # Add in empty columns for previous weeks
            if(len(total[index])<(index_reasons-2)):
                while(len(total[index])<(index_reasons-2)):
                    total[index].extend(['',''])

            # Add Weekly totals and notes to end
            total[index].extend([row['Sessions missed'], row['Attendance Notes']])


        # Student numner does not exist, create new entry
        else:
            total.append([row['Student Number'],
                          row['Firstname'], 
                          row['Surname'], 
                          row['Form'],
                          row['Sessions missed'],
                          row['Attendance %'],
                        ])
            
            last_index = len(total) - 1

            # First Week
            if(weeks==1):
                total[last_index].extend([
                    row['Sessions missed'],
                    row['Attendance Notes']
                ])
            else:
                while(len(total[last_index])<(index_reasons)-2):
                    total[last_index].extend(['',''])
                total[last_index].extend([
                    row['Sessions missed'],
                    row['Attendance Notes']
                ])

# Write data to Excel file
w_df = pd.DataFrame(total)
w_df.columns = columns
w_df = w_df.sort_values(by="Total Sessions Missed", ascending=False)

writer = pd.ExcelWriter('total.xlsx', engine='xlsxwriter')
w_df.to_excel(writer, sheet_name='Total', index=False)
writer.save()
