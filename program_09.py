#!/bin/env pyth on
"""
Karoll Quijano - kquijano

ABE 651: Environmental Informatics

Assignment 09
Data Quality Checking
"""


import pandas as pd
import numpy as np

def ReadData( fileName ):
    """This function takes a filename as input, and returns a dataframe with
    raw data read from that file in a Pandas DataFrame.  The DataFrame index
    should be the year, month and day of the observation.  DataFrame headers
    should be "Date", "Precip", "Max Temp", "Min Temp", "Wind Speed". Function
    returns the completed DataFrame, and a dictionary designed to contain all 
    missing value counts."""
    
    # define column names
    colNames = ['Date','Precip','Max Temp', 'Min Temp','Wind Speed']

    # open and read the file
    DataDF = pd.read_csv("DataQualityChecking.txt",header=None, names=colNames,  
                         delimiter=r"\s+",parse_dates=[0])
    DataDF = DataDF.set_index('Date')
    
    # define and initialize the missing data dictionary
    ReplacedValuesDF = pd.DataFrame(0, index=["1. No Data"], columns=colNames[1:])
        
    return( DataDF, ReplacedValuesDF )

    
DataDF, ReplacedValuesDF = ReadData('DataQualityChecking.txt')
    
def Check01_RemoveNoDataValues( DataDF, ReplacedValuesDF ):
    """This check replaces the defined No Data value with the NumPy NaN value
    so that further analysis does not use the No Data values.  Function returns
    the modified DataFrame and a count of No Data values replaced."""

    # add your code here
    DataDF = DataDF.replace([-999], np.NaN)                                      # Replace -999 with NaN     
    ReplacedValuesDF.loc["1. No Data",:] = DataDF.isna().sum()                   # Count replaced values  
    
    return( DataDF, ReplacedValuesDF )
    
DataDF, ReplacedValuesDF = Check01_RemoveNoDataValues( DataDF, ReplacedValuesDF )     
    
    
def Check02_GrossErrors( DataDF, ReplacedValuesDF ):
    """This function checks for gross errors, values well outside the expected 
    range, and removes them from the dataset.  The function returns modified 
    DataFrames with data the has passed, and counts of data that have not 
    passed the check."""
 
    # add your code here
    # Check for gross errors

    # Apply the following error thresholds: 0 ≤ P ≤ 25; -25≤ T ≤ 35, 0 ≤ WS ≤ 10.
    #Replace values outside this range with NaN.
    DataDF['Precip'][(DataDF['Precip']<0) | (DataDF['Precip']>25)] = np.NaN    
    #DataDF.loc[(]=np.NaN   
    DataDF['Max Temp'][(DataDF['Max Temp']<=-25) | (DataDF['Max Temp']>=35)] = np.NaN    
    #DataDF.loc[]=np.NaN
    DataDF['Min Temp'][(DataDF['Min Temp']<=-25) | (DataDF['Min Temp']>=35)] = np.NaN    
    # DataDF.loc[]=np.NaN   
    DataDF['Wind Speed'][(DataDF['Wind Speed']<=0) | (DataDF['Wind Speed']>=10)] = np.NaN    
    #DataDF.loc[(DataDF['Wind Speed']>=10)]=np.NaN   
    
    # Count data that have not passed the check
    #Record the number of values replaced for each data type in the dataframe ReplacedValuesDF with the index "2. Gross Error"
    ReplacedValuesDF.loc["2. Gross Error",:] = DataDF.isna().sum()- ReplacedValuesDF.sum() 

    return( DataDF, ReplacedValuesDF )
    
    
DataDF, ReplacedValuesDF = Check02_GrossErrors( DataDF, ReplacedValuesDF )    
    
    
def Check03_TmaxTminSwapped( DataDF, ReplacedValuesDF ):
    """This function checks for days when maximum air temperture is less than
    minimum air temperature, and swaps the values when found.  The function 
    returns modified DataFrames with data that has been fixed, and with counts 
    of how many times the fix has been applied."""
    
    # add your code here
    # Count when Max Temp is less than Min Temp
    ReplacedValuesDF.loc['3. Swapped', ['Min Temp','Max Temp']] = (DataDF['Min Temp']>DataDF['Max Temp']).sum()
    ReplacedValuesDF = ReplacedValuesDF.replace([np.NaN],0)    
  
    # Swap Max Temp and Min Temp when Max Temp is less than Min Temp
    DataDF.loc[DataDF['Min Temp']>DataDF['Max Temp'],['Min Temp','Max Temp']]= DataDF.loc[ DataDF['Min Temp']>DataDF['Max Temp'],['Max Temp','Min Temp']].values   

    return( DataDF, ReplacedValuesDF )
    
    
DataDF, ReplacedValuesDF = Check03_TmaxTminSwapped( DataDF, ReplacedValuesDF )    
   
    
def Check04_TmaxTminRange( DataDF, ReplacedValuesDF ):
    """This function checks for days when maximum air temperture minus 
    minimum air temperature exceeds a maximum range, and replaces both values 
    with NaNs when found.  The function returns modified DataFrames with data 
    that has been checked, and with counts of how many days of data have been 
    removed through the process."""
    
    # add your code here
    # Record the number of values replaced for each data type in the dataframe ReplacedValuesDF with the index "4. Range Fail
    ReplacedValuesDF.loc["4. Range Fail",['Min Temp','Max Temp']] = (DataDF['Max Temp']-DataDF['Min Temp']>25).sum() 
    ReplacedValuesDF = ReplacedValuesDF.replace([np.NaN],0)    
    # Identify days with temperature range (Max Temp minus Min Temp) greater than 25°C.
    # When range is exceeded replace both Tmax and Tmin with NaN
    DataDF.loc[(DataDF['Max Temp']-DataDF['Min Temp']>25),['Max Temp','Min Temp']]=np.nan 
        
    return( DataDF, ReplacedValuesDF )
    
DataDF, ReplacedValuesDF = Check04_TmaxTminRange( DataDF, ReplacedValuesDF )    
 

   
# the following condition checks whether we are running as a script, in which 
# case run the test code, otherwise functions are being imported so do not.
# put the main routines from your code after this conditional check.

if __name__ == '__main__':

    fileName = "DataQualityChecking.txt"
    DataDF, ReplacedValuesDF = ReadData(fileName)
    
    print("\nRaw data.....\n", DataDF.describe())
    
    DataDF, ReplacedValuesDF = Check01_RemoveNoDataValues( DataDF, ReplacedValuesDF )
    
    print("\nMissing values removed.....\n", DataDF.describe())
    
    DataDF, ReplacedValuesDF = Check02_GrossErrors( DataDF, ReplacedValuesDF )
    
    print("\nCheck for gross errors complete.....\n", DataDF.describe())
    
    DataDF, ReplacedValuesDF = Check03_TmaxTminSwapped( DataDF, ReplacedValuesDF )
    
    print("\nCheck for swapped temperatures complete.....\n", DataDF.describe())
    
    DataDF, ReplacedValuesDF = Check04_TmaxTminRange( DataDF, ReplacedValuesDF )
    
    print("\nAll processing finished.....\n", DataDF.describe())
    print("\nFinal changed values counts.....\n", ReplacedValuesDF)
    
    
    
    
''' PLOTS
# Plot each dataset before and after correction has been made.
# Use a single set of axis for each variable, and
# provide a legend that indicates which variable is the original and which is after quality checking.   '''

# Make a copy of original dataset
colNames = ['Date','Precip','Max Temp', 'Min Temp','Wind Speed']
DataDFcopy = pd.read_csv("DataQualityChecking.txt",header=None, names=colNames, delimiter=r"\s+",parse_dates=[0])
DataDFcopy = DataDFcopy.set_index('Date')    

import matplotlib.pyplot as plt

### Precipitation 
plt.plot(DataDFcopy['Precip'], marker='.', linestyle='None', color= 'r', markersize=8, label='Before Quality Check')
plt.plot(DataDF['Precip'], marker='.', linestyle='None', color= 'b',markersize=8, label='After Quality Check')
plt.title('Precipitation')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.xticks(rotation=90)
plt.legend()
plt.savefig('01_Precipitation.png', bbox_inches='tight')
plt.show
plt.close()
    
### Maximum air temperature (°C) 
plt.plot(DataDFcopy['Max Temp'], marker='.', linestyle='None', color= 'r', markersize=8, label='Before Quality Check')
plt.plot(DataDF['Max Temp'], marker='.', linestyle='None', color= 'b',markersize=8, label='After Quality Check')
plt.title('Maximum Air Temperature')
plt.xlabel('Date')
plt.ylabel('Maximum air temperature (°C)')
plt.xticks(rotation=90)
plt.legend()
plt.savefig('02_MaxTemp.png', bbox_inches='tight')
plt.show
plt.close()

### Minimum air temperature (°C) 
plt.plot(DataDFcopy['Min Temp'], marker='.', linestyle='None', color= 'r', markersize=8, label='Before Quality Check')
plt.plot(DataDF['Min Temp'], marker='.', linestyle='None', color= 'b',markersize=8, label='After Quality Check')
plt.title('Minimum Air Temperature')
plt.xlabel('Date')
plt.ylabel('Minimum air temperature (°C)')
plt.xticks(rotation=90)
plt.legend()
plt.savefig('03_MinTemp.png', bbox_inches='tight')
plt.show
plt.close()

### Wind speed (m/s) 
plt.plot(DataDFcopy['Wind Speed'], marker='.', linestyle='None', color= 'r', markersize=8, label='Before Quality Check')
plt.plot(DataDF['Wind Speed'], marker='.', linestyle='None', color= 'b',markersize=8, label='After Quality Check')
plt.title('Wind Speed')
plt.xlabel('Date')
plt.ylabel('Wind speed (m/s)')
plt.xticks(rotation=90)
plt.legend()
plt.savefig('04_WindSpeed.png', bbox_inches='tight')
plt.show
plt.close()    



''' NEW TXT FILES '''   
  
# Write data that has passed the quality check into a new file with the same format as the input data file.
DataDF.to_csv('DataQualityCheckingCorrected.txt', header=None, index=True, sep=' ', mode='a')

#Output information on failed checks to a separate Tab delimited file that can be imported into your Metadata file.
ReplacedValuesDF.to_csv('ReplacedValuesDF.txt', header=None, index=True, sep='\t', mode='a')
