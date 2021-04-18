
import pandas as pd
df = pd.read_csv("winequality-red.csv")


quality_mapping ={
    4:0,
    5:1,
    6:2,
    3:3,
    7:4,
    8:5
}

df.loc[:,"quality"] = df.quality.map(quality_mapping)

df = df.sample(frac=1).reset_index(drop=True)

df_train = df.head(1000)
df_test = df.tail(599)



from sklearn import tree, metrics

clf = tree.DecisionTreeClassifier(max_depth=3)

cols = ['fixed acidity' , 'volatile acidity' , 'citric acid' , 
        'residual sugar' , 'chlorides' , 'free sulfur dioxide' ,
        'total sulfur dioxide' , 'density' , 'pH' , 'sulphates',
        'alcohol']
#print(df_train.quality)
clf.fit(df_train[cols], df_train.quality)

train_predictions = clf.predict(df_train[cols])

test_predictions = clf.predict(df_test[cols])

train_accuracy = metrics.accuracy_score(
    df_train.quality , train_predictions
)


test_accuracy = metrics.accuracy_score(
    df_test.quality, test_predictions

)