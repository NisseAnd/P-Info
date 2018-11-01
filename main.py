""" 
The url to run this program use this url:
https://raw.githubusercontent.com/rmlassesen/dataset/master/p_pladser.csv
"""

import csv
import utility.downloader as dl
import utility.convert_csv as cc
import library.centrum_parking as cp
import library.mulighedder as mu
'''
if __name__ == '__main__':
    global file_name
    file_name = dl.download_file() 

data = cc.convert_csv_to_dataframe(file_name)
cp.number_of_parking_spots(data)

# Get the income data
data_income = dl.get_income_data()
'''

data = cc.convert_csv_to_dataframe('p_pladser.csv')
print(mu.mulig(data))

print("end")



'''
#simpel test af linket:

start = 0
end = 3
with open('p_pladser.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if start < end:
            print(row)
            start += 1
        else:
            break

'''

#end