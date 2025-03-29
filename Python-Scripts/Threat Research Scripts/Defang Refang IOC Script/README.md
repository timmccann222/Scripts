# Defang / Refang IOC Script

## Overview

This is a basic script which can be used to refang or defang a specific IOC or a list of IOC's in a JSON, CSV, or XLSX file. The following IOC's are supported:
* IP addresses
* Domains
* URL's

## Usage

The script can be used with the following commandline arguments seen below.

```bash
usage: DefangRefangIOC.py [-h] [--operation {defang,refang}] [--ioc IOC] [--ioc_type {ip,domain,url}] [--ioc_list IOC_LIST]
                          [--file_type {csv,json,xlsx}]

Defang/Refang an IOC or a list of IOC's.

options:
  -h, --help            show this help message and exit
  --operation {defang,refang}
                        Specify what operation to perform on IOC.
  --ioc IOC             Provide the IOC to defang/refang.
  --ioc_type {ip,domain,url}
                        Provide the IOC type.
  --ioc_list IOC_LIST   Provide a list of IOC's off the same type.
  --file_type {csv,json,xlsx}
                        Provide the file format for the list of IOC's.
```
