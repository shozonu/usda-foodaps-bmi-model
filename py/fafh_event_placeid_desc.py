import pandas as pd

def azureml_main(df = None):
    # Create dictionary to hold values
    arr = {"desc" : [] ,"id" : []}
    for index, row in df.iterrows():
        # Place description occurs every nth row,
        # Corresponding place id occurs every n-3th row
        if((index + 1) % 4 == 0):
            arr["id"].append(int(df["raw"].iat[index - 3]))
            arr["desc"].append(df["raw"].iat[index])
    
    # Construct new dataframe from dictionary
    data = pd.DataFrame.from_dict(arr)
    
    # Rearrange columns so that id is first
    cols = data.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    data = data[cols]
    return data
