import json
from pathlib import Path

from client import sendToCloud
from nfc import get_id
from scale import save_json

height = raw_input("Enter your height : ")
age = raw_input("Enter your age : ")
sex = raw_input("Enter your sex : ")

while True:
    nfc_id = get_id()
    if not nfc_id == False:
        save_json()
        my_file = Path("scaleData.json")
        if my_file.is_file():
            with open('scaleData.json') as json_file:
                data = json.load(json_file)
            data2 = {
                "Student_Id" : nfc_id,
                "Body_metrics" : data
            }
            sendToCloud(data2)
            
