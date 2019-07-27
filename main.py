import os
import subprocess
import json
import time
from pathlib import Path

from client import sendToCloud
from scale import save_json
from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *

pn532 = Pn532_i2c()
pn532.SAMconfigure()

while True:
    nfc_id = pn532.read_mifare().get_data()
    nfc_id = [hex(p) for p in nfc_id]    
    id = nfc_id[7] + nfc_id[8] + nfc_id[9] + nfc_id[10]
    id = id.replace('0x', '')
    nfc_id = id
    print(nfc_id)
#    save_json()
#    time.sleep(0.5) 
#    my_file = Path("scaleData.json")
#    if my_file.is_file():
#        with open('scaleData.json') as json_file:
#            data = json.load(json_file)
#        data2 = {
#            "Student_Id" : nfc_id,
#            "Body_metrics" : data
#        }
#        sendToCloud(data2)
#        print(data2)
#        os.remove("scaleData.json")
                    


