# VirusTotal Script

## Overview

This is a basic VirusTotal script which can be used to perform the following activities:

* Retrieve VirusTotal report based on hash value.
* Retrieve VirusTotal report based on URL value.
* Retrieve VirusTotal report based on domain value.
* Retrieve VirusTotal report based on IP address value.

## Usage

The script can be used with the following commandline arguments seen below.

```bash
usage: ThreatRecon.py [-h] [--hash HASH] [--url URL] [--domain DOMAIN] [--ip IP]

Get a file report from VirusTotal using IOC value.

options:
  -h, --help       show this help message and exit
  --hash HASH      The file hash (MD5, SHA-1, or SHA-256)
  --url URL        Provide the URL to scan
  --domain DOMAIN  Provide the domain to scan
  --ip IP          Provide the IP address to scan
```

**N.B.** Ensure the `config.ini` file is populated with your API key from VirusTotal.
