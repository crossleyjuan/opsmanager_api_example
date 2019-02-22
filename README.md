# Ops Manager automation using API

This is an example code to retrieve and update the ops manager configuration. This could be used to perform a deployment of a new cluster or replicaset.

# Create your API Key

Before using the API you will need to create an API key associated to a user, use the following steps to create a new key:

- Select your Name in the top corner
- In the dropdown select Account
- In the API key section click generate key
- Save the API key somewhere safe as you wont be able to see it again.
- Take the IP of the PC where the code will be executed from and add it to the Whitelist IP addresses. This step is mandatory even if you plan to execute the code from the same server. The easiest way to get whitelist the right address will be to try to update the configuration, the error will let you known which IP address is the one you need to whitelist

# Configuration

copy the app.cfg.sample as app.cfg and complete the following values:

    {
       "mmsGroupId":"<mmsGroupId>",
       "user":"<user owner of the apikey>",
       "apikey":"<api key of the user>",
       "root":"<root of the ops manager example: http://1.1.1.1:8080/api/public/v1.0>"
    }

* mmsGroupId: This is the projectId, you can get this selecting the project and then going to "Settings" in the left menu, it will look similar to this: 5c6ed27c96335d4c60a45943
* user: user name owner of the API Key (User Profile --> account name)
* apikey: this is the key generated in the Section "Create your API Key"
* root: this will be the ops manager URL adding "api/public/v1.0" at the end

# Install required libraries

This application uses 2 libraries:

* requests: this library is a helper to consume REST services
* argparse: Argument Parser

if you have installed pip you can execute the following command:

python -m pip install -r requirements.txt

# Execute the test

The structure of the arguments are like this:

usage: automation.py [-h] [-o OUTPUT] {get-agents,get-config,put-config} ...

positional arguments:
  {get-agents,get-config,put-config}

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --ouput-file OUTPUT
                        Output to file

All the commands have a parameter to output the results to a file, use -o or --output-file to specify the output file, like this:

    python automation.py -o output.json get-agents

## Get Agents Running:

This will display all the agents running in the current project

python automation.py get-agents

## Get Current configuration:

This will retrieve the full configuration of the project, this includes agents, deployments, security configuration, etc.
python automation.py get-config

## Update Configuration:

This command can be used to update any configuration in the server, this includes performing a new deployment or changing parameters in a replica set, etc.

python automation.py put-config config-file.json

The config-file will contain the definition of the changes to be performed in the server, an example of this is provided in the example_replica.json and one more with an encrypted replica in example_replicaencrypted.json.
NOTE: these example files will require manual changes to match the names of the servers, paths, etc.
