# healthcheck-fetch
A take-home project requested of me applying for Fetch. I have two versions available here, but either healthchecker.py or healthchecker-cleaned.py can be used.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example YAML Configuration](https://github.com/Tedtanium/healthcheck-fetch/blob/main/sample.yml)

## Prerequisites

To run this project, make certain you have the following installed:

- **Python**: This project requires Python 3.6 or higher. You can download it from [python.org](https://www.python.org/downloads/).

- **Required Python Packages**: You will need the following packages:
  - `PyYAML`: For parsing YAML files.
  - `requests`: For sending HTTP requests.

## Installation

1. Download the appropriate file(s) from this repository! In this case, you'll want either [healthchecker.py](https://github.com/Tedtanium/healthcheck-fetch/blob/main/healthchecker.py), or if you'd like something a bit more human-readable but reformatted into best-practices by a ChatGPT front-end, I have [healthchecker-cleaned.py](https://github.com/Tedtanium/healthcheck-fetch/blob/main/healthchecker-cleaned.py). Those a bit more savvy, feel free to git clone away!

2. Install [Python](https://www.python.org/downloads/) for your respective operating system.

3. Using [this guide](https://packaging.python.org/en/latest/tutorials/installing-packages/), install the appropriate packages using `pip install pyyaml requests`.

## Usage

1. Create a YAML configuration file with the desired fields (e.g. header, body, method) you wish for the health check script to use. Format it similarly to the Example YAML Configuration I have uploaded [here](https://github.com/Tedtanium/healthcheck-fetch/blob/main/sample.yml). Or, alternatively, use that very file!

2. At any Python-enabled command line, run `python <path-to-health-checker.py> <path-to-yaml-file>`, and watch it go! You can quit at any time using CTRL-C.
