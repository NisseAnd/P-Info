""" 
The url to run this program use this url:
https://raw.githubusercontent.com/planetsig/ufo-reports/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv
"""


import utility.downloader as downloader

if __name__ == '__main__':
    global file_name
    file_name = downloader.download_file() 