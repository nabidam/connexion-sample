from flask import Flask, jsonify, Response
from flask_cors import CORS

from connexion import FlaskApp

import random
import string

PARAMETER_TYPES = ["TextBox", "CheckBox",
                   "ComboBox", "DateTime", "TextTLE", "RadioButton"]


def random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))


def generate_command():
    return {
        "idCommand": random.randint(1, 1000),
        "commandName": random_string(10),
        "obcid": random_string(6),
        "lenght": random.randint(1, 500),
        "isEnabled": random.choice([True, False]),
        "moduleId": random.randint(1, 100)
    }


def generate_module():
    return {
        "idModule": random.randint(1, 100),
        "moduleName": random_string(8),
        "obcid": random_string(6),
        "subsystemId": random.randint(1, 50)
    }


def generate_subsystem():
    return {
        "idSubsystem": random.randint(1, 50),
        "subsystemName": random_string(8),
        "obcid": random_string(6),
        "satelliteId": random.randint(1, 10)
    }


def generate_satellite():
    return {
        "idSatellite": random.randint(1, 10),
        "obcid": random_string(6),
        "satelliteName": random_string(8)
    }


def generate_value():
    return {
        "idValue": random.randint(1, 1000),
        "text": random_string(10),
        "value": random_string(5),
        "parameterVisible": random.choice([True, False]),
        "parametersId": random.randint(1, 500)
    }


def generate_parameter():
    return {
        "idParameters": random.randint(1, 500),
        "parameterNumber": random.randint(1, 1000),
        "labelName": random_string(10),
        "defaultValue": random_string(6),
        "formula": random_string(8),
        "minValue": str(random.uniform(0, 10)),
        "maxValue": str(random.uniform(10, 100)),
        "commandId": random.randint(1, 1000),
        "parameterTypeId": random.randint(1, 7),
        "valueTypeId": random.randint(1, 20),
        "values": [generate_value() for _ in range(random.randint(1, 5))]
    }


def generate_parameter_type():
    return [{
        "idParameterType": idx+1,
        "type": t
    } for idx, t in enumerate(PARAMETER_TYPES)]

def generate_stations():
    return [{
        "idStation": idx+1,
        "stationName": random_string(),
        "iPAddress": generate_random_ip()
    } for idx in range(10)]

def generate_settings():
    return [{
        "KeyData": random_string(),
        "ValueData": random_string(),
    } for _ in range(10)]

app = FlaskApp(__name__, specification_dir='./')

CORS(app.app, supports_credentials=True, origins=["*"])

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.json')

# @app.before_request
# def basic_authentication():
#     if request.method.lower() == 'options':
#         return Response()

@app.route('/')
def home():
    return "Mock Server is running!"


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


def GetCommandWithModuleID():
    return jsonify([generate_command() for _ in range(random.randint(1, 10))])


def GetModuleWithSubSystemID():
    return jsonify([generate_module() for _ in range(random.randint(1, 10))])


def GetParameterWithCommandID():
    return jsonify([generate_parameter() for _ in range(random.randint(1, 10))])


def GetAllParameterTypes():
    return jsonify(generate_parameter_type())


def GetAllSatellites():
    return jsonify([generate_satellite() for _ in range(random.randint(1, 10))])


def GetSubsystemWithSatelliteID():
    return jsonify([generate_subsystem() for _ in range(random.randint(1, 10))])


def PrefligtStations():
    return jsonify({
        "description": "OK"
    })
    
def GetAllStations():
    return jsonify(generate_stations())

def InsertStation():
    return jsonify({
        "description": "OK"
    })

def UpdateStation():
    return jsonify({
        "description": "OK"
    })

def DeleteStation():
    return jsonify({
        "description": "OK"
    })
    

def PrefligtSettings():
    return jsonify({
        "description": "OK"
    })    

def GetSettingWithKey():
    return jsonify(generate_settings())

def GetAllSettings():
    return jsonify(generate_settings())

def InsertSetting():
    return jsonify({
        "description": "OK"
    })

def UpdateSetting():
    return jsonify({
        "description": "OK"
    })

def DeleteSetting():
    return jsonify({
        "description": "OK"
    })