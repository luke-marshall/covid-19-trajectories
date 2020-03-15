# COVID-19 Trajectory Tracker

## Refreshing Data
Run `bash refresh_data.sh` - this will move the current file to the data_archive folder with the current date, and grab the latest data from the (Johns Hopkins CSSE github)[https://github.com/CSSEGISandData/COVID-19]. 

## Installing
Install python poetry first. Then run `poetry install`

## Running the script

Run `poetry run python country_analysis.py`
