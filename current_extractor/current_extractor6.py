# http://strftime.org/
#http://openweathermap.org/weather-data



import re
import datetime

#thanks - http://stackoverflow.com/questions/4998629/python-split-string-with-multiple-delimiters
# Function to split values based upon several delimiters
def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)

# http://codereview.stackexchange.com/questions/131371/script-to-print-weather-report-from-openweathermap-api
# Convert JSON dt long integer to datetime 
def time_converter(time):
	converted_time = datetime.datetime.fromtimestamp(
			int(time)
	).strftime('%m-%d-%Y %H:%M %a')
	return converted_time

# Read JSON file into a string	
with open('current.json','r') as myfile:		
	data = myfile.read().replace('\n','')

# Remove delimiters from JSON data	
delimiters = ",","{","}","[","]"	
dat = split(delimiters, data)

# Create new, empty dictionary to hold weather key:values
new_dict = dict()

# Two keys named id, one is station, other is weather
# Detect first id and recode to weather_id
weatherId = False

# Loop through data that has been split
for j in range(0,len(dat)):

	# Verify length >0
	if len(dat[j]) != 0:
		key_value = dat[j].replace('\"','') # Good-bye quotes
		key_value2 = split(":", key_value)  # Split by : delimiter
		
		# weather key found, set flag weatherID = True
		if key_value2[0] == "weather":
			weatherID = True
			
		# Found first id after weather key, save to weather_id	
		elif key_value2[0] == "id" and weatherID == True:
			key_value2[0] = "weather_id"
			weatherID = False

		if len(key_value2[1]) == 0:
			new_dict.update({ key_value2[0] : 9999}) # Add to my_dict		

		else:
			new_dict.update({ key_value2[0] : key_value2[1]}) # Add to my_dict
		#print (key_value) # Print for development

# Find dt key value and convert to date time
# 06-15-2016 08:15 Wed		
num = float(new_dict.get("dt"))
dt = time_converter(num)

## weather codes
## http://openweathermap.org/weather-conditions
for item in new_dict:
	print (item, "=",new_dict[item])

#construct header
header = "city_id,datetime,lat,lon,weather_id,pressure, sea_level,ground_level,wind_speed,wind_dir,"
header = header + "temp,temp_min,temp_max,message, country, sunrise, sunset, name, code\n"

#construct csv
csvString = ""

csvString = csvString + new_dict.get("id") + ","
csvString = csvString + dt + ","

if "lat" in new_dict:
	csvString = csvString + new_dict.get("lat")+ ","
else:
  csvString = csvString + "9999,"
	
if "lon" in new_dict:
	csvString = csvString + new_dict.get("lon")+ ","
else:
  csvString = csvString + "9999,"
	
if "weather_id" in new_dict:
	csvString = csvString + new_dict.get("weather_id")+ ","
else:
  csvString = csvString + "9999,"
	
if "pressure" in new_dict:
	csvString = csvString + new_dict.get("pressure")+ ","
else:
  csvString = csvString + "9999,"

if "sea_level" in new_dict:
	csvString = csvString + new_dict.get("sea_level")+ ","
else:
  csvString = csvString + "9999,"
	
if "grnd_level" in new_dict:
	csvString = csvString + new_dict.get("grnd_level")+ ","
else:
  csvString = csvString + "9999,"	

if "speed" in new_dict:
	csvString = csvString + new_dict.get("speed")+ ","
else:
  csvString = csvString + "9999,"	
	
if "deg" in new_dict:
	csvString = csvString + new_dict.get("deg")+ ","
else:
  csvString = csvString + "9999,"	

if "temp" in new_dict:
	csvString = csvString + new_dict.get("temp")+ ","
else:
  csvString = csvString + "9999,"	
	
if "temp_min" in new_dict:
	csvString = csvString + new_dict.get("temp_min")+ ","
else:
  csvString = csvString + "9999,"	

if "temp_max" in new_dict:
	csvString = csvString + new_dict.get("temp_max")+ ","
else:
  csvString = csvString + "9999,"	
	
if "message" in new_dict:
	csvString = csvString + new_dict.get("message")+ ","
else:
  csvString = csvString + "9999,"	

if "country" in new_dict:
	csvString = csvString + new_dict.get("country")+ ","
else:
  csvString = csvString + "9999,"	
	
if "name" in new_dict:
	csvString = csvString + new_dict.get("name")+ ","
else:
  csvString = csvString + "9999,"	
	
if "sunrise" in new_dict:
	num = float(new_dict.get("sunrise"))
	sunrise = time_converter(num)
	csvString = csvString + str(sunrise) + ","	
else:
  csvString = csvString + "9999,"	
	
if "sunset" in new_dict:
	num = float(new_dict.get("sunset"))
	sunset = time_converter(num)
	csvString = csvString + str(sunset) + ","
else:
  csvString = csvString + "9999,"		

if "cod" in new_dict:
	csvString = csvString + new_dict.get("cod") + "\n"
else:
  csvString = csvString + "9999,"	+ "\n"	


# print(header)
# print(csvString)
		
fd = open('current.csv', 'a')
# fd.write(header)
fd.write(csvString)
fd.close()

print("Complete")
