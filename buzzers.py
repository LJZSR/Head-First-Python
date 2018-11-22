from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v

pprint.pprint(flights)
print()

fts = {}
fts = {convert2ampm(k): v.title()
       for k, v in flights.items()}
pprint.pprint(fts)
print()

when = {}
dests = set(fts.values())
for dest in dests:
    when[dest] = [k for k,v in fts.items() if v == dest]

pprint.pprint(when)
