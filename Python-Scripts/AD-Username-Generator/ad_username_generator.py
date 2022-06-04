import argparse

# use -f as an option which takes file/file path as an argument. 
parser = argparse.ArgumentParser(description="Generate AD usernames based on name and surname", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-f", type=argparse.FileType('r'), help="Text file containing names and surnames")
args = parser.parse_args()


# Split List of Names and Surnames based on newline
open_file = args.f.read().split('\n')

# Contains sublist of each name and surname
dict = []

# Split each name and surname in list by blank space.
# Add each new sublist to a new list (i.e. dict)
for names in open_file:
	values = names.split(' ')
	dict.append(values)

# Generate usernames based on naming coventions
for row in dict:
	name = row[0].lower()
	surname = row[1].lower()
	#NameSurname
	print(name + surname)
	print(name + surname)
	#Name.Surname
	print(name + "-" + surname)
	#Name-Surname
	print(name + "." + surname)
	#NamSur
	print(name[0:3] + surname[0:3])
	#Nam-Sur
	print(name[0:3] + "-" + surname[0:3])
	#Nam.Sur
	print(name[0:3] + "." + surname[0:3])
	#NSurname
	print(name[0] + surname)
	#N-Surname
	print(name[0] + "-" + surname)
	#N.Surname
	print(name[0] + "." + surname)
	#SurnameName
	print(surname + name)
	#Surname-Name
	print(surname + "-" + name)
	#Surname.Name
	print(surname + "." + name)
	#SurNam
	print(surname[0:3] + name[0:3])
	#Sur-Nam
	print(surname[0:3] + "-" + name[0:3])
	#Sur.Nam
	print(surname[0:3] + "." + name[0:3])
	#Sname
	print(surname[0] + name)
	#S-name
	print(surname[0] + "-" + name)
	#S.name
	print(surname[0] + "." + name)
	#SurnameN
	print(surname + name[0])
	#Surname-N
	print(surname + "-" + name[0])
	#Surname.N
	print(surname + "." + name[0])