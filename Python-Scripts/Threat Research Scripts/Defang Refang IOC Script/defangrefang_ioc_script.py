#!/usr/bin/env python3
import re
import argparse
import pandas as pd

# function defines arguments that can be passed by a user.
def parse_args():
    parser = argparse.ArgumentParser(description="Defang/Refang an IOC or a list of IOC's.")
    parser.add_argument("--operation", choices=["defang","refang"], type=str, required=False, help="Specify what operation to perform on IOC.")
    parser.add_argument("--ioc", type=str, required=False, help="Provide the IOC to defang/refang.")
    parser.add_argument("--ioc_type", choices=["ip","domain","url"], type=str, required=False, help="Provide the IOC type.")
    parser.add_argument("--ioc_list", type=str, required=False, help="Provide a list of IOC's off the same type.")
    parser.add_argument("--file_type", choices=["csv","json","xlsx"], type=str, required=False, help="Provide the file format for the list of IOC's.")
    return parser.parse_args()

# defang IP address
def defang_ip(ip):
    # check ip is valid
    if check_ip_address(ip):
        # replace periods with '[.]'
        return ip.replace('.', '[.]')
    else:
        print(f"{ip} is not a valid IP address.")

# defang domain
def defang_domain(domain):
    # replace periods with '[.]'
    return domain.replace('.', '[.]')

# defang URL
def defang_url(url):
    # check if url is valid:
    if check_url(url):
        # Replace "http://" and "https://" and periods in URL with '[.]'
        url = url.replace('http://', 'hxxp[:]//').replace('https://', 'hxxps[:]//').replace('ftp://','ftp[:]//')
        return url.replace('.','[.]')
    else:
        print(f"{url} is not a valid url.")

# refang IP address
def refang_ip(ip):
    # refang ip
    refanged_ip = ip.replace('[.]', '.')
    # check ip is valid
    if check_ip_address(refanged_ip):
        return refanged_ip
    else:
        print(f"{refanged_ip} is not a valid IP address.")

# refang domain
def refang_domain(domain):
    # refang periods
    return domain.replace('[.]', '.')

# refang URL
def refang_url(url):
    # refang urls
    url = url.replace('hxxp[:]//', 'http://').replace('hxxps[:]//', 'https://').replace('ftp[:]//','ftp://')
    refanged_url = url.replace('[.]','.')
    if check_url(refanged_url):
        return refanged_url
    else:
        print(f"{url} is not a valid url.")

# check ip address is valid
def check_ip_address(ip):
    try:
        # ipv4 regex pattern checks each octet is a number between 0 and 255
        ip_v4_pattern = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
        return bool(re.match(ip_v4_pattern, ip))
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

# check url is valid
def check_url(url):
    try:
        # url pattern check if the URL starts with http, https, or ftp and has a valid domain and path.
        url_pattern = r"^(https?|ftp):\/\/[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(:[0-9]+)?(\/[^\s]*)?$"
        return bool(re.match(url_pattern, url))
    except Exception as e:
        print(f"Error occurred: {e}")
        return False

# function defangs list of IOC's
def defang_ioc_list(ioc_list, file_type, ioc_type):
    try:
        # read ioc list
        if file_type == 'xlsx':
            df = pd.read_excel(ioc_list, engine="openpyxl")
        elif file_type == 'csv':
            df = pd.read_csv(ioc_list)
        elif file_type == 'json':
            df = pd.read_json(ioc_list)
        else:
            raise ValueError("Unsupported file type. Please use .json, .xlsx or .csv")

        # check if file is empty
        if df.empty:
            print("The file is empty")
        else:
            print("The file was read successfully.")
            # defang IOC based on type provided
            if ioc_type == 'ip':
                for row in df.values:
                    print(defang_ip(row[0]))
            elif ioc_type == 'url':
                for row in df.values:
                    print(defang_url(row[0]))
            elif ioc_type == 'domain':
                for row in df.values:
                    print(defang_domain(row[0]))
            else:
                raise ValueError("Unsupported IOC type. Please use ip, url or domain.")
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# function refangs list of IOC's
def refang_ioc_list(ioc_list, file_type, ioc_type):
    try:
        # read ioc list
        if file_type == 'xlsx':
            df = pd.read_excel(ioc_list, engine="openpyxl")
        elif file_type == 'csv':
            df = pd.read_csv(ioc_list)
        elif file_type == 'json':
            df = pd.read_json(ioc_list)
        else:
            raise ValueError("Unsupported file type. Please use .json, .xlsx or .csv")

        # check if file is empty
        if df.empty:
            print("The file is empty")
        else:
            print("The file was read successfully.")
            # defang IOC based on type provided
            if ioc_type == 'ip':
                for row in df.values:
                    print(refang_ip(row[0]))
            elif ioc_type == 'url':
                for row in df.values:
                    print(refang_url(row[0]))
            elif ioc_type == 'domain':
                for row in df.values:
                    print(refang_domain(row[0]))
            else:
                raise ValueError("Unsupported IOC type. Please use ip, url or domain.")
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# define main function
def main():
    # command line arguments
    args = parse_args()

    # defang/refang IOC based on user input
    if args.operation == "defang" and (args.ioc or (args.ioc_list and args.file_type)) and args.ioc_type == "ip":
        if args.ioc:
            print(defang_ip(args.ioc))
        else:
            defang_ioc_list(args.ioc_list, args.file_type, args.ioc_type)
    elif args.operation == "defang" and (args.ioc or (args.ioc_list and args.file_type)) and args.ioc_type == "domain":
        if args.ioc:
            print(defang_domain(args.ioc))
        else:
            defang_ioc_list(args.ioc_list, args.file_type, args.ioc_type)
    elif args.operation == "defang" and (args.ioc or (args.ioc_list and args.file_type)) and args.ioc_type == "url":
        if args.ioc:
            print(defang_url(args.ioc))
        else:
            defang_ioc_list(args.ioc_list, args.file_type, args.ioc_type)
    elif args.operation == "refang" and (args.ioc or (args.ioc_list and args.file_type)) and args.ioc_type == "ip":
        if args.ioc:
            print(refang_ip(args.ioc))
        else:
            refang_ioc_list(args.ioc_list, args.file_type, args.ioc_type)
    elif args.operation == "refang" and (args.ioc or args.ioc_list) and args.ioc_type == "domain":
        if args.ioc:
            print(refang_domain(args.ioc))
        else:
            refang_ioc_list(args.ioc_list, args.file_type, args.ioc_type)
    elif args.operation == "refang" and (args.ioc or args.ioc_list) and args.ioc_type == "url":
        if args.ioc:
            print(refang_url(args.ioc))
        else:
            refang_ioc_list(args.ioc_list, args.file_type, args.ioc_type)
    else:
        print("Error: please check command line arguments are correct!")
        parser = argparse.ArgumentParser()
        parser.print_help()

if __name__ == ('__main__'):
    main()
