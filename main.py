""" 
The url to run this program use this url:
https://raw.githubusercontent.com/rmlassesen/dataset/master/p_pladser.csv
"""

import csv
import utility.downloader as dl
import utility.convert_csv as cc
import library.centrum_parking as cp
import library.mulighedder2 as mu

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