import file_handler

bad_dict = {}
good_dict = {}
full_dict = {}
rank_dict = {}

def get_rank_dict():
	return rank_dict

def print_word_freq(word):
	word = word.lower()

	if(word in bad_dict):
		print(word, " appears", bad_dict[word], "times in bad_dict")
	else:
		print(word, " appears 0 times in bad_dict")

	if(word in good_dict):
		print(word, " appears", good_dict[word], "times in good_dict")
	else:
		print(word, " appears 0 times in good_dict")

# build counts of word frequencies for training
def add_to_dictionary(word, dictionary):
	word = word.lower()

	if(word in dictionary):
	    dictionary[word] += 1
	else:
	    dictionary[word] = 1

# calculate the rank of a word for training
def calculate_word_rank(good_count, bad_count):
	ngood = file_handler.getHamEmailCount()
	nbad = file_handler.getSpamEmailCount()
	if(good_count + bad_count > 5):
		temp = min(1, bad_count/nbad) / (min(1, good_count/ngood) + min(1, bad_count/nbad))
		temp2 = min(0.99, temp)
		rank = max(0.01, temp2)

		return rank

def build_dictionaries(spam_dir, ham_dir):
	bad_words = file_handler.parseTrainingDirectory(spam_dir)
	print("Training on spam words...")
	for word in bad_words:
		add_to_dictionary(word, bad_dict)
		add_to_dictionary(word, full_dict)

	good_words = file_handler.parseTrainingDirectory(ham_dir)
	print("Training on ham words...")
	for word in good_words:
		add_to_dictionary(word, good_dict)
		add_to_dictionary(word, full_dict)

# takes all words from spam and non-spam training emails, and puts their spam
# rankings in rank_dict, returns rank_dict
def train_spam_filter(spam_dir, ham_dir):

	if(len(rank_dict) > 0):
		print("WARNING: attempting to train spam filter when some word rankings have already been calculated")

	build_dictionaries(spam_dir, ham_dir)

	for word in full_dict:
		if(word in good_dict):
			good_count = 2 * good_dict[word]
		else:
			good_count = 0

		if(word in bad_dict):
			bad_count = bad_dict[word]
		else:
			bad_count = 0

		rank_dict[word] = calculate_word_rank(good_count, bad_count)
