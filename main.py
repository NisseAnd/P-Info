""" 
The url to run this program use this url:
https://raw.githubusercontent.com/rmlassesen/dataset/master/p_pladser.csv
"""


import utility.downloader as dl
import utility.convert_csv as cc
import library.centrum_parking as cp

if __name__ == '__main__':
    global file_name
    file_name = dl.download_file() 

data = cc.convert_csv_to_dataframe(file_name)
cp.number_of_parking_spots(data)

# Get the income data
#data_income = dl.get_income_data()

data_income = cc.convert_income_to_dataframe(file_name)


