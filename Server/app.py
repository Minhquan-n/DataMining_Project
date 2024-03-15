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
def get_all_patient():
    patient_list = []
    db = db_connect()
    if db != None:
        cursor = db.cursor()
        query = 'SELECT p.id, p.fullname, p.current_age, p.address, m.prediction FROM patient_info p LEFT JOIN medical_record m ON p.id = m.patientid ORDER BY m.update_at DESC'
        cursor.execute(query)
        for (id, fullname, curent_age, address, prediction) in cursor:
            patient = {
                'patient_id': id,
                'patient_name': fullname,
                'current_age': curent_age,
                'address': address,
                'prediction': prediction
            }
            patient_list.append(patient)
        cursor.close()
        db.close()
        return jsonify({'patient_list': patient_list})
    else:
        return jsonify({'error': 'Can not get patient list.'})
    
@app.route('/api/patient/nonpredict', methods=['GET'])
def get_all_patient_non_predict():
    patient_list = []
    db = db_connect()
    if db != None:
        cursor = db.cursor()
        query = 'SELECT p.id, p.fullname, p.current_age, p.address, m.prediction FROM patient_info p LEFT JOIN medical_record m ON p.id = m.patientid WHERE m.prediction is NULL ORDER BY m.update_at DESC'
        cursor.execute(query)
        for (id, fullname, curent_age, address, prediction) in cursor:
            patient = {
                'patient_id': id,
                'patient_name': fullname,
                'current_age': curent_age,
                'address': address,
                'prediction': prediction
            }
            patient_list.append(patient)
        cursor.close()
        db.close()
        return jsonify({'patient_list': patient_list})
    else:
        return jsonify({'error': 'Can not get patient list.'})
    
@app.route('/api/patient/recurrence', methods=['GET'])
def get_all_patient_recurrence():
    patient_list = []
    db = db_connect()
    if db != None:
        cursor = db.cursor()
        query = 'SELECT p.id, p.fullname, p.current_age, p.address, m.prediction FROM patient_info p LEFT JOIN medical_record m ON p.id = m.patientid WHERE m.prediction = "recurrence-events" ORDER BY m.update_at DESC'
        cursor.execute(query)
        for (id, fullname, curent_age, address, prediction) in cursor:
            patient = {
                'patient_id': id,
                'patient_name': fullname,
                'current_age': curent_age,
                'address': address,
                'prediction': prediction
            }
            patient_list.append(patient)
        cursor.close()
        db.close()
        return jsonify({'patient_list': patient_list})
    else:
        return jsonify({'error': 'Can not get patient list.'})
    
@app.route('/api/patient/norecurrence', methods=['GET'])
def get_all_patient_norecurrence():
    patient_list = []
    db = db_connect()
    if db != None:
        cursor = db.cursor()
        query = 'SELECT p.id, p.fullname, p.current_age, p.address, m.prediction FROM patient_info p LEFT JOIN medical_record m ON p.id = m.patientid WHERE m.prediction = "no-recurrence-events" ORDER BY m.update_at DESC'
        cursor.execute(query)
        for (id, fullname, curent_age, address, prediction) in cursor:
            patient = {
                'patient_id': id,
                'patient_name': fullname,
                'current_age': curent_age,
                'address': address,
                'prediction': prediction
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

        query_patient_info = 'INSERT INTO patient_info (fullname, date_of_birth, current_age, address, phone, create_at, update_at) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        data_patient_info = (input['name'], date(input['date_of_birth_year'], input['date_of_birth_month'], input['date_of_birth_date']),
                            date.today().year - input['date_of_birth_year'], input['address'],
                            input['phone'], datetime.now(), datetime.now())
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

# Lay tat ca thong tin cua benh nhan theo id
@app.route('/api/patient/<id>', methods=['GET'])
def get_patient_detail(id):
    response = dict()
    db = db_connect()
    if db != None:
        cursor = db.cursor()
        select_col = 'p.id, p.fullname, p.date_of_birth, p.current_age, p.address, m.age, m.menopause, m.tumor_size, m.inv_node, m.node_caps, m.deg_malig, m.breast, m.breast_quad, m.irradiar, m.prediction, m.medical_record_id, p.phone'
        query = f'SELECT {select_col} FROM patient_info p LEFT JOIN medical_record m ON p.id = m.patientid WHERE p.id = {id}'
        cursor.execute(query)
        for item in cursor:
            info = {
                'id': item[0],
                'fullname': item[1],
                'date_of_birth': item[2].strftime('%d/%m/%Y'),
                'current_age': item[3],
                'address': item[4],
                'age': item[5],
                'menopause': item[6],
                'tumor_size': item[7],
                'inv_nodes': item[8],
                'node_caps': item[9],
                'deg_malig': item[10],
                'breast': item[11],
                'breast_quad': item[12],
                'irradiat': item[13],
                'prediction': item[14],
                'medical_record_id': item[15],
                'phone': item[16]
            }
            response['patient_info'] = info
    return jsonify(response)

@app.route('/api/patient/medicalrecord/<mrid>', methods=['POST', 'PUT'])
def edit_medical_record(mrid):
    if request.method == 'POST':
        input = request.get_json()
        response = {'error': None}
        db = db_connect()
        if db != None:
            cursor = db.cursor()
            query = 'UPDATE medical_record SET menopause=%s, tumor_size=%s, inv_node=%s, node_caps=%s, deg_malig=%s, breast=%s, breast_quad=%s, irradiat=%s, update_at=%s WHERE medical_record_id = %s'
            data = (input['menopause'], input['tumor_size'], input['inv_node'], input['node_caps'], input['deg_malig'], input['breast'], input['breast_quad'], input['irradiat'], datetime.now(), mrid)
            cursor.execute(query, data)
            cursor.close()
        else:
            response['error'] = 'Can not connect to database.'
        db.close()
        return jsonify(response)
    elif request.method == 'PUT':
        input = request.get_json()
        response = {'error': None}
        db = db_connect()
        if db != None:
            cursor = db.cursor()
            query = 'UPDATE medical_record SET prediction=%s, note=%s, update_at=%s WHERE medical_record_id=%s'
            data = (input['prediction'], input['note'], datetime.now(), mrid)
            cursor.execute(query, data)
            cursor.close()
        else:
            response['error'] = 'Can not connect to database'
        db.close()
        return jsonify(response)

# Du doan loai UTV
@app.route('/api/predict', methods=['POST'])
def predict():
    input = request.get_json()
    data = preprocess_data_input(input)
    predictions = get_class_value(model.predict([data]))
    response = {
        'prediction': predictions
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
