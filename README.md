# Innis-Regression-Project

This repo is a 

## About the Project

### Project Goals

The goal of this project is 

### Project Description


### Initial Questions

1) 

2) 

3) 

4) 

### Summary of Findings



### Data Dictionary

Variable | Meaning |
:-: | :-- |
'airconditioningtypeid'|Type of cooling system present in the home (if any)
'architecturalstyletypeid'|Architectural style of the home (i.e. ranch, colonial, split-level, etc…)
'basementsqft'|Finished living area below or partially below ground level
'bathroomcnt'|Number of bathrooms in home including fractional bathrooms
'bedroomcnt'|Number of bedrooms in home 
'buildingqualitytypeid'|Overall assessment of condition of the building from best (lowest) to worst (highest)
'buildingclasstypeid'|The building framing type (steel frame, wood frame, concrete/brick) 
'calculatedbathnbr'|Number of bathrooms in home including fractional bathroom
'decktypeid'|Type of deck (if any) present on parcel
'threequarterbathnbr'|Number of 3/4 bathrooms in house (shower + sink + toilet)
'finishedfloor1squarefeet'|Size of the finished living area on the first (entry) floor of the home
'calculatedfinishedsquarefeet'|Calculated total finished living area of the home 
'finishedsquarefeet6'|Base unfinished and finished area
'finishedsquarefeet12'|Finished living area
'finishedsquarefeet13'|Perimeter  living area
'finishedsquarefeet15'|Total area
'finishedsquarefeet50'| Size of the finished living area on the first (entry) floor of the home
'fips'|Federal Information Processing Standard code -  see https://en.wikipedia.org/wiki/FIPS_county_code for more details
'fireplacecnt'|Number of fireplaces in a home (if any)
'fireplaceflag'|Is a fireplace present in this home 
'fullbathcnt'|Number of full bathrooms (sink, shower + bathtub, and toilet) present in home
'garagecarcnt'|Total number of garages on the lot including an attached garage
'garagetotalsqft'|Total number of square feet of all garages on lot including an attached garage
'hashottuborspa'|Does the home have a hot tub or spa
'heatingorsystemtypeid'|Type of home heating system
'latitude'|Latitude of the middle of the parcel multiplied by 10e6
'logerror'|log(Zestimate)−log(SalePrice)
'longitude'|Longitude of the middle of the parcel multiplied by 10e6
'lotsizesquarefeet'|Area of the lot in square feet
'numberofstories'|Number of stories or levels the home has
'parcelid'|Unique identifier for parcels (lots) 
'poolcnt'|Number of pools on the lot (if any)
'poolsizesum'|Total square footage of all pools on property
'pooltypeid10'|Spa or Hot Tub
'pooltypeid2'|Pool with Spa/Hot Tub
'pooltypeid7'|Pool without hot tub
'propertycountylandusecode'|County land use code i.e. it's zoning at the county level
'propertylandusetypeid'|Type of land use the property is zoned for
'propertyzoningdesc'|Description of the allowed land uses (zoning) for that property
'rawcensustractandblock'|Census tract and block ID combined - also contains blockgroup assignment by extension
'censustractandblock'|Census tract and block ID combined - also contains blockgroup assignment by extension
'regionidcounty'|County in which the property is located
'regionidcity'|City in which the property is located (if any)
'regionidzip'|Zip code in which the property is located
'regionidneighborhood'|Neighborhood in which the property is located
'roomcnt'|Total number of rooms in the principal residence
'storytypeid'|Type of floors in a multi-story house (i.e. basement and main level, split-level, attic, etc.).  See tab for details.
'typeconstructiontypeid'|What type of construction material was used to construct the home
'unitcnt'|Number of units the structure is built into (i.e. 2 = duplex, 3 = triplex, etc...)
'yardbuildingsqft17'|Patio in  yard
'yardbuildingsqft26'|Storage shed/building in yard
'yearbuilt'|The Year the principal residence was built 
'taxvaluedollarcnt'|The total tax assessed value of the parcel
'structuretaxvaluedollarcnt'|The assessed value of the built structure on the parcel
'landtaxvaluedollarcnt'|The assessed value of the land area of the parcel
'taxamount'|The total property tax assessed for that assessment year
'assessmentyear'|The year of the property tax assessment 
'taxdelinquencyflag'|Property taxes for this parcel are past due as of 2015
'taxdelinquencyyear'|Year for which the unpaid propert taxes were due 

### Steps to Reproduce

1. A locally stored env.py file containing hostname, username and password for the mySQL database containing the zillow dataset is needed.

2. Data Science Libraries needed: pandas, numpy, matplotlib.pyplot, seaborn, scipy.stats, sklearn

3. All files in the repo should be cloned to reproduce this project.

4. Ensuring .gitignore is setup to protect env.py file data.

## Plan of Action

### Wrangle

#### Modules

##### Acquire

1) Create and test acquire functions

2) Add functions to acquire.py module

3) Import acquire.py functions and test in notebook

##### Prepare

1) Create and test prepare fucntions

2) Add functions to prepare.py module

3) Import prepare.py functions and test in notebook

##### Missing Values

1) Explore data for missing values

2) Add code to prepare function to remove values

3) Test function in notebook

##### Data Split

1) Write code needed to split data into train, validate and test

2) Add code to prepare function and test in notebook

##### Explore

###### Each Feature Individually

###### Pairs of Variables

###### Multiple Variables

###### Questions to Answer

1) 

2) 

3) 

4) 

###### Explore through visualizations

1) Create visualizations exploring each question

###### Statistics tests

1) Run statistics test relevant to each question

###### Summary 

1) Create a summary that answers exploritory questions

#### Modeling

1) Evaluate which metrics best answer each question

2) Evaluate a basline meteric used to compare models to the most present target variable

3) Develop models to predict whether a customer churns or not

4) Fit the model to Train data

5) Evaluate on Validate data to ensure no overfitting

6) Evaluate top model on test data

#### Report

1) Create report ensuring well documented code and clear summary of findings as well as next steps to improve research