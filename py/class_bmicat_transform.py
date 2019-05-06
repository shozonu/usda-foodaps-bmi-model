import pandas as pd

def azureml_main(dataframe1 = None, dataframe2 = None):
    # Turn bmicat values '3' into '2'.
    # Results in 2 unique values in column:
    # 1 (Not overweight) and 2 (Overweight or Obese)
    for index, row in dataframe1.iterrows():
        if(dataframe1['bmicat'].iat[index] != "1"):
            dataframe1['bmicat'].iat[index] = "2"
    
    return dataframe1
