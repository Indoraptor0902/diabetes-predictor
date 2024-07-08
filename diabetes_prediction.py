import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score


class DiabetesPredictor:
    def __init__(self):
        self.orig_df = pd.read_csv('diabetes.csv')
        self.df = self.orig_df
        self.zero_not_accepted = ['Glucose', 'BloodPressure', 'SkinThickness', 'BMI', 'Insulin']

        self.setup_df()
        self.train()

    def setup_df(self):
        for column in self.zero_not_accepted:
            self.df[column] = self.df[column].replace(0, np.nan)
            mean = int(self.df[column].mean(skipna=True))
            self.df[column] = self.df[column].replace(np.nan, mean)
        
        self.X = self.df.iloc[:, 0:8]
        self.y = self.df.iloc[:, 8]
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2)

        self.sc_X = StandardScaler()
        self.X_train = self.sc_X.fit_transform(self.X_train)
        self.X_test = self.sc_X.transform(self.X_test)
    
    def train(self):
        self.classifier = KNeighborsClassifier(n_neighbors=11, p=2, metric='euclidean')
        self.classifier.fit(self.X_train, self.y_train)

        self.y_pred = self.classifier.predict(self.X_test)
    
    def confusion_matrix(self):
        return confusion_matrix(self.y_test, self.y_pred)
    
    def f1_score(self):
        return f1_score(self.y_test, self.y_pred)
    
    def accuracy_score(self):
        return accuracy_score(self.y_test, self.y_pred)
    
    def has_diabetes(self, user_input):
        # Ensure the input is a list of floats
        user_data = list(map(float, user_input))
        
        # Convert the user input into a numpy array and reshape it
        user_data = np.array(user_data).reshape(1, -1)
        
        # Replace zeros with the mean values for columns that cannot have zero
        for i, column in enumerate(self.zero_not_accepted):
            if user_data[0, i] == 0:
                user_data[0, i] = self.df[column].mean(skipna=True)
        
        # Scale the user input data
        user_data = self.sc_X.transform(user_data)
        
        # Make prediction
        prediction = self.classifier.predict(user_data)
        
        if prediction[0] == 1:
            return True
        else:
            return False


predictor = DiabetesPredictor()

print(predictor.has_diabetes([0,predictor.df['Glucose'].mean(skipna=True), 83,predictor.df['SkinThickness'].mean(skipna=True),predictor.df['Insulin'].mean(skipna=True), 20.9,predictor.df['DiabetesPedigreeFunction'].mean(skipna=True),16]))
print(predictor.confusion_matrix(), predictor.accuracy_score(), predictor.f1_score())

true_count = 0
false_count = 0

for prediction in predictor.orig_df.iloc[:, 8]:
    if prediction == 1:
        true_count += 1
    elif prediction == 0:
        false_count += 1

print("Number of true: " + str(true_count) + " | Number of false: " + str(false_count))