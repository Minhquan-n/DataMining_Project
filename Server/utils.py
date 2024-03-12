import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from datetime import date

def load_column_value_from_file():
    column_value = dict()
    with open('Server/data/data_column_value.txt', 'r') as f:
        for line in f.readlines():
            row = line.strip().split(':')
            column_value[row[0]] = row[1].split(',')
        f.close()
    return column_value

# Chuyen cac gia tri cua cot thanh cac so nguyen tuong ung
def convert_to_int_value(dataset, column_value):
    for col in dataset.columns:
        dataset[col] = dataset[col].map(lambda x: column_value[col].index(f'{x}'))
    
    return dataset

# Ham tao mo hinh du doan missing data. Mo hinh KNN duoc su dung cho viec du doan vi kha nang chiu nhieu tot
def predict_missing_data(features, labels):
    xtrain, xtest, ytrain, ytest = train_test_split(features, labels, random_state=42, shuffle=True, test_size=0.25)
    model = KNeighborsClassifier(n_neighbors=5, weights='distance')
    model.fit(xtrain, ytrain.values.ravel())
    pre = model.predict(xtest)
    print(accuracy_score(ytest, pre))
    print(precision_recall_fscore_support(ytest, pre))
    print(confusion_matrix(ytest, pre))

    return model

def random_forest_model():
    dataset = pd.read_csv('Server/data/processed_data.csv')
    features = dataset.iloc[:,1:]
    labels = dataset.Class
    
    model = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state=42, min_samples_leaf=1, max_depth=183)
    model.fit(features, labels)

    return model

def preprocess_data_input(data):
    column_value = load_column_value_from_file()
    return [
        column_value['age'].index(f'{data["age"]}'),
        column_value['menopause'].index(f'{data["menopause"]}'),
        column_value['tumor_size'].index(f'{data["tumor_size"]}'),
        column_value['inv_nodes'].index(f'{data["inv_nodes"]}'),
        column_value['node_caps'].index(f'{data["node_caps"]}'),
        column_value['deg_malig'].index(f'{data["deg_malig"]}'),
        column_value['breast'].index(f'{data["breast"]}'),
        column_value['breast_quad'].index(f'{data["breast_quad"]}'),
        column_value['irradiat'].index(f'{data["irradiat"]}')
    ]

def get_class_value(data):
    column_value = load_column_value_from_file()
    return column_value['Class'][data[0]]

def get_age(year):
    age = date.today().year - year
    if age >= 10 and age <= 19:
        return '10-19'
    elif age >= 20 and age <= 29:
        return '20-29'
    elif age >= 30 and age <= 39:
        return '30-39'
    elif age >= 40 and age <= 49:
        return '40-49'
    elif age >= 50 and age <= 59:
        return '50-59'
    elif age >= 60 and age <= 69:
        return '60-69'
    elif age >= 70 and age <= 79:
        return '70-79'
    elif age >= 80 and age <= 89:
        return '80-89'
    else:
        return '90-99'