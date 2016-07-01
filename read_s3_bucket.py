# Written by Chuck, 2016
# Purpose: Reads key names (files) from S3 buckets
# Thanks to http://boto.cloudhackers.com/en/latest/s3_tut.html

# imports
import boto # pip.exe install boto
from boto.s3.connection import S3Connection
from boto.s3.connection import Location

# keys
access_key = ''
secret_key = ''

# point to S3 connection object 
conn = S3Connection(access_key, secret_key)

## list all locations - works
# print ('\n'.join(i for i in dir(Location) if i[0].isupper()))

# get list of buckets
rs = conn.get_all_buckets()

ct = 0
textFile = open("s3_list.txt", "w")

print(len(rs)) # returns 1
for b in rs:   # returns weather-raw-json
  print (b.name)
  mybucket = conn.get_bucket(b.name)
  for file_key in mybucket.list():
    #print(file_key.name)
    textFile.write(file_key.name + "\n")
    ct = ct + 1
    #if(ct > 10):    
    #  break;

textFile.close()
    
print("filecount: " + str(ct))
