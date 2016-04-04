import json
import csv
from pprint import pprint


with open("./gmap.json") as file:
    # json coming from file - use json.load
    result = json.load(file)
    # json coming from http or some string, use json.loads (S stands from string)
    # result = json.loads(file.read())
    # print(result)
    pprint(result)

# with open("./sales.csv") as f:
#     reader = csv.reader(f, delimiter=',')
#     for row in reader:
#         print(row)




