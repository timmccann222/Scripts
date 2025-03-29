# AbuseIPDB Script

## Overview

This is a basic script which can be used to return records from AbuseIPDB for a specific IP address or a list of IP addresses in a JSON, CSV, or XLSX file.

## Usage

The script can be used with the following commandline arguments seen below.

```bash
usage: AbuseIPDB.py [-h] [--ip IP] [--ip_list IP_LIST] [--file_type {csv,json,xlsx}]

Get a report from AbuseIPDB based on a provided IP address.

options:
  -h, --help            show this help message and exit
  --ip IP               Provide an IP address to AbuseIPDB and return results.
  --ip_list IP_LIST     Provide a list of IP addresses to AbuseIPDB and return results.
  --file_type {csv,json,xlsx}
                        Provide the file format for the list of IP addresses.
```

**N.B.** Ensure the `config.ini` file is populated with your API key from AbuseIPDB.
