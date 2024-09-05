import pandas as pd
import numpy as np

def main():
    # df = pd.read_csv("/home/iannnn/Documents/Y2T1/data science/grader/for_01_pandas_01/scores_student.csv")
    df = pd.read_csv(input())
    q = input()

    if q == "Q1":
        print(df.shape)
    elif q == "Q2":
        print(df['score'].max())
    elif q == "Q3":
        print(df[ df['score'] >= 80 ]['id'].nunique())
    else:
        print("No Output")

if __name__ == "__main__":
    main()