#-------------------------------------------------------------
# ARGOSTrackingTool.py -- iteration
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Cristiana Falvo (cristiana.falvo@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

# read in data
raw_file = './Data/Raw/RawArgosData_SaraTurtleTrack.txt'
raw_data = open(raw_file, 'r')

# read all lines of file, add to list
data = raw_data.readlines()
print(data[17])

# iterate through lines
# for line in data:
  #  if line[0] == '#'or line[0] == 'u': #if first character in line is a # or uid
   #     continue # skip
        
for line in data:
    if line[0] in ('#', 'u'): # if the line's first character is in this tuple
        continue # then skip it
    
    
print(data[17])


# split string into data items
split_data = data.split()

# extract items in list into variables
record_ID = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]


