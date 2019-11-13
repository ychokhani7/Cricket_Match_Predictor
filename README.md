# Cricket_Match_Predictor
# Analytics and Predictive-modeling for IPL(Premier League) cricket matches
### Programming Language: Python 3.6
### IDE: Jupyter Notebook(Azure Big Data)
### input: CSV file
### Output: Predictive Model of Machine learning using scikit learn module, statistical data analytics with graphs using Numpy,Matplotlib

Kaggle IPL matches.csv in ..\library\matches.csv is used for analysis and generating a predictive model. The data analytics is performed to compare features that influences the outcomes of matches(win/lose). The features that are considered are 'city','toss_decision','toss_winner' and 'venue'. A predictive model is developed using Machine Learning algorithm to get highest possible accuracy. Then feature importance retrieved from predictive model applied reveals the importance of features in determining match outcomes(win/lose).These feature importance is then compared against actual data to check for validity. Two models were built - Random Forest Classifier and Logistic Regression. RandomForestClassifier gave the best accuracy of 89%. 
