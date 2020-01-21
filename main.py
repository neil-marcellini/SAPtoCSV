#  Neil Marcellini
#  1/21/2020
#  This code fetches gps data from SAP and creates csv files in truesail format
# set parameters regatta_name and race_name before running

import json
import requests
import csv
import time
import os

regatta_name = "49erFX%20Worlds%202019"
race_name = "F13%20Gold%20(49erFX)"

csv_headers = ["RowCount", "TimeStamp", "Year", "Month", "Day", "Hour", "Minute", "Second", "Longitude [Deg E]",
               "Latitude [Deg N]", "SOG [knots]", "COG [Deg]", "Pitch [Deg]", "PitchTarget [Deg]", "Heel [Deg]",
               "HeelTarget [Deg]", "HeelRange [Deg]", "ClewLoad [0.1kg]", "Rudder [Deg]", "VMG [k]",
               "TWD [Deg]", "TWS [k]"]

def main():
    start = time.time()
    gps_url = "http://www.sapsailing.com/sailingserver/api/v1/regattas/" + \
              regatta_name + "/races/" + race_name + "/competitors/positions"
    #print(gps_url)
    # get json file
    request = requests.get(gps_url)
    request_text = request.text
    gps_data = json.loads(request_text)

    competitors = gps_data['competitors']
    for comp in competitors:
        makeCSVTrack(comp)
    print("Completed in %.2f seconds" % (time.time() - start))


# makes a csv file for each competitor
def makeCSVTrack(competitor):
    file_name = competitor['name'] + ".csv"
    # replace any slashes in the name
    file_name = file_name.replace('/', '-')
    track = competitor['track']
    # now we will open a file for writing
    csv_file = open(getDirectoryPath() + "/" + file_name, 'w')

    # make a csv writer that uses dictionaries
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()

    # initialize a dictionary for a row
    row = dict.fromkeys(csv_headers, 0)
    # go through a competitor's track and grab data points
    for point in track:
        # update values
        row['RowCount'] += 1
        row['TimeStamp'] = point['timepoint-ms']
        # need to check if these coordinates need conversion
        row['Longitude [Deg E]'] = point['lng-deg']
        row['Latitude [Deg N]'] = point['lat-deg']
        row['COG [Deg]'] = round(point['truebearing-deg'])
        row['SOG [knots]'] = point['speed-kts']
        # write a row to csv
        writer.writerow(row)
    #close the file
    csv_file.close()

# returns the path of csv_files directory
def getDirectoryPath():
    for root, dirs, files in os.walk("."):
        for dir in dirs:
            if "csv_files" in dir:
                return os.path.join(root, dir)

main()
