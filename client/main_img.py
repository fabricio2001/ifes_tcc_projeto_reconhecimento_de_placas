import cv2
import datetime
from openalpr import Alpr
import numpy as np
import requests
import datetime
import json
import sys

alpr = Alpr("br", "openalpr.conf", "runtime_data")
url = "http://127.0.0.1:5000"
filename = 'roi/roi.jpg'
if not alpr.is_loaded():
    print("Error loading openalpr")
    sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("br")

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture("resource/videos/1.mp4")
placaAtual = ""
while True:
    placa = np.ones((100, 400, 3)) * 255

    ret, img = cap.read()

    img_str = cv2.imencode('.jpg', img)[1].tostring()
    result = alpr.recognize_array(img_str)

    for plate in result["results"]:
        coordenadas = plate['coordinates']
        x1, y1 = coordenadas[0]['x'], coordenadas[0]['y']
        x2, y2 = coordenadas[2]['x'], coordenadas[2]['y']
        cv2.rectangle(img, (x1, y1),
                      (x2, y2), (255, 0, 0), 2)
        roi = img[y1:y2, x1:x2]
        cv2.imwrite('roi/roi.jpg', roi)
        if (placaAtual != plate['plate']):
            placaAtual = plate['plate']
            registro = [
                {"placa": plate['plate'], "direcao": 1, "data": datetime.datetime.now(
                ).strftime('%d/%m/%Y %H:%M:%S')},
            ]
            # print(registro)
            json_data = json.dumps(registro)
            print(json_data)
            with open(filename, 'rb') as image:
                response = requests.post(
                    f"{url}/Registros/App", files={"image": image}, data={"json_field": json_data})
            #requests.post(f"{url}/Registros/App", json=registro)

    cv2.imshow("img", img)

    if cv2.waitKey(1) == 27:
        break
