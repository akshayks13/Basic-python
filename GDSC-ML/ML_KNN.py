import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# Loading the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Splitting the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Printing general dataset details
print("Names of classes: ", iris.target_names)
print("Feature details: ", iris.feature_names)

# Creating the KNN model
knn = KNeighborsClassifier(n_neighbors=3)

# Training the model
knn.fit(X_train, y_train)

# Making predictions
y_pred = knn.predict(X_test)

# Evaluating the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

# Plotting a simple visualization
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='viridis')
plt.xlabel('Feature 1 (Sepal length)')
plt.ylabel('Feature 2 (Sepal width)')
plt.title(f'KNN Classification Results (Test set) - Accuracy: {accuracy:.2f}')

# Adding a legend
# We use the target names and the corresponding colors from the colormap
for i, target_name in enumerate(iris.target_names):
    plt.scatter([], [], color=plt.cm.viridis(i / 2), label=target_name)
plt.legend(title="Species")
plt.show()