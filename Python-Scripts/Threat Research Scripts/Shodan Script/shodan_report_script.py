#!/usr/bin/env python3
import configparser
import argparse
import shodan
import json

# function loads configuration file.
def load_config(file_path='config.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

# function retrieves API key from configuration file.
def get_api_credentials(config):
    try:
        shodan_api_key = config['API']['shodan_api_key']
        return shodan_api_key
    except KeyError as e:
        print(f"Missing key in config: {e}")
        return None

# function defines arguments that can be passed by a user.
def parse_args():
    parser = argparse.ArgumentParser(description="Query shodan based on provided artefact.")
    parser.add_argument("--ip", type=str, required=False, help="The IP address used to perform host search.")
    return parser.parse_args()

# Shodan Host Search function
def shodan_host_search(api, ip_address):
    try:
        host = api.host(ip_address)

        # Color Codes
        BOLD = '1'
        RED = '31'
        RESET = '0'

        print(r"""
   ____  _               _               ____                       _
 / ___|| |__   ___   __| | __ _ _ __   |  _ \ ___ _ __   ___  _ __| |_
 \___ \| '_ \ / _ \ / _` |/ _` | '_ \  | |_) / _ \ '_ \ / _ \| '__| __|
  ___) | | | | (_) | (_| | (_| | | | | |  _ <  __/ |_) | (_) | |  | |_
 |____/|_| |_|\___/ \__,_|\__,_|_| |_| |_| \_\___| .__/ \___/|_|   \__|
                                                 |_|
    """)

        # Print host information
        print(f"\033[{BOLD};{RED}mIP:\033[{RESET}m {host['ip_str']}")
        print(f"\033[{BOLD};{RED}mOrganization:\033[{RESET}m {host.get('org', 'n/a')}")
        print(f"\033[{BOLD};{RED}mOperating System:\033[{RESET}m {host.get('os', 'n/a')}")
        print(f"\033[{BOLD};{RED}mCountry:\033[{RESET}m {host['country_name']}")
        print(f"\033[{BOLD};{RED}mCity:\033[{RESET}m {host.get('city', 'n/a')}")
        print(f"\033[{BOLD};{RED}mOpen Ports:\033[{RESET}m {host['ports']}")

         # Print banner data for each service
        for service in host['data']:
            print(f"\033[{BOLD};{RED}m\nPort:\033[{RESET}m {service['port']}")
            print(f"\033[{BOLD};{RED}mBanner:\n\033[{RESET}m{service['data']}")

    except shodan.APIError as e:
        print(f"Shodan API Error: {e}")

    except Exception as ex:
        print(f"Unexpected Error: {ex}")

# defines the main function.
def main():
    # loads configuration file
    config = load_config()
    shodan_api_key = get_api_credentials(config)
    print(f"Shodan API Key: {shodan_api_key}")

    # Initialize the Shodan API
    api = shodan.Shodan(shodan_api_key)

    # Perform search based on provided input.
    args = parse_args()

    if args.ip:
        shodan_host_search(api,args.ip)
    else:
        print("Error: Incorrect value provided!")
        parser = argparse.ArgumentParser()
        parser.print_help()

if __name__ == "__main__":
    main()
