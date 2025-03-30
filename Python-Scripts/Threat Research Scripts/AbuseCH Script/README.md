# AbuseCH Script

## Overview

This is a basic script which can be used to genertae an .xlsx report for IOC(s) from Abuse.ch products ThreatFox and URLHaus.

## Usage

The script can be used with the following commandline arguments seen below.

```bash
usage: AbuseCH2.py [-h] [--ioc IOC] [--hash HASH] [--malware_family MALWARE_FAMILY] [--url URL] [--file_name FILE_NAME]

Query IOC's in Abuse.ch

options:
  -h, --help            show this help message and exit
  --ioc IOC             Search for IOC on ThreatFox.
  --hash HASH           Search for IOC associated with hash in ThreatFox.
  --malware_family MALWARE_FAMILY
                        Searching for IOCs on ThreatFox that are associated with a malware family.
  --url URL             Search for url in URLHaus.
  --file_name FILE_NAME
                        Provide name of file for report (e.g. test_report.xlsx).
```

**N.B.** Ensure the `config.ini` file is populated with your API key from Abuse.ch.

