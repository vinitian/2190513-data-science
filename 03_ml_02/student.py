import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
import numpy as np
import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

class BankLogistic:
    def __init__(self, data_path): # DO NOT modify this line
        self.data_path = data_path
        self.df = pd.read_csv(data_path, sep=',')

    def Q1(self): # DO NOT modify this line
        """
        Problem 1:
        Load 'bank-st.csv' data from the “Attachment”
        How many rows of data are there in total?
        """
        # TODO: Paste your code here
        return self.df.shape[0]

    def Q2(self): # DO NOT modify this line
        """
        Problem 2:
        How many numeric variables are there ?
        """
        # TODO: Paste your code here
        return self.df.select_dtypes(exclude="object").columns.values.shape[0]

    def Q3(self): # DO NOT modify this line
        """
        Problem 3:
        How many categorical variables are there?
        """
        # TODO: Paste your code here
        return self.df.select_dtypes(include="object").columns.values.shape[0]

    def Q4(self): # DO NOT modify this line
        """
        Problem 4:
        What is the distribution of the target variable for the 'NO' class?
        """
        # TODO: Paste your code here
        return self.df[self.df['y'] == 'no'].shape[0]/self.df.shape[0]

    def Q5(self): # DO NOT modify this line
        """
        Problem 5:
        Drop duplication of the data
        What are the shapes of the data?
        """
        # TODO: Paste your code here
        self.df = self.df.drop_duplicates()
        return self.df.shape

    def Q6(self):
        """
        Problem 6:
        How many null values are there in the job and education columns?
        For numeric variables, fill missing values with the mean, and for
        categorical variables, fill missing values with the mode.
        Hint: replace unknown with null
        """
        # TODO: Paste your code here
        self.Q5()
        self.df = self.df.replace('unknown', pd.NA)

        null_job = self.df[self.df['job'].isna()].shape[0]
        null_education = self.df[self.df['education'].isna()].shape[0]

        self.df = self.df.fillna(self.df.mean(numeric_only=True))
        self.df = self.df.fillna(self.df.mode().iloc[0])
        return (null_job, null_education)
    
    def Q7(self):
        """
        Problem 7:
        Split train/test for 70%:30% with random_state=0 & stratify option
        What are the shapes of X_train and X_test?
        Hint: Don't forget to encode categorical data using pd.get_dummies before
        splitting the data.
        """
        # TODO: Paste your code here
        self.Q6()
        
        to_dummy = self.df.select_dtypes(include="object")
        df_dummy = pd.get_dummies(to_dummy, drop_first=True)
        self.df = self.df.drop(columns=to_dummy)
        df_with_dummy = pd.concat([self.df, df_dummy], axis=1)

        y = df_with_dummy.y_yes
        X = df_with_dummy.drop(columns=['y_yes'])

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=0)
        return (self.X_train.shape, self.X_test.shape)

    def Q8(self):
        """
        Problem 8:
        How much data does the test set contain for the class 'No'?
        """
        # TODO: Paste your code here
        self.Q7()
        return self.y_test.value_counts()[False]
    
    def Q9(self):
        """
        Problem 9:
        Set the model to be used as Logistic Regression only with random_state=0
        and max_iter=5000
        Build a model that uses all variables.
        What is the macro F1 score for Model on the test data? (Answer with two
        decimal places).
        """
        # TODO: Paste your code here
        self.Q7()

        logis = LogisticRegression(random_state=0, max_iter=5000)
        logis.fit(self.X_train, self.y_train)
        prediction = logis.predict(self.X_test)
        macro_f1 = f1_score(self.y_test, prediction, average='macro')
        return round(macro_f1,2)
    
#**Copy and paste your libraries, class Clustering with modified functions when
#submitting to the grader. (don’t submit the code below)**

def main(): # DO NOT modify this line
    hw = BankLogistic('/bank-st.csv') #your file path
    exec(input().strip())

    # hw = BankLogistic('03_ml_02/bank-st.csv')
    # print(hw.Q9())

if __name__ == "__main__": # DO NOT modify this line
    main()
#Note: When testing your code, copy command from each example.