#!/usr/bin/env python3
import requests
import configparser
import json
import pandas as pd
import argparse


# function loads configuration file.
def load_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

# function retrieves API key from configuration file.
def get_api_credentials(config):
    try:
        abusech_api_key = config['API']['abusech_api_key']
        return abusech_api_key
    except KeyError as e:
        print(f"Missing key in config: {e}")
        return None

# function defines arguments that can be passed by a user.
def parse_args():
    parser = argparse.ArgumentParser(description="Query IOC's in Abuse.ch")
    parser.add_argument("--ioc", type=str, required=False, help="Search for IOC on ThreatFox.")
    parser.add_argument("--hash", type=str, required=False, help="Search for IOC associated with hash in ThreatFox.")
    parser.add_argument("--malware_family", type=str, required=False, help="Searching for IOCs on ThreatFox that are associated with a malware family.")
    parser.add_argument("--url", type=str, required=False, help="Search for url in URLHaus.")
    parser.add_argument("--file_name", type=str, required=False, default='threat_report', help="Provide name of file for report (e.g. test_report.xlsx).")
    return parser.parse_args()

# search IOC on ThreatFox
def search_ioc_threatfox(api_key, ioc, file_name):
    print(f"Searching for the IOC '{ioc}' on ThreatFox.....")
    # URL
    url = "https://threatfox-api.abuse.ch/api/v1/"

    # HTTP POST Headers
    post_headers = {
        "Auth-Key":api_key
        }

    # HTTP POST parameters
    post_params = {
        "query":"search_ioc",
        "search_term":ioc,
        "exact_match":"true"
        }

    # HTTP POST request
    response = requests.post(url, headers=post_headers, json=post_params)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
        create_report(response.json(),file_name)
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# search IOC by file hash on ThreatFox
def search_hash_threatfox(api_key, hash, file_name):
    print(f"Searching for IOCs associated with the hash '{hash}'.....")
    # URL
    url = "https://threatfox-api.abuse.ch/api/v1/"

    # HTTP POST Headers
    post_headers = {
        "Auth-Key":api_key
        }

    # HTTP POST parameters
    post_params = {
        "query":"search_hash",
        "hash":hash,
        }

    # HTTP POST request
    response = requests.post(url, headers=post_headers, json=post_params)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
        create_report(response.json(),file_name)
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# query malware
def query_malware_threatfox(api_key, malware, file_name):
    print(f"Searching for IOCs on ThreatFox that are associated with the malware family '{malware}'....")
    # URL
    url = "https://threatfox-api.abuse.ch/api/v1/"

    # HTTP POST Headers
    post_headers = {
        "Auth-Key":api_key
        }

    # HTTP POST parameters
    post_params = {
        "query":"malwareinfo",
        "malware":malware,
        "limit":100
        }

    # HTTP POST request
    response = requests.post(url, headers=post_headers, json=post_params)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
        create_report(response.json(),file_name)
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# query URL IOC
def query_urlhaus(auth_key, url, file_name):
    print(f"Searching for information about the URL '{url}' from URLhaus.....")
    # Construct the HTTP request
    data = {
        'url' : url
    }
    # Set the Authentication header
    headers = {
        "Auth-Key"      :   auth_key
    }
    response = requests.post('https://urlhaus-api.abuse.ch/v1/url/', data, headers=headers)
    # Parse the response from the API
    json_response = response.json()
    if json_response['query_status'] == 'ok':
        print(json.dumps(json_response, indent=4, sort_keys=False))
        create_report(response.json(),file_name)
    elif json_response['query_status'] == 'no_results':
        print("No results")
    else:
        print(json_response['query_status'])

# generates an .xlsx report
def create_report(results, file_name):
    print(f"Generating a report titled '{file_name}'.....")

    # check file name is provided
    if not file_name.strip():
        print("Error: No file name provided.")
        return

    # create file name
    file_name = file_name.strip()
    if not file_name.lower().endswith(".xlsx"):
        file_name += ".xlsx"

    # Flattened JSON data storage
    flattened_data = []

    # Process ThreatFox JSON format
    if "data" in results and isinstance(results["data"], list):
        for item in results["data"]:
            flattened_entry = pd.json_normalize(item)
            flattened_data.append(flattened_entry)
    else:
        # Process URLHaus JSON format or other cases
        flattened_entry = pd.json_normalize(results)
        flattened_data.append(flattened_entry)

    # Ensure data exists before attempting to concatenate
    if not flattened_data:
        print("Error: No valid data to process.")
        return

    df = pd.concat(flattened_data, ignore_index=True)

    try:
        # Write to Excel
        df.to_excel(file_name, index=False)
        print(f"File '{file_name}' saved successfully.")
    except Exception as e:
        print(f"Error saving file '{file_name}': {e}")

# defines main function
def main():
    # load API configuration
    config = load_config()
    abusech_api_key = get_api_credentials(config)
    print(f"AbuseCH API Key: {abusech_api_key}")

    # command line arguments
    args = parse_args()

    if args.malware_family and args.file_name:
        query_malware_threatfox(abusech_api_key, args.malware_family, args.file_name)
    elif args.url and args.file_name:
        query_urlhaus(abusech_api_key, args.url, args.file_name)
    elif args.ioc and args.file_name:
        search_ioc_threatfox(abusech_api_key, args.ioc, args.file_name)
    elif args.hash and args.file_name:
        search_hash_threatfox(abusech_api_key, args.hash, args.file_name)
    else:
        print("Error: please check command line arguments are correct!")
        parser = argparse.ArgumentParser()
        parser.print_help()

if __name__ == ("__main__"):
    main()
