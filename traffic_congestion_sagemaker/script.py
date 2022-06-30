import argparse
import joblib
import os
import boto3
import time
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

#metrics
from sklearn import metrics
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

# inference functions ---------------
def model_fn(model_dir):
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf

if __name__ =='__main__':

    print('extracting arguments')
    parser = argparse.ArgumentParser()
    
    source_bucket = 'data-aman-use-case'

    # Data, model, and output directories
    parser.add_argument('--model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))

    args, _ = parser.parse_known_args()
    
    print('loading data from s3')
    s3 = boto3.client('s3')

    X_train = pd.read_csv('s3://' + bucket + '/X_train.csv')
    y_train = pd.read_csv('s3://' + bucket + '/y_train.csv')
    X_test = pd.read_csv('s3://' + bucket + '/x_test.csv')
    y_test = pd.read_csv('s3://' + bucket + '/y_test.csv')

    print('building training and testing datasets')

    # train
    tic = time.time()
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    
    toc = time.time()
    training_time = round(toc - tic, 4)
    print('took {} sec to train the model'.format(training_time))
    
    #make predictions
    y_pred = model.predict(X_test)
    toc2 = time.time()
    predict_time = round(toc2 - toc, 4)
    print('took {} sec to predict from the model'.format(predict_time))
    print('\n')
    
    #metrics
    score = round(model.score(X_test, y_test), 3)
    print('the score is : {}'.format(score))
    print('\n')
    cm = confusion_matrix(y_test, y_pred)
    print('Confusion Matrix:')
    print(cm)
    print('\n')
    print('Classification Report:')
    print(classification_report(y_test, y_pred))
    
    # persist model
    path = os.path.join(args.model_dir, "model.joblib")
    joblib.dump(model, path)
    print('model persisted at ' + path)