import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler  
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
import pickle

data = pd.read_csv("C:/Users/SriramAditya/Desktop/ML CBP/SIP/src/posts/Heart_Disease_Prediction.csv")

x= data.iloc[:, 0:13].values
y= data.iloc[:, 13].values

x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 0.25, random_state=42)
st_x= StandardScaler()    
x_train= st_x.fit_transform(x_train)
x_test= st_x.transform(x_test)  

classifier= KNeighborsClassifier(n_neighbors=12, metric='minkowski', p=2 )
classifier.fit(x_train, y_train)

y_pred= classifier.predict(x_test)
print("Accuracy:",accuracy_score(y_test,y_pred))

pickle.dump(classifier, open('knnClassifier.pkl', 'wb'))