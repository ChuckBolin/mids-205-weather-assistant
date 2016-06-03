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
stemFcst = "http://api.openweathermap.org/data/2.5/forecast/city?id="
stemCurr = "http://api.openweathermap.org/data/2.5/weather?id="
suffix = "&APPID=b655418fdd5a05b8aba9d3e40fdf42cb"
cityFilename = "all_city_list.csv"
downloadFolder = "../dl_data/"
ct = 0
timeDelay = 1.050 # Tweak as needed
toggle = True

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

  # City ID is first field
  city_id = row[0]
  
  # Time delay
  elapsedTime = 0  
  while elapsedTime < timeDelay:
    elapsedTime = time.process_time() - beginTimer  
  
  # Start timer for next hit
  beginTimer = time.process_time()
  
  # Construct current weather source url and destination newFilename
  url = stemCurr + city_id + suffix
  timeStampClean = '{:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
  newFilename = "curr_" + city_id + "_" + timeStampClean + ".json"
  newFilenameFull = downloadFolder + "curr_" + city_id + "_" + timeStampClean + ".json"
  
  # Retrieves file and saves to /dl_data/ folder
  urllib.request.urlretrieve(url, newFilenameFull)
  fileinfo = os.stat(newFilenameFull)
  writeToLogFile(newFilename, fileinfo.st_size)
  
  # Time delay
  elapsedTime = 0  
  while elapsedTime < timeDelay:
    elapsedTime = time.process_time() - beginTimer  
  
  # Start timer for next hit
  beginTimer = time.process_time()
  
  # Construct current weather source url and destination newFilename
  url = stemFcst + city_id + suffix
  timeStampClean = '{:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
  newFilename = "fcst_" + city_id + "_" + timeStampClean +  ".json"
  newFilenameFull = downloadFolder + "fcst_" + city_id + "_" + timeStampClean +  ".json"
  
  # Retrieves file and saves to /dl_data/ folder
  urllib.request.urlretrieve(url, newFilenameFull)
  fileinfo = os.stat(newFilenameFull)
  writeToLogFile(newFilename, fileinfo.st_size)
  
  if ct > 8:
    break   
  
print("records: ", (ct - 1) * 2, " retrieved!")