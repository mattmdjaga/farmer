

import requests
import csv

url = 'https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/383116/rawdata_new.csv?sequence=1&isAllowed=y'

response = requests.get(url)
with open('data_raw.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for line in response.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))