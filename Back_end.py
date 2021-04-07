from sklearn import tree
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics




li = []
Play = '?'
Accuracy=0



def main_calculation():

    for i in range(len(li)):
        for j in range(len(li[i])):
            if i==0:
                if(li[i][j]==1):
                    Outlook = j+1
                    break
            elif i==1:
                if(li[i][j]==1):
                    Temperature = j+1
                    break

            elif i==2:
                if(li[i][j]==1):
                    Humidity = j+1
                    break

            elif i==3:
                if(li[i][j]==1):
                    Windy = j
                    break


    #print(f"{Outlook} {Temperature} {Humidity} {Windy}")




    data = pd.read_csv(".\\Dataset.csv")

    features =[]

    # Iterate over each row
    for index, rows in data.iterrows():
        # Create list for the current row
        my_list =[int(rows.x1), int(rows.x2), int(rows.x3), int(rows.x4)]

        # append the list to the final list
        features.append(my_list)


    #print(features)
    labels = data.y.tolist()
    #print(labels)

    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.5) # 50% training and 50% test



    clf = tree.DecisionTreeClassifier() #it is an empty box of rules
    clf = clf.fit(X_train, y_train) # Train Decision Tree Classifer,

    global Play
    Play = list(clf.predict([[Outlook,Temperature,Humidity,Windy]]))

    playAccuracy = list(clf.predict(X_test))

    #print(Play)

    global Accuracy
    Accuracy = metrics.accuracy_score(y_test, playAccuracy)
