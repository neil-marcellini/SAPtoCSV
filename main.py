#  Neil Marcellini
#  2/9/2020
#  This code fetches gps data from SAP and creates csv files for each race and each competitor in a regatta.
#  .csv files are in truesail format
# set parameters regatta_id before running

import json
import requests
import csv
import time
import os
import datetime
import urllib.parse


regatta_url = "https://49erworlds2020.sapsailing.com/gwt/Home.html#/" \
              "regatta/races/:eventId=ee70229c-9836-4025-9096-1b5050152b1e&regattaId=49erFX%20Worlds%202020"
base_url = ""
regatta_id = ""

csv_headers = ["RowCount", "TimeStamp", "Year", "Month", "Day", "Hour", "Minute", "Second", "Longitude [Deg E]",
               "Latitude [Deg N]", "SOG [knots]", "COG [Deg]", "Pitch [Deg]", "PitchTarget [Deg]", "Heel [Deg]",
               "HeelTarget [Deg]", "HeelRange [Deg]", "ClewLoad [0.1kg]", "Rudder [Deg]", "VMG [k]",
               "TWD [Deg]", "TWS [k]"]

def parseURL():
    global base_url
    global regatta_id
    base_url = regatta_url.split("sapsailing.com")[0] + "sapsailing.com/sailingserver/api/v1/regattas/"
    # print(base_url)
    regatta_id = regatta_url.split("regattaId=")[1]
    # print(regatta_id)


def main():
    start = time.time()
    parseURL()
    race_names = getAllRaces()
    for race_name in race_names:
        dirname = urllib.parse.unquote(race_name)
        dirname = dirname.replace(' ', '-')
        os.mkdir(os.path.join(os.getcwd(), "csv_files", dirname))
        gps_url = base_url + regatta_id + "/races/" + race_name + "/competitors/positions"
        # print(gps_url)
        # get json file
        request = requests.get(gps_url)
        request_text = request.text
        gps_data = json.loads(request_text)

        competitors = gps_data['competitors']
        for comp in competitors:
            makeCSVTrack(comp, dirname)
    print("Completed in %.2f seconds" % (time.time() - start))


# makes a csv file for each competitor
def makeCSVTrack(competitor, dirname):
    file_name = competitor['name'] + ".csv"
    # replace any slashes in the name
    file_name = file_name.replace('/', '-')
    track = competitor['track']
    # now we will open a file for writing
    csv_file = open(os.getcwd() + "/" + "csv_files" + "/" + dirname + "/" + file_name, 'w')
    # make a csv writer that uses dictionaries
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()

    # initialize a dictionary for a row
    row = dict.fromkeys(csv_headers, 0)
    # go through a competitor's track and grab data points
    for point in track:
        # update values
        row['RowCount'] += 1
        timestamp = point['timepoint-ms'] / 1000  # divide by 1000 to get rid of trailing 0s
        row['TimeStamp'] = timestamp
        # Gives you the date and time in UTC
        d = datetime.datetime.utcfromtimestamp(int(timestamp))
        row['Year'] = d.year
        row['Month'] = d.month
        row['Day'] = d.day
        row['Hour'] = d.hour
        row['Minute'] = d.minute
        row['Second'] = d.second
        # need to check if these coordinates need conversion
        row['Longitude [Deg E]'] = point['lng-deg']
        row['Latitude [Deg N]'] = point['lat-deg']
        row['COG [Deg]'] = round(point['truebearing-deg'])
        row['SOG [knots]'] = point['speed-kts']
        # write a row to csv
        writer.writerow(row)
    #close the file
    csv_file.close()


def getAllRaces():
    races_url = base_url + regatta_id + "/races/"
    # print(races_url)
    # get json file
    request = requests.get(races_url)
    request_text = request.text
    races_data = json.loads(request_text)
    race_list = races_data['races']
    race_names = [urllib.parse.quote(race['name']) for race in race_list]
    return race_names


main()
