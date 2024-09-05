import pandas as pd
from sklearn.model_selection import train_test_split

"""
    ASSIGNMENT 2 (STUDENT VERSION):
    Using pandas to explore Titanic data from Kaggle (titanic.csv) and answer the questions.
"""


def Q1(df):
    """
        Problem 1:
            How many rows are there in the “titanic.csv?
            Hint: In this function, you must load your data into memory before executing any operations. To access titanic.csv, use the path /data/titanic.csv.
            * TA's announcement: use Q1(df) instead of Q1()
    """
    # TODO: Code here
    return df.shape[0]


def Q2(df):
    '''
        Problem 2:
            Drop unqualified variables
            Drop variables with missing > 50%
            Drop categorical variables with flat values > 70% (variables with the same value in the same column)
            How many columns do we have left?
    '''
    # TODO: Code here
    df2 = df.dropna(thresh=len(df)/2, axis=1)
    df2 = df2.drop(["PassengerId"], axis=1)
    return df2.shape[1]


def Q3(df):
    '''
       Problem 3:
            Remove all rows with missing targets (the variable "Survived")
            How many rows do we have left?
    '''
    # TODO: Code here
    df3 = df.dropna(subset=["Survived"])
    return df3.shape[0]


def Q4(df):
    '''
       Problem 4:
            Handle outliers
            For the variable “Fare”, replace outlier values with the boundary values
            If value < (Q1 - 1.5IQR), replace with (Q1 - 1.5IQR)
            If value > (Q3 + 1.5IQR), replace with (Q3 + 1.5IQR)
            What is the mean of “Fare” after replacing the outliers (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here
    q1, q3 = df["Fare"].quantile([0.25, 0.75])
    iqr = q3 - q1
    min = q1 - 1.5*iqr
    max = q3 + 1.5*iqr

    # Conditional that returns a boolean Series with column labels specified
    df.loc[df["Fare"] < min, "Fare"] = min
    df.loc[df["Fare"] > max, "Fare"] = max

    return round(df["Fare"].mean(),2)


def Q5(df):
    '''
       Problem 5:
            Impute missing value
            For number type column, impute missing values with mean
            What is the average (mean) of “Age” after imputing the missing values (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here
    # numeric
    df = df.fillna(df.mean(numeric_only=True))

    # categorical
    df = df.fillna(df.mode().iloc[0])
    return round(df["Age"].mean(),2)


def Q6(df):
    '''
        Problem 6:
            Convert categorical to numeric values
            For the variable “Embarked”, perform the dummy coding.
            What is the average (mean) of “Embarked_Q” after performing dummy coding (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    # TODO: Code here
    df_dummy = pd.get_dummies(df[["Embarked"]], drop_first=False)
    df_with_dummy = pd.concat([df, df_dummy], axis=1)
    return round(df_with_dummy["Embarked_Q"].mean(),2)


def Q7(df):
    '''
        Problem 7:
            Split train/test split with stratification using 70%:30% and random seed with 123
            Show a proportion between survived (1) and died (0) in all data sets (total data, train, test)
            What is the proportion of survivors (survived = 1) in the training data (round 2 decimal points)?
            Hint: Use function round(_, 2), and train_test_split() from sklearn.model_selection
    '''
    # TODO: Code here
    y = df["Survived"]
    X = df.drop(["Survived"], axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.3, random_state=123)
    return round(y_train.value_counts()[1] / y_train.value_counts().sum(), 2)
