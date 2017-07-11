#!/usr/local/bin/python3
import pandas as pd
import numpy as np
import glob
import xlrd
import csv
import os

# directory_name=sys.argv[n]
# print(directory_name)
# cwd = os.getcwd()
# print(cwd)
# print(glob.glob("./Payout/Payout*"))
all_data = pd.DataFrame()
for f in glob.glob('./Payout/Payout*'):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)
    print(f)
# all_data.head()
# print(all_data)
all_data.to_csv("./totals.csv")
# data_xls = pd.read_excel('./Payout/totals.xlsx', 'Sheet1', index_col=None)
# data_xls.to_csv('./Payout/totals.csv', encoding='utf-8')
csvFile = open('./totals.csv', "r")
csvReader = csv.reader(csvFile)
# header = csvReader.next()
# Loop through the lines in the file and get each coordinate
counter=0
totalDeposit=0
totalShiftPay=0
for row in csvReader:
    for index, row in enumerate(row, start=0):   # Python indexes start at zero
        row=row.strip()
        # print (row)
        if row == 'Total Amount Deposited':
            counter=1
            continue
        elif row =='Shift Pay':
            counter=2
            continue
        else:
            dog=0
            # print('Undefined')
        if counter==1:
            try:
                totalDeposit += float(row)

            except:
                print('Exception Caught')

            counter=0
            continue
        if counter ==2:
            try:
                totalShiftPay += float(row)

            except:
                print('Exception Caught')

            counter=0
            continue

# # Create a Pandas dataframe from the data.
df2 = pd.DataFrame({'Deposit': [totalDeposit],'Shift Pay':[totalShiftPay]},{'Totals'})
#
# # Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('./AggregateData.xlsx', engine='xlsxwriter')
#
# # Convert the dataframe to an XlsxWriter Excel object.
df2.to_excel(writer, sheet_name='Sheet1')
#
# # Close the Pandas Excel writer and output the Excel file.
writer.save()

csvFile.close()
# os.remove('./totals.csv') UNCOMMENT WHEN DONE
print('Finished!')
