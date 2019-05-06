-- Create table containing relevant columns
create table x (
-- mae and cod from Regression evaluation
    mae FLOAT,
    cod FLOAT,
-- the rest from Classification evaluation
    accuracy FLOAT,
    prec FLOAT,
    recall FLOAT,
    fscore FLOAT,
    auc FLOAT,
-- String columns for describing row
    label VARCHAR,
    model VARCHAR,
    method VARCHAR,
    extra VARCHAR
);

-- Insert columns from Regression
insert into x (mae,cod)
select [Mean Absolute Error],[Coefficient of Determination]
from t1;

-- Insert columns from Classification
insert into x (accuracy,prec,recall,fscore,auc)
select Accuracy,[Precision],Recall,[F-Score],AUC
from t2;

select * from x;
