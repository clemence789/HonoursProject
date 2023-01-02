import pandas as pd
from sklearn.model_selection import train_test_split as tts


df = pd.read_csv(r'code\dataset1.csv', encoding='utf-8')

ml_df = df.filter(['Score', 'Text'], axis=1)
print(ml_df.shape)
print(ml_df.info())

#declaring feature vector and target variable
X = ml_df.drop(['Score'], axis = 1)
y = ml_df['Score']

#split dataset into 80 for training and 20 for testing
X_train, X_test, y_train, y_test = tts(X, y, test_size = 0.2, random_state = 0)
print(X_train.shape)
print(X_test.shape)

ml_df.to_csv(r'code\dataset2.csv')



#split the dataset by class values
#def separate_by_class(dataframe):
 #   separated = dict()
  #  for i in range(len(dataframe)):
   #     vector = dataframe[i]
    #    class_value = vector[-1]
     #   if(class_value not in separated):
      #      separated[class_value] = list()
       #     separated[class_value].append(vector)
    #return separated

#separated = separate_by_class(df)
#print(separated)