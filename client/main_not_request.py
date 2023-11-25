import cv2
import datetime
from openalpr import Alpr
import numpy as np
import datetime
import sys
import requests

if len(sys.argv) > 1:
    parametro = sys.argv[1]
    try:
        numero = int(parametro)
        if numero == 1 or numero == 2:
            print(f"Parâmetro válido: {numero}")
        else:
            print("Entrada inválida. Por favor, insira 1 ou 2.")
            sys.exit(1)
    except ValueError:
        print("Entrada inválida. Por favor, insira 1 ou 2.")
        sys.exit(1)

else:
    print("Nenhum parâmetro foi passado.")
    sys.exit(1)

alpr = Alpr("br", "openalpr.conf", "runtime_data")
url = "https://webhook.site/3ddb85d6-7a2b-48a4-81a4-0a41b3330122"
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

        img_str = cv2.imencode('.jpg', img)[1].tobytes()
        result = alpr.recognize_array(img_str)

        for plate in result["results"]:
            cv2.rectangle(img, (plate['coordinates'][0]['x'], plate['coordinates'][0]['y']),
                          (plate['coordinates'][1]['x'], plate['coordinates'][1]['y']), (255, 0, 0), 2)

            if (placaAtual != plate['plate']):
                placaAtual = plate['plate']
                registro = [
                    {"placa": plate['plate'], "accuracy": plate['confidence'], "direcao": parametro, "data": datetime.datetime.now(
                    ).strftime('%d/%m/%Y %H:%M:%S')},
                ]
                print(registro)
                response = requests.post(f"{url}/Registros/App", json=registro)
                if response.status_code == 200:
                    # Processar a resposta
                    print(response.json())  # Assumindo que a resposta é em JSON
                else:
                    print('Falha na requisição:', response.status_code)

        # cv2.imshow("img", img)

        if cv2.waitKey(1) == 27:
            break
except Exception as e:
    # Código que será executado para qualquer outra exceção
    print(f"Video finalizado.")
