#!/usr/bin/env python3

import configparser
import requests
import json
import argparse
from datetime import datetime
import base64

# function loads configuration file.
def load_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

# function retrieves API key from configuration file.
def get_api_credentials(config):
    try:
        vt_api_key = config['API']['vt_api_key']
        return vt_api_key
    except KeyError as e:
        print(f"Missing key in config: {e}")
        return None

# function returns VT report for hash value.
def vt_hash_report(api_key, hash):
    url = "https://www.virustotal.com/api/v3/files/" + hash
    headers = {"accept": "application/json","x-apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        vt_print_report(response.json(), "hash")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# function returns VT report for url value.
def vt_url_report(api_key, url):
    # VT requires URL to be base64 encoded before making the API call.
    encoded_url = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    url = "https://www.virustotal.com/api/v3/urls/" + encoded_url
    headers = {"accept": "application/json","x-apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        vt_print_report(response.json(), "url")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# function returns VT report for domain value.
def vt_domain_report(api_key, domain):
    url = "https://www.virustotal.com/api/v3/domains/" + domain
    headers = {"accept": "application/json","x-apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        vt_print_report(response.json(), "domain")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# function returns VT report for IP address value.
def vt_ip_report(api_key, ip):
    url = "https://www.virustotal.com/api/v3/ip_addresses/" + ip
    headers = {"accept": "application/json","x-apikey": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        vt_print_report(response.json(), "ip")
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# function formats and displays VT report
def vt_print_report(response, report_type):
    if 'data' in response:
        print(r"""
     __     ___               _____     _        _   ____                       _
 \ \   / (_)_ __ _   _ __|_   _|__ | |_ __ _| | |  _ \ ___ _ __   ___  _ __| |_
  \ \ / /| | '__| | | / __|| |/ _ \| __/ _` | | | |_) / _ \ '_ \ / _ \| '__| __|
   \ V / | | |  | |_| \__ \| | (_) | || (_| | | |  _ <  __/ |_) | (_) | |  | |_
    \_/  |_|_|   \__,_|___/|_|\___/ \__\__,_|_| |_| \_\___| .__/ \___/|_|   \__|
                                                          |_|
    """)

        # Color Codes
        BOLD = '1'
        BLUE = '34'
        RESET = '0'

        if report_type == "hash":
            # Hash Report
            print(f"\033[{BOLD};{BLUE}mVT Link:\033[{RESET}m {response['data']['links']['self']}")
            print(f"\033[{BOLD};{BLUE}mMeaningful File Name:\033[{RESET}m {response['data']['attributes']['meaningful_name']}")
            print(f"\033[{BOLD};{BLUE}mFile SHA256 Hash:\033[{RESET}m {response['data']['attributes']['sha256']}")
            print(f"\033[{BOLD};{BLUE}mFile SHA1 Hash:\033[{RESET}m {response['data']['attributes']['sha1']}")
            print(f"\033[{BOLD};{BLUE}mFile MD5 Hash:\033[{RESET}m {response['data']['attributes']['md5']}")
            print(f"\033[{BOLD};{BLUE}mFile Reputation Score:\033[{RESET}m {response['data']['attributes']['reputation']}")
            print(f"\033[{BOLD};{BLUE}mFile Type:\033[{RESET}m {response['data']['type']}")
            print(f"\033[{BOLD};{BLUE}mFile Type Description:\033[{RESET}m {response['data']['attributes']['type_description']}")
            print(f"\033[{BOLD};{BLUE}mFile Type Extension:\033[{RESET}m {response['data']['attributes']['type_extension']}")
            print(f"\033[{BOLD};{BLUE}mCreation Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['creation_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mFirst Seen In The Wild:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['first_seen_itw_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mLast Modification Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['last_modification_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mFirst Submission Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['first_submission_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mLast Submission Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['last_submission_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mSuggested Threat Label:\033[{RESET}m {response['data']['attributes']['popular_threat_classification']['suggested_threat_label']}")
        elif report_type == "url":
            # URL Report
            print(f"\033[{BOLD};{BLUE}mVT Link:\033[{RESET}m {response['data']['links']['self']}")
            print(f"\033[{BOLD};{BLUE}mURL:\033[{RESET}m {response['data']['attributes']['url']}")
            print(f"\033[{BOLD};{BLUE}mURL Reputation:\033[{RESET}m {response['data']['attributes']['reputation']}")
            print(f"\033[{BOLD};{BLUE}mFirst Submission Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['first_submission_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mLast Submission Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['last_submission_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mLast Modification Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['last_modification_date']).strftime('%Y-%m-%d %H:%M:%S')}")
        elif report_type == "domain":
            print(f"\033[{BOLD};{BLUE}mVT Link:\033[{RESET}m {response['data']['links']['self']}")
            print(f"\033[{BOLD};{BLUE}mDomain:\033[{RESET}m {response['data']['id']}")
            print(f"\033[{BOLD};{BLUE}mDomain Reputation:\033[{RESET}m {response['data']['attributes']['reputation']}")
            print(f"\033[{BOLD};{BLUE}mCreation Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['creation_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mLast Analysis Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['last_analysis_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mLast Modification Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['last_modification_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mWHOIS Information:\033[{RESET}m {response['data']['attributes']['whois']}")
        elif report_type == "ip":
            print(f"\033[{BOLD};{BLUE}mVT Link:\033[{RESET}m {response['data']['links']['self']}")
            print(f"\033[{BOLD};{BLUE}mIP Address:\033[{RESET}m {response['data']['id']}")
            print(f"\033[{BOLD};{BLUE}mNetwork Range:\033[{RESET}m {response['data']['attributes']['network']}")
            print(f"\033[{BOLD};{BLUE}mCountry Code:\033[{RESET}m {response['data']['attributes']['country']}")
            print(f"\033[{BOLD};{BLUE}mIP Address Reputation:\033[{RESET}m {response['data']['attributes']['reputation']}")
            print(f"\033[{BOLD};{BLUE}mLast Analysis Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['last_analysis_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mLast Modification Date:\033[{RESET}m {datetime.fromtimestamp(response['data']['attributes']['last_modification_date']).strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"\033[{BOLD};{BLUE}mWHOIS Information:\033[{RESET}m {response['data']['attributes']['whois']}")
        else:
            print("\nNo file report data found.")

# function defines arguments that can be passed by a user.
def parse_args():
    parser = argparse.ArgumentParser(description="Get a file report from VirusTotal using IOC value.")
    parser.add_argument("--hash", type=str, required=False, help="The file hash (MD5, SHA-1, or SHA-256)")
    parser.add_argument("--url", type=str, required=False, help='Provide the URL to scan')
    parser.add_argument("--domain", type=str, required=False, help='Provide the domain to scan')
    parser.add_argument("--ip", type=str, required=False, help='Provide the IP address to scan')
    return parser.parse_args()

# defines the main function.
def main():
    # loads configuration file
    config = load_config()
    vt_api_key = get_api_credentials(config)

    print(f"VirusTotal API Key: {vt_api_key}")

    # generate report based on IOC provided
    args = parse_args()

    if args.hash:
        vt_hash_report(vt_api_key, args.hash)
    elif args.url:
        vt_url_report(vt_api_key, args.url)
    elif args.domain:
        vt_domain_report(vt_api_key, args.domain)
    elif args.ip:
        vt_ip_report(vt_api_key, args.ip)
    else:
        print("Error: You must provide either a hash, domain, IP address or a URL to scan.")
        parser = argparse.ArgumentParser()
        parser.print_help()


if __name__ == "__main__":
    main()
