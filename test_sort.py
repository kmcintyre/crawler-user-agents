import json
from collections import OrderedDict

def check_lower(pair):
    key,value = pair
    return (key.lower(),value)

crawlers = json.load(open('crawler-user-agents.json'))
sorted_crawler = OrderedDict(sorted(crawlers.items(), key=lambda x: x[1].lower()))

json.dump(sorted_crawler, open('crawler-user-agents-2.json', 'w'), indent=4)
