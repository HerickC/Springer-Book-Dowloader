import csv
import os
import requests

if not os.path.exists('Downloads'):
    os.makedirs('Downloads')


with open('Springer.csv') as csvfile:
    csvReader = csv.DictReader(csvfile)
    for row in csvReader:

        # uncomment this line to download only a especific area
        # if(row['Area'] == "Computer Science"):
        path = 'Downloads/'+row['Area']
        if not os.path.exists(path):
            os.makedirs(path)
        print("Downloading '"+row['Title']+"'...")
        r = requests.get(row['DirectLink'])
        with open(path+'/'+row['Title']+'.pdf', 'wb') as f:
            f.write(r.content)
