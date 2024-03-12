from flask import Flask, request, jsonify
from utils import *
from dbconnect import db_connect
from datetime import date, datetime

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
        query = 'SELECT id, fullname, date_of_birth, address FROM patient_info'
        cursor.execute(query)
        for (id, fullname, date_of_birth, address) in cursor:
            patient = {
                'patient_id': id,
                'patient_name': fullname,
                'patient_date_of_birth': date_of_birth.strftime('%d/%m/%Y'),
                'patient_address': address
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

        query_patient_info = 'INSERT INTO patient_info (fullname, date_of_birth, address, create_at, update_at) VALUES (%s, %s, %s, %s, %s)'
        data_patient_info = (input['name'], date(input['date_of_birth_year'], input['date_of_birth_month'], input['date_of_birth_date']), input['address'], datetime.now(), datetime.now())
        cursor.execute(query_patient_info, data_patient_info)
        new_patient_id = cursor.lastrowid
        if new_patient_id != None:
            query_medical_record = 'INSERT INTO medical_record (patientid, age, create_at, update_at) VALUES (%s, %s, %s, %s)'
            data_medical_record = (new_patient_id, get_age(input['date_of_birth_year']), datetime.now(), datetime.now())
            cursor.execute(query_medical_record, data_medical_record)
            
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
