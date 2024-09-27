import os
import sys
import time
import yaml
import requests

"""This is a version of the original script (healthchecker.py) that I threw at ChatGPT and said 'Clean this up for me as per best practices', after validating that what I wrote worked as intended first. (This version has also been tested, so either should run fine.)"""

def load_yaml(filepath):
    """Load the YAML file and return its content."""
    if not os.path.isfile(filepath) or not filepath.endswith('.yml'):
        raise ValueError("Error: The filepath is invalid.")
    
    with open(filepath, 'r') as file:
        return yaml.safe_load(file)

def get_http_method(entry):
    """Determine the HTTP method from the entry, defaulting to 'GET'."""
    return entry.get('headers', {}).get('method', 'get').lower()

def send_healthcheck(url, headers, body, method):
    """Send the healthcheck request and return the response."""
    response = getattr(requests, method)(url, headers=headers, data=body)
    return response

def update_counts(counts, url, response):
    """Update the up and down counts based on the response status."""
    if 200 <= response.status_code < 300 and (response.elapsed.total_seconds() * 1000) < 500:
        counts[url]['up_count'] += 1
    else:
        counts[url]['down_count'] += 1

def calculate_availability(counts, url):
    """Calculate and return the availability percentage for the URL."""
    total_count = counts[url]['up_count'] + counts[url]['down_count']
    return round(counts[url]['up_count'] / total_count * 100) if total_count > 0 else 0

def main(filepath):
    counts = {}
    content = load_yaml(filepath)
    
    try:
        while True:
            for entry in content:
                url = entry.get('url')
                headers = entry.get('headers', {})
                body = entry.get('body')
                method = get_http_method(entry)

                if url not in counts:
                    counts[url] = {'up_count': 0, 'down_count': 0}

                response = send_healthcheck(url, headers, body, method)
                update_counts(counts, url, response)

                up_percentage = calculate_availability(counts, url)
                print(f"{url[8:].rstrip('/')} has {up_percentage}% availability percentage")
            time.sleep(15)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_yaml_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    main(filepath)