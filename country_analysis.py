import csv
import plotly.express as px
import plotly.graph_objects as go
import pandas
import numpy as np

BREAKPOINT = 30
GAP=BREAKPOINT * 2
MIN_DAYS = 7


# Extract data
country_lines = []
countries = {}
with open('time_series_19-covid-Confirmed.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    for line in reader:
        country = line[1]
        countries[country] = [0 for x in range(4,len(line))] if country not in countries else countries[country]
        for i in range(4,len(line)):
            countries[country][i-4] += int(line[i])
    

    
# Line up with date of first case
output_lines = []
for country in countries:
    if country not in ["China", "Cruise Ship"]:
        line = countries[country]
        for i in range(0,len(line)):
            if int(line[i]) > BREAKPOINT and int(line[i]) < BREAKPOINT + GAP:
                line = [country] + line[i:]
                # print(line)
                if len(line) >= MIN_DAYS:
                    output_lines.append(line)
                break


# Write to csv
with open('country.csv', mode='w') as regional_file:
    regional_writer = csv.writer(regional_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for line in output_lines:
        # print(line)
        
        regional_writer.writerow(line)
        

# Generate plot.

fig = go.Figure()
for line in output_lines:
    country = line[0]
    line = line[1:]
    x = [x for x in range(len(line))]
    print(x)
    fig.add_trace(go.Scatter( x=x,y=line,
                    mode='lines',
                    name=country))
fig.update_layout(
    title="Growth in COVID-19 cases after "+str(BREAKPOINT)+" cases observed (at least "+str(MIN_DAYS)+" days data available)",
    xaxis_title="Days since cases passed "+str(BREAKPOINT),
    yaxis_title="Number of Cases",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)
fig.show()

                