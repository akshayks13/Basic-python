from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron

from sklearn.metrics import accuracy_score
import numpy as np

iris = datasets.load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=8)

scaler = StandardScaler()
scaler.fit(X_train)

X_train_std = scaler.transform(X_train)
X_test_std = scaler.transform(X_test)

clf = Perceptron(max_iter=1000,random_state=42)
clf.fit(X_train_std, y_train)

ypred = clf.predict(X_test_std)
print('Misclassified %d' % (y_test != ypred).sum())

# Accuracy score
print('Accuracy score %.2f' % accuracy_score(y_test, ypred))

class My_Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000, random_state=None):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.random_state = random_state
        self.weights = None
        self.bias = None

    def signum(self, x):
        return np.where(x >= 0, 1, 0)

    def fit(self, X, y):
        if self.random_state is not None:
            np.random.seed(self.random_state)

        # Initialize weights and bias
        self.weights = np.random.random(X.shape[1])
        self.bias = np.random.random()

        for _ in range(self.n_iterations):
            # Calculate the predicted values
            predictions = self.signum(np.dot(X, self.weights) + self.bias)

            # Update weights and bias based on the perceptron learning rule
            self.weights += self.learning_rate * np.dot((y - predictions), X)
            self.bias += self.learning_rate * np.sum(y - predictions)

    def predict(self, X):
        # Return the signum of the dot product of features and weights, plus the bias
        return self.signum(np.dot(X, self.weights) + self.bias)

y_train_binary = np.where(y_train == 0, 1, 0)
y_test_binary = np.where(y_test == 0, 1, 0)

my_perceptron = My_Perceptron(learning_rate=0.01, n_iterations=1000, random_state=42)
my_perceptron.fit(X_train_std, y_train_binary)

predictions = my_perceptron.predict(X_test_std)

# Count misclassifications
misclassified = np.sum(y_test_binary != predictions)
print('Misclassified:', misclassified)

accuracy = accuracy_score(y_test_binary, predictions)
print('Accuracy score: %.2f' % accuracy)

from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Calculate the confusion matrix
conf_matrix = confusion_matrix(y_test_binary, predictions)

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=['Not Class 0', 'Class 0'], yticklabels=['Not Class 0', 'Class 0'])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()
