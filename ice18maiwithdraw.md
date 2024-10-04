# Q1 -- online course csv
1. self.df.shape[0]
2. 
3.
4.
5.
6.
7. 





# Q2
1. shape[0] already done

2. drop AmountSpent is negative, and select only Age>18 or age is null -> ask for # of remaining rows
    ```python
    df = df.drop(df[df.AmountSpent < 0].index)
    df = df[(df["Age"] >= 18) | df["Age"].isnull() ]
    return df.shape[0]
    ```
    [source](https://stackoverflow.com/questions/13851535/how-to-delete-rows-from-a-pandas-dataframe-based-on-a-conditional-expression)

3. convert m,M,male to Male and f,F,female to Female -> self.df[self.df["Age"] >= 18]
    ```python
    mapper = {
        'm':'Male',
        'M':'Male',
        'male':'Male',
        'f':'Female',
        'F':'Female',
        'female':'Female'
    }
    self.df['Gender'].replace(mapper, inplace=True)

    return ???????
    ```

4. Q1, Q99, less than Q1 convert to Q1, more than Q99 convert to Q99 -> mean()
    ```python
    q1 = self.df[“Salary”].quantile(0.01)
    q99 = self.df[“Salary”].quantile(0.99)
    
    self.df.loc[self.df["Salary"] < q1, "Salary"] = q1
    self.df.loc[self.df["Salary"] > q99, "Salary"] = q99

    return self.df[“Salary”].mean() #not sure about return

    ```
5. impute null age with mean, null gender with mode, ask for self.df[self.df["Age"] >= self.df["Age"].mean()].shape[0] + self.df[self.df["Gender"] >= "Female"].shape[0]
    ```python
    self.df['Age'] = self.df['Age'].fillna(self.df.mean(numeric_only=True))
    self.df['Gender'] = self.df['Gender'].fillna(self.df.mode.iloc[0])

    return self.df[self.df["Age"] >= self.df["Age"].mean()].shape[0] + self.df[self.df["Gender"] >= "Female"].shape[0]
    ```
    [source](https://www.statology.org/pandas-fillna-specific-column/)

6. make dummy noydes for OwnedHouse, Marriage, History, use drop_first=True, then drop the original cols and concat the dummies with self.df. finally, return number of cols of the final df.
    ```python
    dummy = pd.get_dummies(self.df, columns=['OwnedHouse','Marriage','History'], drop_first=True)
    self.df.drop(['OwnedHouse','Marriage','History'], axis=1, inplace=True)
    df_with_dummy = pd.concat([self.df, dummy], axis=1)

    return df_with_dummy.shape[1]
    ```
    [source](https://www.statology.org/pandas-get-dummies/)

7. stratify by AmountSpentBin
    - what is the ratio of y_test(sth)  to y_test.shape[0] ?
    ```python
    from sklearn.model_selection import train_test_split
    y = self.df.pop("AmountSpentBin")
    X = self.df
    X_train, X_test, y_train, y_test = train_test_split(stratify=y, test_size=0.3,random_state=2190513)
    
    return round((y_test something) / y_test.shape[0],2) #pls edit return
    ```



# Q3 - must import yourself
0. things to import:
    ```python
    from sklearn.tree import DecisionTreeRegressor
    from sklearn import metrics
    import pandas as pd
    import numpy as np
    ```

1. DecisionTreeRegression  round(predictions[75],4)
    ```python
    dtree = DecisionTreeRegressor(max_depth=7, min_leaf_nodes=4, random_state=2024) #not sure about the numbers but that's pretty much it
    dtree.fit(self.X_train, self.y_train)
    predictions = dtree.predict(X_test)

    return round(predictions[75],4)
    ```

2. RMSE
    ```python
    dtree = DecisionTreeRegressor(max_depth=7, min_leaf_nodes=4, random_state=2024) #not sure about the numbers
    dtree.fit(self.X_train, self.y_train)
    predictions = dtree.predict(X_test)

    return round(np.sqrt(metrics.mean_squared_error(y_test, predictions)),2) #be careful, squared has 'd' in it
    ```

3. what is the most important feature? (ans is Salary)
    ```python
    dtree = DecisionTreeRegressor(max_depth=7, min_leaf_nodes=4, random_state=2024) #not sure about the numbers
    dtree.fit(self.X_train, self.y_train)
    predictions = dtree.predict(X_test)
    important = dtree.feature__importances_.argmax() #argmax() returns position of max

    return self.X_train.columns.index(important)
    ```
    [np.argmax](https://numpy.org/doc/stable/reference/generated/numpy.argmax.html)

4. log transform y then DecisionTreeRegression  round(predictions[75],4)
    ```python
    y_train_log = np.log(self.y_train)
    y_test_log = np.log(self.y_test)
    dtree = DecisionTreeRegressor(max_depth=7, min_leaf_nodes=4, random_state=2024) #not sure about the numbers
    dtree.fit(self.X_train, y_train_log)
    predictions = dtree.predict(X_test)

    return round(np.power(np.e, np.log(predictions[75])),4) #from e^(ln(x)) = x, np.log() is by default ln()
    ```

5. RMSE from Q3.3 
    ```python
    y_train_log = np.log(self.y_train)
    y_test_log = np.log(self.y_test)
    dtree = DecisionTreeRegressor(max_depth=7, min_leaf_nodes=4, random_state=2024) #not sure about the numbers
    dtree.fit(self.X_train, y_train_log)
    predictions = dtree.predict(X_test)
    predictions_tonormal = np.power(np.e, np.log(predictions))

    return round(np.sqrt(metrics.mean_squared_error(y_test, predictions_tonormal)),2)
    ```


keggle Directed Marketing


YOUFORM
1. which is correct?
A. edX has the most courses and course completion (or sth)
B.