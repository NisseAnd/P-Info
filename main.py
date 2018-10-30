""" 
The url to run this program use this url:
https://raw.githubusercontent.com/planetsig/ufo-reports/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv
"""


import utility.downloader as dl
import utility.convert_csv as cc
import library.centrum_parking as cp

if __name__ == '__main__':
    global file_name
    file_name = dl.download_file() 

cc.convert_csv_to_dataframe(file_name)
#cp.number_of_spots(data)