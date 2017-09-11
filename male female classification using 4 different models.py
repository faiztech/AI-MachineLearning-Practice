from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier

#{height, weights, shoe size}

X = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[171,75,42],[181,85,43]]

Y = ['male','female','female','female','male','male','male','female', 'female','male']

P = [[190,70,43]]

#{Decision Tree Model}
clf = DecisionTreeClassifier()
clf = clf.fit(X,Y)
print "\n1) Using Decision Tree Prediction is " + str(clf.predict(P))



#{K Neighbors Classifier}
neigh = KNeighborsClassifier()
neigh.fit(X,Y)
print "2) Using K Neighbors Classifier Prediction is " + str(neigh.predict(P))


#{using MLPClassifier}
mlpc = MLPClassifier()
mlpc.fit(X,Y)
print "3) Using MLPC Classifier Prediction is " + str(mlpc.predict(P))


#{using MLPClassifier}
rfor = RandomForestClassifier()
rfor.fit(X,Y)
print "4) Using RandomForestClassifier Prediction is " + str(rfor.predict(P)) +"\n"
