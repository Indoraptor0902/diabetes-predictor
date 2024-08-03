import diabetes_prediction
import numpy as np

predictor = diabetes_prediction.DiabetesPredictor()

total_insulin = 0
subjects = 0

for i in range(len(predictor.df)):
    if predictor.df.iloc[i, 7] > 12 and predictor.df.iloc[i, 7] < 20:
        total_insulin += predictor.df.iloc[i, 4]
        subjects += 1

try:
    print(total_insulin / subjects)
except ZeroDivisionError:
    print("None of the subjects are teenagers")