## This is an demo on how to get and update a deployment configuration
## Using the Ops Manager API and automation
## For reference on how to use it please use the README.md

## This application will use the app.cfg file to configure the mandatory
## configuration like URL, user, apikey, etc.

import requests
from requests.auth import HTTPDigestAuth
import json
import sys
import argparse

## retrieve Agents runtime information
def get_agents(options):
    agent="/groups/%s/agents" % options["mmsGroupId"]
    url="%s%s" % (options["root"], agent)
    headers={ 'accept': 'application/json' }

    response = requests.get(url, auth=HTTPDigestAuth(options["user"], options["apikey"]), headers=headers)

    return response

## retrieve automation Configuration
def get_automation_config(options):
    automation="/groups/%s/automationConfig" % options["mmsGroupId"]
    url="%s%s" % (options["root"], automation)
    headers={ 'accept': 'application/json' }
    response = requests.get(url, auth=HTTPDigestAuth(options["user"], options["apikey"]), headers=headers)

    return response

## updates the automation configuration using the provided file
def put_automation_config(config, file):
    automation="/groups/%s/automationConfig" % options["mmsGroupId"]
    url="%s%s" % (options["root"], automation)
    headers={ 
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    with open(file, "r") as f:
         data = f.read()
         response = requests.put(url, 
                                 auth=HTTPDigestAuth(options["user"], options["apikey"]), 
                                 headers=headers, 
                                 data=data)
    return response
    
## parse the arguments from command-line
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--ouput-file", dest="output", help="Output to file")

    subparsers = parser.add_subparsers(dest="command")
    get_agents_parser = subparsers.add_parser("get-agents")
    get_config_parser = subparsers.add_parser("get-config")
    put_config_parser = subparsers.add_parser("put-config")
    put_config_parser.add_argument("file", help="Input file")
    return parser.parse_args()

## opens the app.cfg file to retrieve the json containing the mandatory parameters
## to connect to the Ops Manager API
def parse_config_file():
    with open("app.cfg", "r") as f:
        return json.loads(f.read())


def parse_response(response):
    if response.status_code == 200:
        result = json.dumps(json.loads(response.text), indent=3, sort_keys=True)

        if args.output is not None:
            with open(args.output, "w") as f:
                f.write(result)
        else:
            print(result)
    else:
        print("Result_code: %d, text: %s" % (response.status_code, response.text))

options = parse_config_file()

args = parse_arguments()

if args.command == "get-agents":
    response = get_agents(options)
elif args.command == "get-config":
    response = get_automation_config(options)
elif args.command == "put-config":
    response = put_automation_config(options, args.file)

parse_response(response)
