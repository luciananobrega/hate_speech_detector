import pandas as pd
from processing_text import *

### === PART I: IMPORTING AND EDITING THE DATASETS
twitter_dataset = pd.read_csv('data\\B2Share_eudat\\twitter_dataset.csv')
# dropping all NA values, we'll delete those tweets that are not available anymore.
# as we can't check the content, I prefered to drop them.
twitter_dataset = twitter_dataset.dropna()

twitter_dataset = twitter_dataset[['data', 'Hate.speech']]

g1_dataset = pd.read_csv('data\\OffComBR-master\\OffComBR3.csv')
cols = g1_dataset.columns.tolist()
cols = cols[::-1] #reverting cols
g1_dataset = g1_dataset[cols]
g1_dataset['class'] = g1_dataset['class'].map({'yes': 1, 'no': 0})
g1_dataset.columns = ['data', 'Hate.speech']

frames = [twitter_dataset, g1_dataset] 
full_dataset =  pd.concat(frames, ignore_index=True)

### === PART II: DATA ENRICHMENT

from tqdm import tqdm, tqdm_notebook
#tqdm.pandas(tqdm_notebook)

data = full_dataset['data'].apply(process_text)
"""
data = data.apply(remove_punctuation)

length = data.apply(len)
laughs = data.apply(count_laughs)

data = data.apply(remove_laughs)


data = data.apply(remove_links)


data = data.apply(remove_duplicated_letters)

data = data.apply(remove_stopwords)

data = data.apply(stemming)

data = data.apply(bag_of_words)
"""
