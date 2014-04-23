
# build counts of word frequencies
def add_to_dictionary(word, dictionary):
	word = word.lower();
	if(word in dictionary):
	    dictionary[word] += 1;
	else:
	    dictionary[word] = 1;


def calculate_word_rank(word, good_count, bad_count):
	if(good_count + bad_count > 5):
		temp = min(1, bad_count/nbad) / (min(1, good_count/ngood) + min(1, bad_count/nbad));
		temp2 = min(0.99, temp);
		rank = max(0.01, temp2);

		return rank;


def spam_rank(word):
	if(word in rank_dict):
		return rank_dict[word];
	else:
		return 0.4;

def find_most_interesting_word(mail_dict):
	interesting_value = 0.5;
	interesting_word = '';

	for word, value in mail_dict.items():
		if (abs(value - 0.5) >= abs(interesting_value - 0.5)):
			interesting_value = value;
			interesting_word = word;

	return (interesting_word, interesting_value);


def calculate_mail_spam_prob(email):
	
	# mail_dict = {'hello': 0.8, 'andrew': 0.2, 'sign': 0.95, 'up': 0.6, 'for': 0.3, 'free': 0.99, 'access': 0.99, 'to': 0.4, 'the': 0.4, 'world\'s': 0.81, 'best': 0.85, 'parties': 0.94, 'around': 0.2, 'globe': 0.78, 'do': 0.1, 'you': 0.31, 'think': 0.01, 'have': 0.35, 'what': 0.06, 'it': 0.4, 'takes': 0.89};
	mail_dict = {};
	interesting_dict = {};
	spam_prob_threshold = 0.8;

	# create mail_dict as a set of words in the email and their corresponding spam rankings
	for word in email:
		if(word not in mail_dict):
			mail_dict[word] = spam_rank(word);

	# create interesting_dict as a set of the 15 most interesting words from the email
	# and their corresponding spam rankings
	while(len(interesting_dict) < 15):
		interesting_word, interesting_value = find_most_interesting_word(mail_dict);
		del mail_dict[interesting_word];

		interesting_dict[interesting_word] = interesting_value;

		# if the email has no more words to draw from (ie. it had less than 15 to begin with), break
		if(len(mail_dict) == 0):
			break;

	# print(interesting_dict.items());

	# average of 15 most interesting word rankings
	prob = sum(interesting_dict.values())/len(interesting_dict);

	return prob;


# main

bad_dict = {'a': 1, 'b': 2, 'c': 3, 'g': 4};
good_dict = {'a': 1, 'b': 2, 'd': 7, 'e': 25};
full_dict = {};
rank_dict = {};

# for each word in bad emails #
bad_words = ['Bad', 'bad', 'stupid', 'stupid', 'idiot', 'free', 'bad', 'crap', 'junk', 'spam', 'free', 'bad', 'stupid', 'stupid', 'bad', 'bad', 'bad', 'spam', 'spam', 'stupid', 'idiot', 'andrew', 'andrew'];
for word in bad_words:
	add_to_dictionary(word, bad_dict);
	add_to_dictionary(word, full_dict);

# for each word in good emails #
good_words = ['hello', 'hello', 'friend', 'friend', 'andrew', 'how', 'hello', 'how', 'are', 'you', 'andrew', 'hello', 'friend', 'friend', 'hello', 'hello', 'hello', 'are', 'are', 'friend', 'how', 'andrew', 'andrew'];
for word in good_words:
	add_to_dictionary(word, good_dict);
	add_to_dictionary(word, full_dict);

nbad = len(bad_dict);   # change to number of emails in spam corpus
ngood = len(good_dict); # change to number of emails in non-spam corpus

print('number of bad words is', nbad);
print('number of good words is', ngood);
print();

for word in full_dict:
	if(word in good_dict):
		good_count = 2 * good_dict[word];
	else:
		good_count = 0;

	if(word in bad_dict):
		bad_count = bad_dict[word];
	else:
		bad_count = 0;

	# print(word, ': good count is', good_count, ', bad count is', bad_count);
	rank_dict[word] = calculate_word_rank(word, good_count, bad_count);


print();

for word in rank_dict:
	print(word, 'has rank', rank_dict[word]);

