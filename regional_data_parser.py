import csv

output_lines = []
with open('time_series_19-covid-Confirmed.csv') as f:
    reader = csv.reader(f)
    header = next(reader)
    
    for line in reader:
        # print(line)
        
        location = line[1] if line[0] == "" else line[0] + " " + line[1]
        # print(location)
        # detected = False
        for i in range(4,len(line)):
            if int(line[i]) > 0:
                line = line[:4] + line[i:]
                # print(line)
                output_lines.append(line)
                break



with open('regional.csv', mode='w') as regional_file:
    regional_writer = csv.writer(regional_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    for line in output_lines:
        # print(line)
        location = line[1] if line[0] == "" else line[0] + " " + line[1]
        regional_writer.writerow([location]+line[4:])
        
        

        

                