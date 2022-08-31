import json
import sys

# JSON file argument
json_file_name = sys.argv[1]
# Opening JSON file
fp = open(json_file_name)
# returns JSON object as a dictionary
data = json.load(fp)

# Investigate Logs
for dictionary in data['Records']:
	# Get method returns None if key does not exist.
	time = dictionary.get('eventTime')
	source_ip = dictionary.get('sourceIPAddress')
	event_name = dictionary.get('eventName')
	user_type = dictionary.get('userIdentity').get('type')
	user_accountid = dictionary.get('userIdentity').get('accountId')
	user_arn = dictionary.get('userIdentity').get('arn')

	print(time, source_ip, event_name, user_type, user_accountid, user_arn)

# Closing file
fp.close()