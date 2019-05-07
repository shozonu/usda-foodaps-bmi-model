# USDA FoodAPS BMI Modeling
## Spring 2019 CIS 3200 Data Processing/Analytics Project

### Description
Create a machine learning model using Azure ML Studio that can accurately predict an individual's body mass index (BMI) given the frequency of various food sources near their household.

Uses the frequency of various categories of food sources within various distances to survey respondants' households.

### Result
Out of the configurations tested, using Bayesian Linear Regression on clipped (data within 10 and 90 percentile) and binned (each frequency column quantized into 10 bins of percentiles) yielded the best overall result:

Metric | Value
----|----
Mean Absolute Error:| 2.039
Root Mean Squared Error:|2.737
Relative Absolute Error:|0.566
Relative Squared Error:|0.404
Coefficient of Determination:|0.596

For the purpose of BMI predictions, Mean Absolute Error is the most useful metric to gauge performance by.
With a mean absolute error of ~2 in a dataset where mean BMI is 25, the predictions given by the model are fairly accurate within 2-3 standard deviations of the mean.

#### USDA FoodAPS Data:
https://www.ers.usda.gov/data-products/foodaps-national-household-food-acquisition-and-purchase-survey/

#### Azure ML Gallery:
https://gallery.cortanaintelligence.com/Experiment/USDA-FoodAPS-BMI-Modeling

#### Presentation Link:
https://docs.google.com/presentation/d/16hM15KZuClYDjCQdylandxbIRArnYA1okK7JqKcARxw/edit?usp=sharing
