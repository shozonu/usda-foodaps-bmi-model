import pandas as pd

def azureml_main(dataframe1 = None, dataframe2 = None):
    # For each row
    for index, row in dataframe1.iterrows():
        hnum = dataframe1['hhnum'].iat[index]
        pnum = dataframe1['PNUM'].iat[index]
        
        # Append create unique pid by appending pnum to end of hhnum
        pid = int("{}{}".format(hnum, pnum), 10)
        dataframe1["hhnum"].iat[index] = pid
    
    # Rename columns
    dataframe1.rename(columns={"hhnum" : "pid"}, inplace = True)
    dataframe1.rename(columns={"NDINNERSOUT" : "ndinnersout"}, inplace = True)
    dataframe1.rename(columns={"HEALTHSTATUS" : "healthstatus"}, inplace = True)
    dataframe1.rename(columns={"BMICAT" : "bmicat"}, inplace = True)
    dataframe1.rename(columns={"BMI" : "bmi"}, inplace = True)
    
    # Drop pnum column
    dataframe1.drop(["PNUM"], axis=1, inplace = True)
    
    return dataframe1