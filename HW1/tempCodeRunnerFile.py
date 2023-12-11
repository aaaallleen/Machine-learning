ones = np.ones(len(training_dataX))
X = np.c_[ones, training_dataX]
theta, cost_list = Regression(X, training_dataY, 0.0000005, 100000)
predictprice(theta)