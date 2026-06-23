import pandas as pd

def audit_and_clean_data(dataframe):
    print("\n[SECURITY SCAN] Running UEBA filters on student metrics...")
    
   
    clean_dataframe = dataframe.fillna(dataframe.mean(numeric_only=True))
    
    valid_data_condition = (clean_dataframe['Study_Hours'] <= 24) & (clean_dataframe['Sleep_Hours'] >= 0)
    
    
    clean_dataframe = clean_dataframe[valid_data_condition]
    return clean_dataframe
    