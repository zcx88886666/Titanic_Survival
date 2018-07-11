import numpy as np
import pandas as pd

# acquire data from files
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
combine = [train_df, test_df]

print(train_df.columns.values)
print(train_df.head())
print(train_df.tail())
print(train_df.info())
print('_' * 40)
print(test_df.info())
print(train_df.describe())
train_df.describe(include=['0'])
train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index = False).mean().sort_values(by='Survived', ascending=False)