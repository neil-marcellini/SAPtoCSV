# SAPtoCSV
This program accesses the SAP sailing analytics API and pulls gps data from all races of a specified regatta. The data is then written to a CSV file with a format that matches the output of another device, and stored in the csv_files folder, with subfolders for each race. There will be one CSV file for each competitor in a race.

## Prerequisites
You will need python3, pip, and venv. Or Pycharm.

## Getting Started
To run the program you can use Pycharm or run from terminal using venv. 

To use Pycharm:

Open Pycharm and go to File -> Open. Select the SAPtoCSV-master folder.

To use venv from command line:
Open SAPtoCSV-master folder in terminal.
Enter the following commands:
```python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Configuration
No configuration is required to run, but if you want to select a different race then you must do the following:

There is one global variable in the program that can be set to select a regatta. To find a regatta name go to [sapsailing.com](https://www.sapsailing.com/gwt/Home.html), select an event, then click the regattas tab, select a regatta, click on Races/Tracking, scroll down and click tracking, and select replay. When the page loads go to the url and you will see a section that says "regattaName=" . Copy the text immediately following and before the next "&". Then replace all "+" with "%20".

For example with the following url:
```
https://www.sapsailing.com/gwt/RaceBoard.html?regattaName=49er+Worlds+2019&raceName=F15+Silver+(49er)&leaderboardName=49er+Worlds+2019&leaderboardGroupName=49er+%2F+49er+FX+%2F+Nacra+17+World+Championships+2019&eventId=e5a65f0a-b9b4-4630-b0b0-ad1fd7727518&mode=FULL_ANALYSIS
```

The regatta_name variable should be set to `49er%20Worlds%202019`

## What I Learned
Working on this program helped me understand how CSV files work, how to create them from JSON files using the python csv module, how to select only relevant data, and how to manipulate the data into the specific format required. I also had to draw on my previous experience working with the [SAP Sailing API](https://www.sapsailing.com/sailingserver/webservices/api/v1/index.html) and the formatting of their JSON files.
