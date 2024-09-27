import os
import sys
import time
import yaml
import requests

"""This script attempts health checks every 15 seconds if fed an appropriate YAML file containing URL endpoints, with support for body and header elements, printing out the overall percentage of reliability for the given healthcheck endpoints. For a cleaner version of this script that is less human but ironically more readable by humans in nature (ChatGPT), go here: """

def main(filepath): 
    counts = {}
    # Determines if the filepath exists and carries the .yml extension.
    if not (os.path.isfile(filepath) or filepath.endswith('.yml')):
        print(f"Error: The filepath is invalid.")
        return
    with open(filepath, 'r') as file:
        content = yaml.safe_load(file)
    # Infinite loop, 'til the ctrl+c break comes a-knockin'.
    while True:
        for entry in content:
            url = entry.get('url')
            headers = entry.get('headers', {})
            body = entry.get('body')
            # Here we check to see if the header has a method associated with it - if not, we assume get.
            if 'headers' in entry:
                method = entry['headers'].get('method')
            else:
                method = "get"
            # Initializes counts for each URL, if they do not already exist.
            if url not in counts:
                counts[url] = {'up_count': 0, 'down_count': 0}
            
            # Sends the healthcheck HTTP response. 
            response = getattr(requests, method.lower())(url, headers=headers, data=body)
            # Condition: If status code is 200-299, and has latency lower than 500ms, we consider it up!
            if response.status_code >= 200 and response.status_code <= 299 and (response.elapsed.total_seconds() * 1000) < 500:
                counts[url]['up_count'] += 1
            else:
                counts[url]['down_count'] += 1
            up_percentage = round(counts[url]['up_count'] / (counts[url]['up_count'] + counts[url]['down_count']) * 100)
            print(f"{url[8:].rstrip('/')} has {up_percentage}% availability percentage")
        time.sleep(15)


filepath = sys.argv[1]
main(filepath)