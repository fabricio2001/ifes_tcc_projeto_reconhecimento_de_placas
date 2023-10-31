import cv2
import datetime
from openalpr import Alpr
import numpy as np
import datetime

alpr = Alpr("br", "openalpr.conf", "runtime_data")
# url = "http://127.0.0.1:5000"
if not alpr.is_loaded():
    print("Error loading openalpr")
    sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("br")

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("resource/videos/1.mp4")
placaAtual = ""
try:
    while True:
        placa = np.ones((100, 400, 3)) * 255

        ret, img = cap.read()

        img_str = cv2.imencode('.jpg', img)[1].tostring()
        result = alpr.recognize_array(img_str)

        for plate in result["results"]:
            cv2.rectangle(img, (plate['coordinates'][0]['x'], plate['coordinates'][0]['y']),
                        (plate['coordinates'][1]['x'], plate['coordinates'][1]['y']), (255, 0, 0), 2)

            if (placaAtual != plate['plate']):
                placaAtual = plate['plate']
                registro = [
                    {"placa": plate['plate'], "direcao": 1, "data": datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')},
                ]
                print(registro)
                # requests.post(f"{url}/Registros/App", json=registro)
                

        # cv2.imshow("img", img)

        if cv2.waitKey(1) == 27:
            break
except Exception as e:
    # Código que será executado para qualquer outra exceção
    print(f"Ocorreu um erro: {e}")