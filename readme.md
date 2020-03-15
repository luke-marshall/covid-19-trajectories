# COVID-19 Trajectory Tracker

This tool shows all countries' case growth trajectories after a certain number of cases have been reached. For example, if the breakpoint is set to 200, the country_analysis script will generate a chart of how cases have grown in each country for a given number of days after 200 cases were observed. 

## Refreshing Data
Run `bash refresh_data.sh` - this will move the current file to the data_archive folder with the current date, and grab the latest data from the [Johns Hopkins CSSE github](https://github.com/CSSEGISandData/COVID-19). 

## Installing
Install python poetry first. Then run `poetry install`. This will install the required dependencies.

## Running the script

The main script is `country_analysis.py`. This shows the relevant chart (as per description above) and spits out a csv for further analysis. 
Run `poetry run python country_analysis.py`

Additionally, a `regional_analysis.py` script is included. This script does not show a chart, but generates a csv for further analysis which includes US and Australian regions separated by state, as well as some other international regions and all other countries' data. 
