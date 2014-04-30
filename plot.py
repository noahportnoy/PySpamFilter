#import matplotlib.pyplot as plt
import os
import training
import spam_filter
import file_handler
import argparse


# plot detection rate versus false positive rate
# make multiple plots like this ^ for different methods of determining spam/non-spam (averaging, median, etc.)
# todo: handle tuples?
def plot_detection_rates(plots):
	
	for spam_plot, method in plots:
		plt.plot(*zip(*spam_plot), label = method);

	plt.ylabel('detection rate');
	plt.xlabel('false positive rate')
	plt.title('Spam Filter Accuracy with Varying Threshold (Ignores Headers)')
	plt.legend()
	plt.show();


#=======================================================================
#---------------================  MAIN  ===============-----------------
#=======================================================================

#Get some Inputs
parser = argparse.ArgumentParser()
parser.add_argument("-st", "--strain", help="Enter the spam directory you want to train on")
parser.add_argument("-ht", "--htrain", help="Enter the ham directory you want to train on")
parser.add_argument("-sd", "--spam_detect", help="Enter email that you would like to check the spam ranking of. Must be in PySpamFilter directory")
parser.add_argument("-ta", "--test_accuracy", nargs= 2, help="Enter spam first and then ham email-directory that you would like to check the spam ranking of. Must be in PySpamFilter directory")
parser.add_argument("-rw", "--rank_word", help="Rank this word more than others")
args = parser.parse_args()

#---------- If spam / ham is not inputed then send training_ham, spam--------
#Training HAM case
ham_dir = None
spam_dir = None

#Training SPAM case
if args.strain != None:
	#Check to see if directory is in directory
	if args.strain in os.listdir():
		print("Spam training commencing!")
		spam_dir = args.strain
	else:
		print("There is no folder '"+args.strain+"' in this directory.")
		exit()
else:
	spam_dir = "training_spam"

if args.htrain != None:
	#Check to see if directory is in directory
	if args.htrain in os.listdir():
		print("Ham training commencing!")
		ham_dir = args.htrain
	else:
		print("There is no folder '"+args.htrain+"' in this directory.")
		exit()
else:
	ham_dir = "training_ham"
#----------------------------------------------------------------------
training.train_spam_filter(spam_dir, ham_dir);


#Spam Detect case
if args.spam_detect != None:
	if(os.path.isfile(args.spam_detect)) is True:
		#Detect the spam of this email!!
		print("Good to go")
		spam_filter.spam_detect_email(args.spam_detect, "combined" , .0000000001 )
		exit()
	else:
		print("There is no email '"+args.spam_detect+"' in this directory.")

#Rank Word
if args.rank_word != None:
	print("The ranking of  '"+args.rank_word+"' is:")
	print(spam_filter.spam_rank(args.rank_word))
	exit()

#Detect accuracy of a directory case
if args.test_accuracy[1] != None:
	#Check if first (SPAM) and second (HAM) directorys are there
	if ((args.test_accuracy[0] in os.listdir()) & ((args.test_accuracy[1] in os.listdir()))):
		print("Folders are good")
		print("There is no directory '"+args.test_accuracy[0]+"' or '"+args.test_accuracy[1]+"' in this directory.")

		plot_mean = spam_filter.test_accuracy(args.test_accuracy[0], args.test_accuracy[1], "mean");
		plot_majority = spam_filter.test_accuracy(args.test_accuracy[0], args.test_accuracy[1], "majority");
		plot_combined = spam_filter.test_accuracy(args.test_accuracy[0], args.test_accuracy[1], "combined")

		spam_plots = [(plot_mean, "mean"), (plot_majority, "majority"), (plot_combined, "naive Bayes")];
		plot_detection_rates(spam_plots);

	else:
		print("There is no directory '"+args.test_accuracy[0]+"' or '"+args.test_accuracy[1]+"' in this directory.")
	exit()


# original



# for presentation!
# print("Analyzing file: ./test_spam/00001.317e78fa8ee2f54cd4890fdc09ba8176")
# print()
# file_object = open("./test_spam/00001.317e78fa8ee2f54cd4890fdc09ba8176", 'U', encoding='utf-8', errors='replace')
# spam_filter.spam_detect_email(file_object, "combined", 0.0000000001);

# test for presentation
# print(training.print_word_freq('hello'));
# print(training.print_word_freq('free'));
# print(training.print_word_freq('thanks'));
# print(training.print_word_freq('friend'));
# print(training.print_word_freq('click'));
# print(training.print_word_freq('nigeria'));
# print(training.print_word_freq('hey'));
# print(training.print_word_freq('sir'));
# print(training.print_word_freq('sales'));

# print(spam_filter.spam_rank('hello'));
# print(spam_filter.spam_rank('free'));
# print(spam_filter.spam_rank('thanks'));
# print(spam_filter.spam_rank('friend'));
# print(spam_filter.spam_rank('click'));
# print(spam_filter.spam_rank('nigeria'));
# print(spam_filter.spam_rank('hey'));
# print(spam_filter.spam_rank('sir'));
# print(spam_filter.spam_rank('sales'));