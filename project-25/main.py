import csv
import pandas

with open('./project-25/weather_data.csv', mode='r') as weather_data:
    data = weather_data.readlines()
    # print(data)

with open('./project-25/weather_data.csv', mode='r') as weather_data:
    data = csv.reader(weather_data)
    temperature = []
    for row in data:
        print(row)
        print(row[1])
        if row[1] != "temp":
            temperature.append(row[1])
    print(temperature)

data = pandas.read_csv('project-25/weather_data.csv')

# print(data)