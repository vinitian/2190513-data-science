import pandas as pd
import json

# note: please download the dataset from here
# https://github.com/kaopanboonyuen/2110446_DataScience_2021s2/raw/main/datasets/data.tgz
# or
# https://www.kaggle.com/datasets/datasnaek/youtube-new

"""
    ASSIGNMENT 1 (STUDENT VERSION):
    Using pandas to explore youtube trending data from GB (GBvideos.csv and GB_category_id.json) and answer the questions.
"""

def Q1():
    """
        1. How many rows are there in the GBvideos.csv after removing duplications?
        - To access 'GBvideos.csv', use the path '/data/GBvideos.csv'.
    """
    # TODO: Paste your code here
    # vdo_df = pd.read_csv('for_01_pandas_02/USvideos.csv')
    vdo_df = pd.read_csv('/data/GBvideos.csv')
    return vdo_df.drop_duplicates().shape[0]

def Q2(vdo_df):
    '''
        2. How many VDO that have "dislikes" more than "likes"? Make sure that you count only unique title!
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''
    # TODO: Paste your code here
    return vdo_df[vdo_df['likes'] < vdo_df['dislikes']]['title'].nunique()


def Q3(vdo_df):
    '''
        3. How many VDO that are trending on 22 Jan 2018 with comments more than 10,000 comments?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - The trending date of vdo_df is represented as 'YY.DD.MM'. For example, January 22, 2018, is represented as '18.22.01'.
    '''
    # TODO: Paste your code here
    return vdo_df[(vdo_df['trending_date'] == '18.22.01') & (vdo_df['comment_count'] > 10000)]['video_id'].nunique()

def Q4(vdo_df):
    '''
        4. Which trending date that has the minimum average number of comments per VDO?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''
    # TODO:  Paste your code here
    vdo_df_groupby_trending_date = vdo_df.groupby('trending_date')
    vdo_df2 = vdo_df_groupby_trending_date.comment_count.sum()
    return vdo_df2[vdo_df2 == vdo_df2.min()].index[0]

def Q5(vdo_df):
    '''
        5. Compare "Sports" and "Comedy", how many days that there are more total daily views of VDO in "Sports" category than in "Comedy" category?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - You must load the additional data from 'GB_category_id.json' into memory before executing any operations.
            - To access 'GB_category_id.json', use the path '/data/GB_category_id.json'.
    '''
    # TODO:  Paste your code here
    
    # convert json to df
    with open('/data/GB_category_id.json') as fd:
    # with open('for_01_pandas_02/US_category_id.json') as fd:
        cat = json.load(fd)
    cat_list = []
    for d in cat['items']:
        cat_list.append((int(d['id']), d['snippet']['title']))

    cat_df = pd.DataFrame(cat_list, columns=['id', 'category'])

    vdo_df_withcat = vdo_df.merge(cat_df, left_on='category_id', right_on='id')
    vdo_df_sports_comedy = vdo_df_withcat[(vdo_df_withcat['category'] == 'Comedy') | (vdo_df_withcat['category'] == 'Sports')]
    vdo_df_pivot = vdo_df_sports_comedy.pivot_table(index=['trending_date'], columns=['category'], values=['views'], aggfunc='sum',fill_value=0)
    return vdo_df_pivot[vdo_df_pivot['views','Comedy'] < vdo_df_pivot['views', 'Sports']].shape[0]


vdo_df = pd.read_csv('for_01_pandas_02/USvideos.csv') 
# vdo_df = pd.read_csv('/data/GBvideos.csv')

# print(vdo_df)
print(Q5(vdo_df))

# query = input()
# if query == 'Q1':
#     # print(Q1(vdo_df))
#     print(vdo_df.drop_duplicates(inplace=True))
# elif query == 'Q2':
#     print(Q2(vdo_df))
# elif query == 'Q3':
#     print(Q3(vdo_df))
# elif query == 'Q4':
#     print(Q4(vdo_df))
# elif query == 'Q5':
#     print(Q5(vdo_df))