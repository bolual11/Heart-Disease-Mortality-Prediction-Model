# Heart-Disease-Mortality-Prediction-Model

## Intro: 
Heart diseases are the number 1 cause of death around the world. They are responsible for a third of the deaths globally, with an estimated 18 million deaths resulting from heart disease. I will explore the ‘Heart Failure Clinical Records’ dataset which I discovered on Kaggle. Using this dataset, I will drop columns I do not need to help me predict the mortality by heart disease. Individuals with cardiovascular disease, or those at elevated risk due to factors like hypertension, diabetes, hyperlipidemia, or an existing condition will require prompt detection and effective management. This is where a machine learning program would be effective. 


## Goal: Create a model for predicting mortality caused by Heart Disease.
Using Excel and Python libraries
Health Datasets

## How to determine heart attack risk factor?
Age
Sex 
Race
Clinical records e.g platelets, diabetes status, cholesterol levels
Family history

## Advantages of using the current dataset
Consistent data types (numeric), which simplifies preprocessing.
Directly related to heart failure, with a clear target variable (DEATH_EVENT) indicating heart-related events.

## Features:
Age: age of the patient (years)
Anemia: decrease of red blood cells or hemoglobin (boolean)
Creatinine phosphokinase  (CPK): level of the CPK enzyme in the blood (mcg/L)
Diabetes: if the patient has diabetes (boolean)
Ejection fraction: percentage of blood leaving the heart at each contraction  (percentage)
High blood pressure: if the patient has hypertension (boolean)
Platelets: platelets in the blood (kilo platelets/mL)
Sex: woman or man (binary)
Serum creatinine: level of serum creatinine in the blood (mg/dL)
serum sodium: level of serum sodium in the blood (mEq/L)
smoking: if the patient smokes or not (boolean)
time: follow-up period (days)

## Target:
Death event: if the patient died during the follow-up period (boolean)

## Testing model:
Logistics Regression: This is an algorithm that is used in this case to estimate whether a patient will experience a death event (1) or not (0). The number is the probability. This model can be split into three parts, with these being ‘Accuracy’, ‘ Confusion matrix’, and ‘Classification report’.

Accuracy: This feature tells me the percentage of correct predictions.
Confusion Matrix: This matrix breaks down how well the model can distinguish between my ‘DEATH’ and ‘NO DEATH’ sections. The matrix follows this format: 
[True Negatives    ​False Positives
False Negatives    True Positives]

Classification Report: The classification report provides more detailed metrics for each grouping. In this model, the more detailed metrics are: ‘Precision’, ‘Recall’, ‘F1 Score’, and ‘Support’.
Precision: Precision tells me how many patients actually died out of all the patients that were predicted as dead. In this case, for Class 1 (death events), a precision of 0.88 means that 88% of the times the model predicted a death event, it was correct. This means the model is quite confident when it predicts death events.

Recall: Recall tells me out of all the patients who actually died, how many the model correctly predicted as dead. In this case, a recall of 0.28 for Death events means that the model only correctly identified 28% of actual deaths. A recall of 0.97 means that the model correctly predicted survival in 97% of survivors.

F1 Score: This is the mean of precision and recall. This score gives me a single metric, showing me how well the model is balancing precision and recall.
Support: 

Mean Squared Error (MSE): This number represents the average squared difference between actual and anticipated mortality rates. A lower MSE score indicates that the predictions are closer to the actual values.
R² Score (R-squared): Measures how well the model explains the variation in death rates. A model with a R² score near to 1 effectively explains data variability, whereas a number closer to 0 indicates inadequate explanation.

## Sources:
Background info:
https://ourworldindata.org/cardiovascular-diseases#:~:text=As%20you%20can%20see%2C%20heart,total%20of%20around%2018%20million. 
https://www.medicalnewstoday.com/articles/282929#:~:text=Heart%20disease%20is%20the%20leading,disease%20to%20describe%20several%20conditions
Datasets:
Heart Failure Clinical Records. (2020). UCI Machine Learning Repository. https://doi.org/10.24432/C5Z89R. 
https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data/data 
