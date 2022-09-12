# https://tryhackme.com/room/scripting
import socket

def port_connection(website, port):
	# create an INET, STREAMing socket, TCP
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# now connect to the server on port the speciifed port
	s.connect((website, port))
	s.sendall(bytes("GET / HTTP/1.1\r\nHost: {ip}:{port}\r\n\r\n".format(ip=website, port=port), encoding='utf8'))
	# return response from server
	response = s.recv(1024)
	# decode response
	data = response.decode("utf-8")
	s.close()

	return data


def response_filter(data):
	response = data.splitlines() # split lines
	values = response[6].split() # split words

	return values[0], values[1], values[2]


def number_operation(op, orig_num, new_num):
	print("Operation: ", op, orig_num, new_num)
	result = 0
	if op == "add":
		result = orig_num + new_num
	elif op == "minus":
		result = orig_num - new_num
	elif op == "divide":
		result = orig_num / new_num
	elif op == "multiply":
		result = orig_num * new_num
	else:
		result = None

	print("Result: ", result)
	return result


original_num = 0.0
server_port = 1337

while server_port != 9765:
	try:
		# response data from server
		data = port_connection("10.10.239.179", server_port)
		# operation, number and port values from server
		operation, new_num, new_port = response_filter(data)
		# perform operation
		result = number_operation(operation, float(original_num), float(new_num))
		original_num = float(result)
		# store new port number
		server_port = int(new_port)

		print("Operation Result: {orig_num}\nNext Port: {port}".format(orig_num=original_num, port=server_port))

	except:
		pass

print("Flag: ", round(original_num, 2))