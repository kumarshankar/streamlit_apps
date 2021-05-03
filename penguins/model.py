import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle


DATA_URL = "penguins_cleaned.csv"
target_mapper = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}

def load_data():
    data = pd.read_csv(DATA_URL)
    return data


def feature_encoding(df):
    target = 'species'
    encode = ['island', 'sex']
    for col in encode:
        dummy = pd.get_dummies(df[col], prefix=col)
        df = pd.concat([df,dummy], axis=1)
        del df[col]
    return df

def target_encode(val):
    return target_mapper[val]


if __name__ == "__main__":
    df = load_data()
    df = feature_encoding(df)
    df.species = df.species.apply(target_encode)
    X = df.drop('species', axis=1)
    Y = df['species']    
    clf = RandomForestClassifier()
    clf.fit(X, Y)
    # Saving the model
    pickle.dump(clf, open('penguins_clf.pkl', 'wb'))


    



