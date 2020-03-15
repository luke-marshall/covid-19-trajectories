today=`date '+%Y_%m_%d__%H_%M_%S'`;
filename="data_archive/$today.csv"
echo $filename
mv time_series_19-covid-Confirmed.csv $filename

wget https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv
