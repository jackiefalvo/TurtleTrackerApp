#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Cristiana Falvo (cristiana.falvo@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

# create variable pointing to data file
file_name = './Data/Raw/RawArgosData_SaraTurtleTrack.txt'

# create a file object from the file
file_object = open(file_name, 'r')

# read contents of file into a list
line_list = file_object.readlines()

# close the file (we have our list now)
file_object.close()

# sample line
lineString = line_list[100]

# split string into data items
lineData = lineString.split()

# extract items in list into variables
record_ID = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

# delete error variable from environments
    # del(obs_data)
    
# print sara's location
print(f"Record {record_ID} indicates Sara was seen at {obs_lat}N,{obs_lon}W on {obs_date}")

