#Spam Filter designed by N. Portnoy and A. Sousa
import rlcompleter
import readline
import string
import os
import re
#
#
#==========================================================
#------------------ IMPORTANT -----------------------------
#Parente wants us to make the filter in 3 ways:
#   -MAJORITY 
#   -AVERAGE
#   -AND ONE OTHER
#
#

print ("Filter Dat SPAM!");

#Some variables that will be used below
#current = file_object.readline()
word_list = []
file_list = []

#Parse the given file by word
def parseLine(current_line):
	while current_line != '':
		#print (current_line)
		current_line = file_object.readline();
		test = re.split(' |!|"|:|\W+|-|\n|''|', current_line)
		for item in test:
			if item == '':
				None
			else:
				word_list.append(item)

#Trim out the header of the email. Find the first empty line
def parseEmail(file_object):
	found = False;
	x=0
	current = file_object.readline();
	while found == False:
		if current == '\n':
			print ("Goood to go!");
			found = True;
			parseLine(current)
			break;
		else:
			x += 1;
			current = file_object.readline();
			print(current)
			if x > 100:
				break;

def findFile():
	v=0
	for file in os.listdir("./spam"):
	    if file.endswith(""):
	    	if v == 4:
	    		v=0
	    	else:
		    	file_list.append(file)
		    	v += 1

#Method that returns #Spam and #ham 
def getSpamCount():
	print ("Yet to do")
def getHamCount():
	print ("Yet to do")

#MAIN - Where all the action happens:
#First find the right file
findFile()

#Then cut the header off and finally add all words to the master list
for item in file_list:
	filename = "spma/" + item
	file_object = open(filename, 'U', encoding='utf-8', errors='replace')
	print ("Opening file: ", item)
	parseEmail(file_object)

#OLD - but this worked... sort of
#[word_list.append(word.strip(string.punctuation)) for word in current_line.split()])

#print (word_list)
