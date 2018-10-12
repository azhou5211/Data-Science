This is a very basic implementation of prediction.

Notes:
Predict.py takes in a train.txt and test.txt file to predict values.
This is not for time series.
This program does not take categorical variables. It can only take numerical variables.
This program has a major flaw, in which it does not detect whether the prediction is good or not. Neither F-test for the regression nor T-tests for each independent variable has been computed in the following program. Meaning the Regression Model may not be significant and not all the attributes may be significant for predicting. Also the Regression conditions are not checked. Therefore, this program may not provide accurate predictions. 

You can run the program by:
python3 Predict.py <trainfile.txt> <testfile.txt>

An example would be:
python3 Predict.py trainA.txt testB.txt

Training File Structure:
The first line in the training file will be an integer that gives the number of independent variables (k).
The second line in the training file will be an integer that gives the number of samples (n).
Each line after contains (k+1) double precision floating point numbers seperated by commas. The first k values are dependent variables of that sample, while the last k value will be the actual value (independent variable) of that sample.

Test File Structure:
The first line in the test file will be an integer containing the number cases that you want to predict.
Each line after contains k double precision floating numbers that are seperated by commas, and they represent each independent variable for that test case.


Predict.py will print out the predicted values for each test case in the terminal.
