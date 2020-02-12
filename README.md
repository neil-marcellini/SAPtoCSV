# SAPtoCSV
This program accesses the SAP sailing analytics API and pulls gps data from all races of a specified regatta. The data is then written to a CSV file with a format that matches the output of another device, and stored in the csv_files folder, with subfolders for each race. There will be one CSV file for each competitor in a race.

## Prerequisites
You will need python3, pip, and venv. Or Pycharm.

## Getting Started
To run the program you can use Pycharm or run from terminal using venv. 

To use Pycharm:

Open Pycharm and go to File -> Open. Select the SAPtoCSV-master folder. You may need to configure the project interpreter.

To use venv from command line:

Open SAPtoCSV-master folder in terminal.

Enter the following commands:

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python main.py
To exit venv enter `deactivate`


## Configuration
No configuration is required to run, but if you want to select a different race then you must do the following:

To select a different regatta go to [sapsailing.com](https://www.sapsailing.com/gwt/Home.html), select an event, then click the regattas tab, select a regatta, click on Races/Tracking. Copy the url and set the global variable `regatta_url` to it.

## What I Learned
Working on this program helped me understand how CSV files work, how to create them from JSON files using the python csv module, how to select only relevant data, and how to manipulate the data into the specific format required. I also had to draw on my previous experience working with the [SAP Sailing API](https://www.sapsailing.com/sailingserver/webservices/api/v1/index.html) and the formatting of their JSON files.
