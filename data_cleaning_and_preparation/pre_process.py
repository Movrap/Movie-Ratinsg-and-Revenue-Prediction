from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import pandas as pd
import numpy as np

def encode_categorical_features(inputfilename):
    df = pd.read_csv(inputfilename)
    country = np.array(df["country"])
    #X = df.iloc[:,:].values


    label_enc = LabelEncoder()

    country_encoded = label_enc.fit_transform(country)

    onehot_enc = OneHotEncoder(sparse = False)

    country_encoded = country_encoded.reshape(len(country_encoded),1)

    onehot_encoded = onehot_enc.fit_transform(country_encoded)

    print(onehot_encoded)

'''
    df["country"] = label_enc.fit_transform(df["country"])
    onehot_enc = OneHotEncoder(categorical_features=[13])

    X = onehot_enc.fit(df["country"])
    print(X)

    return X
'''
