import cv2
from pyzbar.pyzbar import decode
import time
import gspread
gc = gspread.service_account(filename='client-access.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/14dQbkV9JTxp9PjsEdqp0d7Gw4THIil1p0lEQOqicuSI/edit?usp=sharing')
worksheet = sh.worksheet("Sheet2")


cap = cv2.VideoCapture(0)
cap.set(3,640) #Widgth
cap.set(4,480) #Height
valid_ids = []
used_ids = []

camera = True
while camera == True:
    success, frame = cap.read()

    for code in decode(frame):
        if code.data.decode('utf-8') not in used_ids:
            print("Approved. You may Enter!")
            print(code.data.deode('utf-8'))
            used_ids.append(code.data.deode('utf-8'))
            worksheet.update("A2",code.data.decode('utf-8'))
            time.sleep(5)

        elif code.data.deode('utf-8') in used_ids:
            print("Sorry, this ID has already been used")
            time.sleep(5)
        else:
            pass
    cv2.imshow("Testing-code-scan",frame)
    cv2.waitKey(1)
