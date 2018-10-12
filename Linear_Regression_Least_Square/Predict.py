import numpy as np
import sys

# k is the number of attributes.
# n is the number of samples
# x is a matrix with all samples in attributes, with 1's in the first column
# y is a matrix which are the actual values of a given sample with attributes
# W are the weights of each attribute, with the first weight being the y-intercept
# test is a matrix with given attribute values to get predict_Value (y_hat).


def importTrain():
    file = open(sys.argv[1],"r")
    reader = file.read().splitlines()
    # k attributes
    k = int(reader[0])
    # n examples
    n = int(reader[1])
    # x matrix
    x = np.ones(shape=(n,k+1))
    # y matrix
    y = np.zeros(shape=(n,1))
    # Initialize x and y matrix to the correct numbers
    for i in range(2,n+2):
        row = i - 2
        column = 1
        splitter = reader[i].split(",")
        for j in splitter:
            if (column==k+1):
                y[row] = np.float64(j)
            else:
                x[row][column] = np.float64(j)
            column = column + 1
    return n,k,x,y

def importtest():
    file = open(sys.argv[2],"r")
    reader = file.read().splitlines()
    number_of_tests = int(reader[0])
    test = np.ones(shape=(number_of_tests,k+1))
    for i in range(1,number_of_tests+1):
        splitter = reader[i].split(",")
        row = i - 1
        column = 1
        for j in splitter:
            test[row][column] = np.float64(j)
            column = column+1
    return test, number_of_tests


if __name__ == "__main__":
    n,k,x,y = importTrain()
    # x transpose
    xtranspose = x.transpose()
    # x transpose * x
    xtransposeandx = xtranspose.dot(x)
    # inverse = (x transpose * x)^-1
    inverse = np.linalg.inv(xtransposeandx)
    # W = coefficients of the weights.
    W = (inverse.dot(xtranspose)).dot(y)
    test, number_of_tests = importtest()
    for i in range (0,number_of_tests):
        tempMatrix = test[i]
        prediced_Value = tempMatrix.dot(W)
        print("Predicted Value: " + str(prediced_Value[0]))
