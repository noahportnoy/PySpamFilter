import matplotlib.pyplot as plt


# plot detection rate versus false positive rate
# make multiple plots like this ^ for different methods of determining spam/non-spam (averaging, median, etc.)
# todo: handle tuples?
def plot_detection_rates(plots):
	
	for spam_plot, method in plots:
		plt.plot(*zip(*spam_plot), label = method)

	plt.ylabel('detection rate')
	plt.xlabel('false positive rate')
	plt.title('Spam Filter Accuracy with Varying Threshold (Ignores Headers)')
	plt.legend()
	plt.show()