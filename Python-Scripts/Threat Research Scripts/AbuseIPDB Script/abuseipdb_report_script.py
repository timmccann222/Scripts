#!/usr/bin/env python3
import configparser
import requests
import argparse
import json
import pandas as pd

# function loads configuration file.
def load_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config
  
# function retrieves API key from configuration file.
def get_api_credentials(config):
    try:
        abuseipdb_api_key = config['API']['abuseipdb_api_key']
        return abuseipdb_api_key
    except KeyError as e:
        print(f"Missing key in config: {e}")
        return None
# function defines arguments that can be passed by a user.
def parse_args():
    parser = argparse.ArgumentParser(description="Get a report from AbuseIPDB based on a provided IP address.")
    parser.add_argument("--ip", type=str, required=False, help="Provide an IP address to AbuseIPDB and return results.")
    parser.add_argument("--ip_list", type=str, required=False, help="Provide a list of IP addresses to AbuseIPDB and return results.")
    parser.add_argument("--file_type", choices=["csv","json","xlsx"], type=str, required=False, help="Provide ")
    return parser.parse_args()

# function returns AbuseIPDB report for IP address.
def check_ip(ip, api_key):
    # api url
    url = "https://api.abuseipdb.com/api/v2/check"

    # http headers
    headers = {
        "Key": api_key,
        "Accept":"application/json",
        }

    # http params
    params = {
        "maxAgeInDays": 90,
        "ipAddress": ip
        }

    # http GET request
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# function returns AbuseIPDB report for list of IP addresses.
def check_ip_list(ip_list, file_type, api_key):
    try:
        # read ip_list
        if file_type == 'xlsx':
            df = pd.read_excel(ip_list, engine="openpyxl")
        elif file_type == 'csv':
            df = pd.read_csv(ip_list)
        elif file_type == 'json':
            df = pd.read_json(ip_list)
        else:
            raise ValueError("Unsupported file type. Please use .json, .xlsx or .csv")

        # check if file is empty
        if df.empty:
            print("The file is empty")
        else:
            print("The file was read successfully.")
            # loop through list of IP Addresses
            for row in df.values:
                check_ip(row[0],api_key)

    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# defines the main function.
def main():
    # load configuration
    config = load_config()
    abuseipdb_api_key = get_api_credentials(config)
    print(f"AbuseIPDB API Key: {abuseipdb_api_key}")

    # command line arguments
    args = parse_args()

    if args.ip:
        check_ip(args.ip, abuseipdb_api_key)
    elif args.ip_list and args.file_type:
        check_ip_list(args.ip_list, args.file_type, abuseipdb_api_key)
    else:
        print("Error: please check command line arguments are correct!")
        parser = argparse.ArgumentParser()
        parser.print_help()

if __name__ == "__main__":
    main()
