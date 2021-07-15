# importing libraries for persorming the sentiment analysis, cleaning data, training and saving model

import pandas as pd
import math
import creme
import pickle
from sklearn.model_selection import train_test_split
from creme import metrics
from creme import compose
from creme import feature_extraction
from creme import naive_bayes
from textblob import TextBlob



def pred_senti(sentence):
    return model.predict_one(sentence)

# creme function

def retrain_mod(sentence, lable):
    model.fit_one(sentence, lable)



if __name__ == "__main__":
   
    # creme
    messages = pd.read_csv(r'amazonreviews.csv', sep=',',names=["label", "review"])
    message_train,message_test=train_test_split(messages)
    messages_train = message_train.to_records(index=False)
    messages_test=message_test.to_records(index=False)
    model = compose.Pipeline(
    ('tokenize', feature_extraction.TFIDF(lowercase=False)),
    ('nb', naive_bayes.MultinomialNB(alpha=1)))
    metric=metrics.Accuracy()
    for label,sentence in messages_train:
        model = model.fit_one(sentence, label)
        y_pred = model.predict_one(sentence)
        metric = metric.update(label, y_pred)
    print(metric)
    test_metric=metrics.Accuracy()
    for label,sentence in messages_test:
        y_pred = model.predict_one(sentence)
        test_metric = metric.update(label, y_pred)
    print(test_metric)
    print(pred_senti("i hate you"))
    
 

    with open( "creme_md.pickle", 'wb') as file:  
        pickle.dump(model, file)

    # Load the Model back from file
    with open( "creme_md.pickle", 'rb') as file:  
        Pickled_Model = pickle.load(file)

    print(Pickled_Model.predict_one(sentence))    