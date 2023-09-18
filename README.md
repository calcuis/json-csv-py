## convert json to csv

This Python code reads data from a JSON file, converts it to CSV format, and writes it to another file. Here's a step-by-step explanation of the code:

Importing Modules:
```
import json, csv
```
The code imports the necessary modules: json for working with JSON data and csv for working with CSV data.

Opening and Reading JSON File:
```
with open('data.json', encoding='utf-8-sig') as json_file:
    jsondata = json.load(json_file)
```
The code opens a JSON file named data.json and loads its content into the jsondata variable using `json.load()`. The encoding='utf-8-sig' parameter is used to handle the UTF-8 encoding with a byte order mark (BOM) if present.

Opening and Writing to CSV File:
```
data_file = open('data.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(data_file)
```
The code opens a CSV file named data.csv for writing ('w' mode) and creates a CSV writer object using `csv.writer()`.

Writing CSV Header:
```
count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
```
It iterates through the data in the JSON file. If count is 0 (first iteration), it extracts the keys (assumed to be the header) from the first JSON object and writes them as the CSV header using `csv_writer.writerow()`. The count is then incremented to ensure that only one header row is written.

Writing CSV Data Rows:
```
csv_writer.writerow(data.values())
```
For each JSON object (excluding the first one, which was used for the header), it writes the corresponding values as a row in the CSV file using `csv_writer.writerow()`.

Closing the CSV File:
```
data_file.close()
```
Finally, it closes the CSV file to ensure that all the data is written and the file is properly closed.
