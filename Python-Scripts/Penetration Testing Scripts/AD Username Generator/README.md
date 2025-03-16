# Active Directory Username Generator

During a penetration test, usernames can be extracted from internal documents, social media, services (mainly web) inside the domain environments and also from the publicly available (i.e. OSINT).

This python script is used to generate potential usernames based on a list of names gathered during OSINT. The script then outputs a list of potential usernames using the common AD username conventions seen below.

```
NameSurname
Name.Surname
NamSur
Nam.Sur
NSurname
N.Surname
SurnameName
Surname.Name
SurnameN
Surname.N
```

## Usage

`-f`: file path

```bash
python3 ad_username_generator.py -f names.txt
```
