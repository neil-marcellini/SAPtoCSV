# SAPtoCSV
This program accesses the SAP sailing analytics API and pulls gps data from a specified regatta and race. The data is then written to a CSV file with a format that matches the output of another device, and stored in the csv_files folder. There will be one CSV file for each competitor in the race.

## Getting Started
To run the program please use Pycharm. Open Pycharm and go to File -> Open. Select the priceBookUpdate-master folder.

## Configuration
If you want to select a different race then the example you must do the following:

There are two global variables in the program that can be set to select a specific race. To find regatta and race names go to [sapsailing.com](https://www.sapsailing.com/gwt/Home.html), select an event, then click the regattas tab, select a regatta, click on Races/Tracking, scroll down and click tracking, and select replay. When the page loads go to the url and you will see sections that say "regattaName=" and "raceName=". Copy the text immediately following and before the next "&". Then replace all "+" with "%20".

For example with the following url:
```
https://www.sapsailing.com/gwt/RaceBoard.html?regattaName=49er+Worlds+2019&raceName=F15+Silver+(49er)&leaderboardName=49er+Worlds+2019&leaderboardGroupName=49er+%2F+49er+FX+%2F+Nacra+17+World+Championships+2019&eventId=e5a65f0a-b9b4-4630-b0b0-ad1fd7727518&mode=FULL_ANALYSIS
```

The regatta_name variable should be set to `49er%20Worlds%202019` and the race_name variable should be set to `F15%20Silver%20(49er)`

## What I Learned
Working on this program helped me understand how CSV files work, how to create them from JSON files using the python csv module, how to select only relevant data, and how to manipulate the data into the specific format required. I also had to draw on my previous experience working with the [SAP Sailing API](https://www.sapsailing.com/sailingserver/webservices/api/v1/index.html) and the formatting of their JSON files.
