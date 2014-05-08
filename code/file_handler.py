import os
import re

#Some variables that will be used below
spam_email_count = 0
ham_email_count = 0

#Method that returns #Spam and #ham 
def setSpamEmailCount(count):
	global spam_email_count
	spam_email_count = count

def setHamEmailCount(count):
	global ham_email_count
	ham_email_count = count

def getSpamEmailCount():
	if spam_email_count == 0:
		print("WARNING: spam email count is zero!")

	return spam_email_count

def getHamEmailCount():
	if ham_email_count == 0:
		print("WARNING: ham email count is zero!")

	return ham_email_count

#Parse the given file by word
def parseLine(current_line, words):
	if current_line != '':
		current_line = re.split('\n', current_line)[0]
		test = re.split(' |!|"|:|\W+|-|\n|''|', current_line)
		# print(test)
		for item in test:
			if item == '':
				None
			else:
				words.append(item)

	return words

# DON'T trim out the header of the email!
def parseEmail(*args):
	if len(args) == 2:
		file_object = args[0]
		words = args[1]

	elif len(args) == 1:
		file_object = args[0]
		words = []

	for current in file_object:
		words = parseLine(current, words)

	return words

# Trim out the header of the email. Find the first empty line
# def parseEmail(*args):
# 	if len(args) is 2:
# 		file_object = args[0]
# 		words = args[1]

# 	elif len(args) is 1:
# 		file_object = args[0]
# 		words = []

# 	found = False
# 	x=0
# 	for current in file_object:
# 		if found == False:
# 			if current == '\n':
# 				# print ("Goood to go!")
# 				found = True
# 			else:
# 				x += 1
# 				# print(current)
# 				# if x > 100:
# 				# 	break

# 		if found == True:
# 			words = parseLine(current, words)

# 	return words

def findFiles(directory):
	file_count = 0
	file_list = []

	for file in os.listdir(directory):

		if file.endswith(""):
			file_list.append(file)
			file_count += 1

	return file_list


#parseTrainingDirectory() - Where all the action happens:
#First find the right file
def parseTrainingDirectory(directory):
	word_list = []
	file_list = findFiles("./" + directory)
	print("Parsing", directory, "directory...")

	if "spam" in directory:
		# print("Length of file_list is", len(file_list))
		setSpamEmailCount(len(file_list))
	elif "ham" in directory:
		# print("Length of file_list is", len(file_list))
		setHamEmailCount(len(file_list))

	#Then cut the header off and finally add all words to the master list
	for item in file_list:
		filename = directory + "/" + item
		file_object = open(filename, 'U', encoding='utf-8', errors='replace')
		# print ("Opening file: ", item)
		word_list = parseEmail(file_object, word_list)

	return word_list

