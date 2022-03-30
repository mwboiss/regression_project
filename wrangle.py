# Import for data manipulation
import pandas as pd
import numpy as np

# Import for scaling and splitting data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Import for database access
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
    fips
    FROM properties_2017
    JOIN predictions_2017
    USING(parcelid)
    JOIN propertylandusetype
    USING(propertylandusetypeid)
    WHERE propertylandusetypeid = 261
    ''', url)
    
    # Notify user of next step
    print('Saving new csv...')
    
    # Create csv
    zillow_data.to_csv(filename, index=False)
    
    # Return DataFrame
    return zillow_data

def prep_zillow(df):
    '''
    function used to wrangle zillow data
    '''
        
    # Rename columns
    df = df.rename(columns={'bedroomcnt' : 'bedrooms',\
                            'bathroomcnt' : 'bathrooms',\
                            'calculatedfinishedsquarefeet' : 'area',\
                            'taxvaluedollarcnt' : 'taxable_value',\
                            'yearbuilt' : 'year_built',\
                            'fips' : 'county'})
    
     # Create a variable that shows the age of the house in 2017
    df['house_age_2017'] = 2017 - df.year_built 
    
    # Create a variable that shows the ratio of bedrooms to bathrooms
    df['bed_to_bath_ratio'] = df.bedrooms / df.bathrooms

    # Replace infinite values with NaN to be dropped later
    df = df.replace(np.inf, np.nan)
    
    # Drop Nulls
    df = df.dropna()
    
    # Map county values to name of county
    df.county = df.county.map({6037.0 : 'los_angeles_ca',\
                               6059.0 : 'orange_ca',\
                               6111.0 : 'ventura_ca'})
    
    # One hot encode county 

    # Get dummy variables
    dummy_name = pd.get_dummies(df[['county']])

    # Concat dummy_name to dataframe
    df = pd.concat([df,dummy_name],axis=1)
    
    return df

def remove_outliers(df, column_list):
    ''' remove outliers from dataframe 
        then return the new dataframe
    '''
    # Iterate through column_list
    for col in column_list:
        
        # find percentiles
        q_25 = np.percentile(df[col], 25)
        q_75 = np.percentile(df[col], 75)
        
        # Calculate IQR
        iqr = q_75 - q_25
        
        # assign upper bound
        upper_bound = q_75 + 1.5 * iqr   
        
        # assign lower bound 
        lower_bound = q_25 - 1.5 * iqr   

        # assign df without outliers
        df = df[(df[col] > lower_bound) & (df[col] < upper_bound)]
        
    # return dataframe without outliers    
    return df

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

def model_split(df):
    
    # Assign x for testing the model, y as target for modeling
    X = df.drop(columns=['taxable_value'])
    y = df[['taxable_value']]
    
    return X, y

def wrangle_zillow(use_cache = True):
    
    # Get Zillow data from database
    zillow = get_zillow_data(use_cache)
    
    # Prepare Zillow data
    zillow = prep_zillow(zillow)
    
    # remove outliers
    zillow = remove_outliers(zillow, ['bedrooms','bathrooms','year_built','area','taxable_value','house_age_2017','bed_to_bath_ratio'])
     
    # Split the data for modeling
    train, validate, test = split_zillow(zillow)
    
    return train, validate, test