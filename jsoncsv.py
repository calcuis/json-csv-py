import json, csv

with open('data.json', encoding='utf-8-sig') as json_file:
    jsondata = json.load(json_file)

data_file = open('data.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(data_file)

count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

data_file.close()
