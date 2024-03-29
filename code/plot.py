import matplotlib.pyplot as plt


# plot detection rate versus false positive rate for different spam classification methods
# (majority, mean average, naive Bayes)
def plot_detection_rates(plots):
	
	for spam_plot, method in plots:
		plt.plot(*zip(*spam_plot), label = method)

	plt.ylabel('detection rate')
	plt.xlabel('false positive rate')
	plt.title('Spam Filter Accuracy with Varying Threshold (Considers Headers)')
	plt.legend()
	plt.show()