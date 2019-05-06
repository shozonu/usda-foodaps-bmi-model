import pandas as pd

def azureml_main(df1 = None):
    # Strings describing the rows, in order.
    d_label = [
        "BMI",
        "BMI",
        "BMI",
        "BMI",
        "BMI",
        "BMI",
        "BMI",
        "BMI Category",
        "BMI Category",
        "BMI Category",
        "BMI Category",
        "BMI Category",
        "BMI Category"
    ]
    d_model = [
        "Regression",
        "Regression",
        "Regression",
        "Regression",
        "Regression",
        "Regression",
        "Regression",
        "Classification",
        "Classification",
        "Classification",
        "Classification",
        "Classification",
        "Classification"
    ]
    d_method = [
        "Bayesian",
        "Bayesian",
        "Decision Forest",
        "Bayesian",
        "Bayesian",
        "Bayesian",
        "Bayesian",
        "SVM",
        "SVM",
        "SVM",
        "SVM",
        "SVM",
        "SVM"
    ]
    d_extra = [
        "Binned",
        "Not Binned",
        " ",
        "Clip 95%, Binned",
        "Clip 95%, Not Binned",
        "Clip 90%, Binned",
        "Clip 90%, Not Binned",
        " ",
        "X-Validated",
        "Clip 95%",
        "Clip 95%, X-Validated",
        "Clip 90%",
        "Clip 90%, X-Validated"
    ]
    for index,row in df1.iterrows():
        df1["label"].iat[i] = d_label[index]
        df1["model"].iat[i] = d_model[index]
        df1["method"].iat[i] = d_method[index]
        df1["extra"].iat[i] = d_extra[index]
    return df1
