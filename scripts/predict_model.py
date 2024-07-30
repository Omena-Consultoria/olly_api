import pandas as pd
from catboost import CatBoostClassifier

import warnings
warnings.filterwarnings("ignore")

def train_and_predict_model(train_path, arr):
    # Importing dataset
    df = pd.read_excel(train_path)

    # Separating X (features) and Y (target)
    x = df.drop('modelo', axis=1)
    y = df['modelo']
    
    #Separating categorical features
    categorical_features = ['filme', 'musica', 'prefere', 'paisagem', 'esporte', 'cor', 'impressao',
       'fds', 'relaxar', 'se_considera']

    model = CatBoostClassifier(iterations=20,
                           learning_rate=0.8,
                           depth=3,
                           cat_features=categorical_features,
                           verbose=False,
                           allow_writing_files=False)
    
    # Fitting the model
    model.fit(x, y)
    
    # Importing the test dataset
    data_to_predict = arr
    
    # Operating Model
    predict = model.predict(data_to_predict)
    
    # Returning the result
    return predict[0][0]