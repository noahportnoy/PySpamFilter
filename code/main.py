import os
import argparse
import file_handler
import training
import spam_filter
import plot

#=======================================================================
#---------------================  MAIN  ===============-----------------
#=======================================================================

#Get some Inputs
parser = argparse.ArgumentParser()
parser.add_argument("-st", "--strain", help="Enter the spam directory you want to train on")
parser.add_argument("-ht", "--htrain", help="Enter the ham directory you want to train on")
parser.add_argument("-sd", "--spam_detect", help="Enter email that you would like to check the spam ranking of. Must be in PySpamFilter directory")
parser.add_argument("-rw", "--rank_word", action='store_true', help="Enter a word of which you would like to know the spam ranking")
parser.add_argument("-ta", "--test_accuracy", nargs='*', help="Enter spam first and then ham email-directory that you would like to check the spam ranking of. Must be in PySpamFilter directory")
args = parser.parse_args()

#---------- If spam / ham is not inputed then send training_ham, spam--------
#Training HAM case
ham_dir = None
spam_dir = None

#Training SPAM case
if args.strain != None:
	#Check to see if directory is in directory
	if args.strain in os.listdir():
		# print("Spam training commencing!")
		spam_dir = args.strain
	else:
		print("There is no folder '"+args.strain+"' in this directory.")
		exit()
else:
	spam_dir = "training_spam"

if args.htrain != None:
	#Check to see if directory is in directory
	if args.htrain in os.listdir():
		# print("Ham training commencing!")
		ham_dir = args.htrain
	else:
		print("There is no folder '"+args.htrain+"' in this directory.")
		exit()
else:
	ham_dir = "training_ham"
#----------------------------------------------------------------------
print()
training.train_spam_filter(spam_dir, ham_dir)


#Spam Detect case
if args.spam_detect != None:
	if(os.path.isfile(args.spam_detect)) is True:
		#Detect the spam of this email!!
		print()
		spam_filter.spam_detect_email_file(args.spam_detect, "combined" , .0000000001, True )
		exit()
	else:
		print("There is no email '"+args.spam_detect+"' in this directory.")
		exit()

#Rank Word
if args.rank_word is True:
	print()
	input_word = input("Enter a word: ")
	while(input_word is not None):
		training.print_word_freq(input_word)
		print("The spamicity of", input_word, "is:", spam_filter.spam_rank(input_word))
		print()
		input_word = input("Enter a word: ")
	exit()

#Detect accuracy of a directory case
if args.test_accuracy != None:
	if len(args.test_accuracy) is 2:
		#Check if first (SPAM) and second (HAM) directorys are there
		if ((args.test_accuracy[0] in os.listdir()) & ((args.test_accuracy[1] in os.listdir()))):
			# print("Folders are good")
			test_spam_dir = args.test_accuracy[0]
			test_ham_dir = args.test_accuracy[1]
		else:
			print("There is no directory '"+args.test_accuracy[0]+"' or '"+args.test_accuracy[1]+"' in this directory.")
else:
	test_spam_dir = "test_spam"
	test_ham_dir = "test_ham"

#----------------------------------------------------------------------
plot_mean = spam_filter.test_accuracy(test_spam_dir, test_ham_dir, "mean")
plot_majority = spam_filter.test_accuracy(test_spam_dir, test_ham_dir, "majority")
plot_combined = spam_filter.test_accuracy(test_spam_dir, test_ham_dir, "combined")
spam_plots = [(plot_mean, "mean"), (plot_majority, "majority"), (plot_combined, "naive Bayes")]
plot.plot_detection_rates(spam_plots)
exit()


# original



# for presentation!
# print("Analyzing file: ./test_spam/00001.317e78fa8ee2f54cd4890fdc09ba8176")
# print()
# file_object = open("./test_spam/00001.317e78fa8ee2f54cd4890fdc09ba8176", 'U', encoding='utf-8', errors='replace')
# spam_filter.spam_detect_email(file_object, "combined", 0.0000000001)

# test for presentation
# print(training.print_word_freq('hello'))
# print(training.print_word_freq('free'))
# print(training.print_word_freq('thanks'))
# print(training.print_word_freq('friend'))
# print(training.print_word_freq('click'))
# print(training.print_word_freq('nigeria'))
# print(training.print_word_freq('hey'))
# print(training.print_word_freq('sir'))
# print(training.print_word_freq('sales'))

# print(spam_filter.spam_rank('hello'))
# print(spam_filter.spam_rank('free'))
# print(spam_filter.spam_rank('thanks'))
# print(spam_filter.spam_rank('friend'))
# print(spam_filter.spam_rank('click'))
# print(spam_filter.spam_rank('nigeria'))
# print(spam_filter.spam_rank('hey'))
# print(spam_filter.spam_rank('sir'))
# print(spam_filter.spam_rank('sales'));