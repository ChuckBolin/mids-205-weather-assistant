# Filename: extract.py
# Author: Chuck B     Date: 6.2.2016
# Purpose: Test code to download JSON files from 
#          openweathermap using API Key

# All imports
import csv              # read csv file (city)
import time             # elapsed time
import urllib.request   # download file from URL
import os               # filesize
import datetime         # datetime stamp

# Function to log file download
def writeToLogFile(filename, size):
  logFile = open("logfile.txt","a")
  logFile.write(filename + "," + str(size) + "\n")
  logFile.close()
  return


# Variable initialization
stemMultiCurr = "http://api.openweathermap.org/data/2.5/group?id="
stemFcst = "http://api.openweathermap.org/data/2.5/forecast/city?id="
stemCurr = "http://api.openweathermap.org/data/2.5/weather?id="
suffix = "&APPID=b655418fdd5a05b8aba9d3e40fdf42cb"
cityFilename = "all_city_list.csv"
downloadFolder = "../dl_data/"
ct = 0
tenCount = 0 # used to count to 10 before processing 10 
tenList=[]
timeDelay = 1.050 # Tweak as needed
toggle = True
cityGroup = 0

# Open CSV file containing city_id
f = open(cityFilename)

# Grab time
beginTimer = time.process_time() 

# Loop through each row in CSV file
for row in csv.reader(f):
  
  # Update counter
  ct = ct + 1  
  
  # Process rows of data, not the header
  if ct < 2:
    continue

  tenCount = tenCount + 1  
    
    
  # City ID is first field
  city_id = row[0]
  tenList.append(city_id)
  
  # collect 10 cities before processing
  if(tenCount == 10):
    tenCount = 0
    
    cities = "" # empty list
    for j in range(0,10):
      cities = cities + tenList[j]
      if j < 9:
        cities = cities + ","
    
    cityGroup = cityGroup + 1
    print (cities, "\n")
    
    ##Time delay
    elapsedTime = 0  
    while elapsedTime < timeDelay:
      elapsedTime = time.process_time() - beginTimer  
    
    ##Start timer for next hit
    beginTimer = time.process_time()
    
    ##Construct current weather source url and destination newFilename
    url = stemMultiCurr + cities + suffix
    timeStampClean = '{:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
    newFilename = "curr_" + str(cityGroup).strip() + "_" + timeStampClean + ".json"
    newFilenameFull = downloadFolder + "curr_" + str(cityGroup).strip() + "_" + timeStampClean + ".json"
    
    ##Retrieves file and saves to /dl_data/ folder
    urllib.request.urlretrieve(url, newFilenameFull)
    fileinfo = os.stat(newFilenameFull)
    writeToLogFile(newFilename, fileinfo.st_size)
    
    ##Time delay
    # elapsedTime = 0  
    # while elapsedTime < timeDelay:
    # elapsedTime = time.process_time() - beginTimer  
    
    ##Start timer for next hit
    # beginTimer = time.process_time()
    
    ##Construct current weather source url and destination newFilename
    # url = stemMultiCurr + cities + suffix
    # timeStampClean = '{:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
    # newFilename = "fcst_" + cityGroup + "_" + timeStampClean +  ".json"
    # newFilenameFull = downloadFolder + "fcst_" + cityGroup + "_" + timeStampClean +  ".json"
    
    ##Retrieves file and saves to /dl_data/ folder
    # urllib.request.urlretrieve(url, newFilenameFull)
    # fileinfo = os.stat(newFilenameFull)
    # writeToLogFile(newFilename, fileinfo.st_size)
    
    del tenList[:] # clear list
    
    if ct > 30:
      break   
  
print("records: ", (ct - 1) * 1, " retrieved!")