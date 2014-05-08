import file_handler
import numpy as np
import training
import os

# returns the spam ranking of a word
def spam_rank(word):
	word = word.lower()
	rank_dict = training.get_rank_dict()

	if word in rank_dict:
		return rank_dict[word]
	else:
		return 0.4

# finds the most interesting word in a given dictionary of words and their spam rankings
def find_most_interesting_word(mail_dict):
	interesting_value = 0.5
	interesting_word = ''

	for word, value in mail_dict.items():
		if abs(value - 0.5) >= abs(interesting_value - 0.5):
			interesting_value = value
			interesting_word = word

	return (interesting_word, interesting_value)

def spam_detect_email_file(filename, method, threshold, verbose):
	
	email = open(filename, 'U', encoding='utf-8', errors='replace')

	rank_dict = training.get_rank_dict()
	# print("Length of rank_dict is", len(rank_dict))

	# mail_dict = {'hello': 0.8, 'andrew': 0.2, 'sign': 0.95, 'up': 0.6, 'for': 0.3, 'free': 0.99, 'access': 0.99, 'to': 0.4, 'the': 0.4, 'world\'s': 0.81, 'best': 0.85, 'parties': 0.94, 'around': 0.2, 'globe': 0.78, 'do': 0.1, 'you': 0.31, 'think': 0.01, 'have': 0.35, 'what': 0.06, 'it': 0.4, 'takes': 0.89}
	mail_dict = {}
	interesting_dict = {}
	spam_prob_threshold = threshold
	num_of_words_to_grab = 15

	# create mail_dict as a set of words in the email and their corresponding spam rankings
	email_words = file_handler.parseEmail(email)

	for word in email_words:
		if word not in mail_dict:
			if(spam_rank(word) != None):
				mail_dict[word] = spam_rank(word)
			else:
				mail_dict[word] = 0.4

	# create interesting_dict as a set of the most interesting words from the email
	# and their corresponding spam rankings
	while(len(interesting_dict) <= num_of_words_to_grab):
		interesting_word, interesting_value = find_most_interesting_word(mail_dict)

		# if the email has no more words to draw from, break
		if len(mail_dict) == 0:
			break
		else:
			del mail_dict[interesting_word]
			interesting_dict[interesting_word] = interesting_value
			
			if verbose == True:
				print(interesting_word, ": ", interesting_value)

	if method == "mean":
		# average of most interesting word rankings
		prob = sum(interesting_dict.values())/len(interesting_dict)
		if (prob >= threshold):
			return 1
		else:
			return 0

	elif method == "majority":
		count_words_above_threshold = 0
		# count the number of words in the interesting dictionary which
		# have values greater than the threshold
		for word, value in interesting_dict.items():
			if( value >= threshold ):
				count_words_above_threshold += 1

		# if there are more words above the threshold than below, mark
		# the email as spam
		if(count_words_above_threshold/len(interesting_dict) > 0.5):
			return 1
		# otherwise, mark the email as non-spam
		else:
			return 0

	elif method == "combined":
		prob_product = 1
		one_minus_prob_product = 1

		for word, value in interesting_dict.items():
			prob_product *= value
			one_minus_prob_product *= (1 - value)

		prob = prob_product/(prob_product + one_minus_prob_product)

		if verbose == True:
			print()
			if ( prob >= threshold):
				print("This message is spam with probability", prob)
				return 1
			else:
				print("This message is not spam with probability", 1-prob)
				return 0
	else:
		print("Invalid method", method, "used for test_accuracy")
		exit()

	return 0


# returns whether an email is spam (1 for spam, 0 for non-spam)
# returns whether an email is spam (1 for spam, 0 for non-spam)
def spam_detect_email(email, method, threshold):
	
	rank_dict = training.get_rank_dict()

	mail_dict = {}
	interesting_dict = {}
	spam_prob_threshold = threshold
	num_of_words_to_grab = 15

	# create mail_dict as a set of words in the email and their corresponding spam rankings
	email_words = file_handler.parseEmail(email)

	for word in email_words:
		if word not in mail_dict:
			if spam_rank(word) != None:
				mail_dict[word] = spam_rank(word)
			else:
				mail_dict[word] = 0.4

	# create interesting_dict as a set of the most interesting words from the email
	# and their corresponding spam rankings
	while(len(interesting_dict) <= num_of_words_to_grab):
		interesting_word, interesting_value = find_most_interesting_word(mail_dict)

		# if the email has no more words to draw from, break
		if len(mail_dict) == 0:
			break
		else:
			del mail_dict[interesting_word]
			interesting_dict[interesting_word] = interesting_value
			# print(interesting_word, ": ", interesting_value)

	if method == "mean":
		# average of most interesting word rankings
		prob = sum(interesting_dict.values())/len(interesting_dict)
		if (prob >= threshold):
			return 1
		else:
			return 0

	elif method == "majority":
		count_words_above_threshold = 0
		# count the number of words in the interesting dictionary which
		# have values greater than the threshold
		for word, value in interesting_dict.items():
			if( value >= threshold ):
				count_words_above_threshold += 1

		# if there are more words above the threshold than below, mark
		# the email as spam
		if count_words_above_threshold/len(interesting_dict) > 0.5:
			return 1
		# otherwise, mark the email as non-spam
		else:
			return 0

	elif method == "combined":
		prob_product = 1
		one_minus_prob_product = 1

		for word, value in interesting_dict.items():
			prob_product *= value
			one_minus_prob_product *= (1 - value)

		prob = prob_product/(prob_product + one_minus_prob_product)
		# print(prob)

		if prob >= threshold:
			return 1
		else:
			return 0

def test_accuracy(test_spam_dir, test_ham_dir, method):

	# a list of tuples, where each tuple is the detection rate and false_positive rate
	# for a given threshold
	filter_results = []
	true_positives = 0
	false_positives = 0
	count_total_spam = 0
	count_total_ham = 0
	print("Testing accuracy with the", method, "method")

	if method == "combined":
		thresh_range = np.arange(0.0000000000000000001,0.24,0.02)
	else:
		thresh_range = np.arange(0.01,0.99,0.08)

	for threshold in thresh_range:
		# find detection rate for spam
		print("threshold is", threshold)

		file_list = file_handler.findFiles("./" + test_spam_dir)
		for item in file_list:
			filename = test_spam_dir + "/" + item
			# print(filename)
			file_object = open(filename, 'U', encoding='utf-8', errors='replace')
			true_positives += spam_detect_email(file_object, method, threshold)
			count_total_spam += 1
		true_positive_rate = true_positives / count_total_spam
		
		# find false positive rate for ham
		file_list = file_handler.findFiles("./" + test_ham_dir)
		for item in file_list:
			filename = test_ham_dir + "/" + item
			file_object = open(filename, 'U', encoding='utf-8', errors='replace')
			false_positives += spam_detect_email(file_object, method, threshold)
			count_total_ham += 1
		false_positive_rate = false_positives / count_total_ham

		# add true positive and false positive rates to plot array
		# (for the given threshold value)
		filter_results.append((false_positive_rate, true_positive_rate))
	
	return filter_results

