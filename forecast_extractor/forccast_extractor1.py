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
with open('forecast.json','r') as myfile:		
	data = myfile.read().replace('\n','')

# Remove delimiters from JSON data	
delimiters = ",","{","}","[","]"	
dat = split(delimiters, data)

# Create new, empty dictionary to hold weather key:values
new_dict = dict()

# Two keys named id, one is station, other is weather
# Detect first id and recode to weather_id
#weatherId = False
fd = open('forecast_json.txt', 'a')

# Loop through data that has been split
for j in range(0,len(dat)):

	# Verify length >0
	if len(dat[j]) != 0:
		# key_value = dat[j].replace('\"','') # Good-bye quotes
		# key_value2 = split(":", key_value)  # Split by : delimiter
		output = dat[j] + "\n" #key_value2[0] + "=" + key_value2[1] + "\n"
		fd.write(output)

		
		# weather key found, set flag weatherID = True
		# if key_value2[0] == "weather":
			# weatherID = True
			
		# Found first id after weather key, save to weather_id	
		# elif key_value2[0] == "id" and weatherID == True:
			# key_value2[0] = "weather_id"
			# weatherID = False

		# if len(key_value2[1]) == 0:
			# new_dict.update({ key_value2[0] : 9999}) # Add to my_dict		

		# else:
			# new_dict.update({ key_value2[0] : key_value2[1]}) # Add to my_dict
		#print (key_value) # Print for development

# Find dt key value and convert to date time
# 06-15-2016 08:15 Wed		
# num = float(new_dict.get("dt"))
# dt = time_converter(num)

# fd = open('forecast_json.txt', 'a')
# fd.write(csvString)

# for item in new_dict:
	# print (item, "=",new_dict[item])
fd.close()
