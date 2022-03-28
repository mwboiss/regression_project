import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import sklearn.preprocessing

from env import get_db_url
import os

def get_zillow_data(use_cache=True):
    '''
    This functions recieves a boolean as input to see if the user wants to recieve a fresh copy from the database.
    Then the fucntion checks to see if the file being requested already exists.
    Runs a query for the data using the assigned url.
    Creates a new csv if needed.
    Then returns the zillow dataframe.
    '''
    
    # Assign filename to csv for storage
    filename = 'zillow.csv'
    
    # Check if file exists and if user wants a fresh copy from the database
    if os.path.exists(filename) and use_cache:
        print('Using cached csv file...')
        return pd.read_csv(filename)
    
    # Notify user of next step
    print('Retrieving from database...')
    
    # Assign url
    url = get_db_url('zillow')
    
    # Run query for data
    zillow_data = pd.read_sql('''
    SELECT bedroomcnt,\
    bathroomcnt,\
    calculatedfinishedsquarefeet,\
    taxvaluedollarcnt,\
    yearbuilt,\
    taxamount,\
    fips
    FROM properties_2017
    LEFT JOIN propertylandusetype
    USING(propertylandusetypeid)
    WHERE propertylandusetypeid = 261
    ''', url)
    
    # Notify user of next step
    print('Saving new csv...')
    
    # Create csv
    zillow_data.to_csv(filename, index=False)
    
    # Return DataFrame
    return zillow_data


def wrangle_zillow(use_cache=True):
    '''
    function used to wrangle zillow data
    '''
    # Get Zillow data
    zillow = get_zillow_data(use_cache)
        
    # Rename columns
    zillow = zillow.rename(columns={'bedroomcnt' : 'bedrooms',\
                                'bathroomcnt' : 'bathrooms',\
                                'calculatedfinishedsquarefeet' : 'area',\
                                'taxvaluedollarcnt' : 'taxable_value',\
                                'yearbuilt' : 'year_built',\
                                'taxamount' : 'tax_amount',\
                                'fips' : 'county'})
    
    # Drop Nulls
    zillow = zillow.dropna()
    
    # Map county values to name of county
    zillow.county = zillow.county.map({6037.0 : 'los_angeles_ca',\
                                       6059.0 : 'orange_ca',\
                                       6111.0 : 'ventura_ca'})
    
    
    # One hot encode county 

    # Get dummy variables
    dummy_name = pd.get_dummies(zillow[['county']])

    # Concat dummy_name to dataframe
    zillow = pd.concat([zillow,dummy_name],axis=1)
    
    return zillow

def split_zillow(df):
    '''
    This funciton splits the dataset for modeling into:
    train - for exploring the data, and fitting the models
    validate - for ensuring the model is not overfit
    test - for testing the model on unseen data
    '''
    # This seperates out the test data from the train and validate data. Test makes up 20 % of the data.
    train_validate, test = train_test_split(df, random_state=1729, test_size=0.2)
    
    # This seperates out the train and validates sets. Train makes up 56 % of the data and Validate makes up 24 %.
    train, validate = train_test_split(train_validate, random_state=1729, test_size=0.3)
    
    # The funciton returns the split sets
    return train, validate, test


def scale_data(train, validate, test, return_scaler=False):
    '''
    This function scales the split data and returns a scaled version of the dataset.
    
    If return_scaler is true, the scaler will be returned as well.
    '''
    
    col = train.columns[train.dtypes == 'float']
    col = col.append(train.columns[train.dtypes == 'int'])

    train_scaled = train[col]
    validate_scaled = validate[col]
    test_scaled = test[col]

    scaler = MinMaxScaler()
    scaler.fit(train[col])
    
    train_scaled[col] = scaler.transform(train[col])
    validate_scaled[col] = scaler.transform(validate[col])
    test_scaled[col] = scaler.transform(test[col])
    
    if return_scaler:
        return train_scaled, validate_scaled, test_scaled, scaler
    else:
        return train_scaled, validate_scaled, test_scaled