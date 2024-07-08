from diabetes_prediction import DiabetesPredictor


predictor = DiabetesPredictor()

user_inputs = []

print("To predict whether you are at risk of diabetes, you will need to provide some information about yourself.")
print("Enter your number for each of the following fields.")
print("If you're not sure for any of these, enter -1. Note that doing this multiple time will give inaccurate results.")

for field in predictor.df.iloc[:, 0:8].columns.tolist():
    user_input = float(input(field + ": "))
    if user_input == -1:
        user_input = predictor.df[field].mean(skipna=True)
    user_inputs.append(user_input)

print(predictor.has_diabetes(user_inputs))