# Data Classification Using AI

## About

A simple AI-based data classification project developed using Python and Scikit-learn. The project uses student data to predict the result based on study hours, attendance, and sleep hours.

## Dataset

The dataset contains:

* Hours Studied
* Attendance
* Sleep Hours
* Result

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Decision Tree Classifier

## How It Works

1. The student dataset is loaded using Pandas.
2. The `Result` column is separated as the target variable.
3. The remaining columns are used as input features.
4. The dataset is divided into training and testing data using `train_test_split()`.
5. A Decision Tree Classifier is trained using the training data.
6. The trained model predicts results for the test data.
7. Accuracy is calculated by comparing the predicted results with the actual results.
8. The model is also used to predict the result of a new student.
9. A confusion matrix is displayed to evaluate the classification results.

## Train-Test Split

The dataset is split into:

* **80% Training Data** – used to train the model.
* **20% Testing Data** – used to test the model on unseen input.

The split uses `random_state=42` so that the same split can be reproduced.

## Model Used

**Decision Tree Classifier**

The Decision Tree learns patterns from the training data and uses those patterns to classify the results of new data.

## Output

The program displays:

* Training and testing datasets
* Predictions made by the model
* Actual test results
* Accuracy
* Prediction for a new student
* Confusion matrix

## Learning Outcome

This project helped me understand supervised learning, train-test splitting, model training, prediction, accuracy evaluation, Decision Tree classification, and confusion matrices.
