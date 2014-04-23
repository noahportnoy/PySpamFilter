import matplotlib.pyplot as plt
import os
import training
import spam_filter
import file_handler


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


#main
training.train_spam_filter("training_spam", "training_ham");
# original
plot_mean = spam_filter.test_accuracy("test_spam", "test_ham", "mean");
plot_majority = spam_filter.test_accuracy("test_spam", "test_ham", "majority");
plot_combined = spam_filter.test_accuracy("test_spam", "test_ham", "combined")

spam_plots = [(plot_mean, "mean"), (plot_majority, "majority"), (plot_combined, "naive Bayes")];
plot_detection_rates(spam_plots);


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