#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:11:29 2023

@author: blucie
"""

# Import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data.csv', encoding="ISO-8859-1")

###############################################################################
############################## General questions ##############################
###############################################################################

## How many columns and rows are there in the data?
columns = len(data.columns)
rows = len(data.index)
print ('There are', columns, 'colums in the data.')
print ('There are', rows, 'rows in the data.')

# -----------------------------------------------------------------------------

## How many unique recipients of a Nobel prize are listed?
### hint: you can use the groupby function
# first: print (data.columns) to see how columns are named
names = data ['firstname' and 'surname'].unique ()
unique = len (names)
print ('There are', unique, 'unique recipients in the data.')

# -----------------------------------------------------------------------------

## How many categories of prizes are part of the data?
# first: print (data.columns) to see how columns are named
categories = data ['category'].unique ()
sum_categories = len (categories)
print('There are ', sum_categories ,'categories of prizes in the data.')

# -----------------------------------------------------------------------------

## Give the name of the person who was the youngest when they received their Nobel prize.
data ['year - bornYear'] = data['year'] - data['bornYear']
minimal_age = data ['year - bornYear'].min ()
for i in range(len(data['year - bornYear'])):
    if minimal_age in data['year - bornYear']:
        row_youngest_recipient = i
firstname = data.iloc (i, 3)
surname = data.iloc (i, 4)
print('The youngest recipient was', firstname, surname)

## Same question for the oldest recipient.

#--Enter your code here--#

#print('The oldest recipient was', XXX)

# -----------------------------------------------------------------------------

## Look at the column 'share'. It states with how many other recipients the prize was shared. Do you notice something about those values?

#--Enter your code here--#

###############################################################################
################################ Visualisation ################################
###############################################################################

## Create a barplot with the number of prizes per category.

#--Enter your code here--#

## Save your figure as "counts_category.png" in the output folder.

#--Enter your code here--#

# -----------------------------------------------------------------------------

## Plot the age distribution.

#--Enter your code here--#

## Save your figure as "age_distribution.png" in the output folder.

#--Enter your code here--#

# -----------------------------------------------------------------------------

## Plot the age distribution by sex.

#--Enter your code here--#

## Save your figure as "age_distribution_sex.png" in the output folder.

#--Enter your code here--#


###############################################################################
################################ Missing data #################################
###############################################################################

## How many missing values are present in the column 'died'?
data.isna('died').sum()
#--Enter your code here--#

#print('There are ', XXX ,'missing values in the column [died].')

# -----------------------------------------------------------------------------

## Create a new dataframe with only the rows with a value in column 'died'.

#--Enter your code here--#

## In this new dataframe, how many values are missing in the 'diedCountryCode' column?

#--Enter your code here--#

#print('There are ', XXX ,'missing values in the column [diedCountryCode].')
