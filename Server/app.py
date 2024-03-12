from flask import Flask, request, jsonify
from utils import *
from dbconnect import db_connect
from datetime import date

app = Flask(__name__)

# Khoi tao model
model = random_forest_model()

# Kiem tra ket noi co so du lieu
db = db_connect()
if db != None:
    print('Connect success.')
else:
    print('Can not connect to database.')
db.close()

# Cac route
# Lay danh sach cac benh nhan
@app.route('/api/patient', methods=['GET'])
def get_patient_list():
    patient_list = []
    db = db_connect()
    if db != None:
        cursor = db.cursor()
        query = 'SELECT patient_id, patient_name, patient_date_of_birth FROM patient_info'
        cursor.execute(query)
        for (patient_id, patient_name, patient_date_of_birth) in cursor:
            patient = {
                'patient_id': patient_id,
                'patient_name': patient_name,
                'patient_date_of_birth': patient_date_of_birth
            }
            patient_list.append(patient)
        cursor.close()
        db.close()
        return jsonify({'patient_list': patient_list})
    else:
        return jsonify({'error': 'Can not get patient list.'})

# Them mot benh nhan moi vao csdl 
@app.route('/api/patient', methods=['POST'])
def create_patient_info():
    input = request.get_json()
    response = dict()
    db = db_connect()
    if db != None:
        cursor = db.cursor()
        query = 'INSERT INTO patient_info (patient_name, patient_date_of_birth, patient_year_of_birth) VALUES (%s, %s, %s)'
        data = (input['name'], date(input['date_of_birth_year'], input['date_of_birth_month'], input['date_of_birth_date']), input['date_of_birth_year'])
        cursor.execute(query, data)
        emp_no = cursor.lastrowid
        print(emp_no)
        if emp_no != None:
            db.commit()
            cursor.close()
            response['error'] = None
        else:
            db.rollback()
            response['error'] = 'Can not create new patient.'
    else:
        response['error'] = 'Can not connect to database.'
    return jsonify(response)

# Du doan loai UTV
@app.route('/api/predict', methods=['POST'])
def predict():
    input = request.get_json()
    data = preprocess_data_input(input)
    predictions = get_class_value(model.predict([data]))
    response = {
        'predictions': predictions,
        'input': input
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
