import cv2
import datetime
from openalpr import Alpr
import numpy as np
import datetime
import os

def get_plate_value(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if 'plate:' in line:
            _, value = line.split(':')
            return value.strip()

    return None  # Retorna None se não encontrar um valor de placa


alpr = Alpr("br", "openalpr.conf", "runtime_data")
if not alpr.is_loaded():
    print("Error loading openalpr")
    sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("br")
directory_path_inicial = r"F:\UFPR-ALPR dataset"

total_img_test = 0
total_img_correct = 0
total_img_seach = 0

subdirectories = [d for d in os.listdir(directory_path_inicial) if os.path.isdir(os.path.join(directory_path_inicial, d))]

for directory in subdirectories:
    print(directory)
    if(directory):
        directory_path_meio = directory_path_inicial + "/" + directory
        sub_subdirectories = [d for d in os.listdir(directory_path_meio) if os.path.isdir(os.path.join(directory_path_meio, d))]
        for sub_directory in sub_subdirectories:
            # print(sub_directory)
            directory_path_final = directory_path_meio + "/" + sub_directory
            all_files = os.listdir(directory_path_final)
            
            png_files = [file for file in all_files if file.endswith('.png')]
            files_without_extension = [os.path.splitext(file)[0] for file in png_files]
            exist = False
            for file in files_without_extension:
                # print(file)
                if (exist):
                    break
                file_path = directory_path_final + "/" + file 
                img_path = file_path + ".png"
                txt_path = file_path + ".txt"
                plate_value = get_plate_value(txt_path)
                image = cv2.imread(img_path)
                success, encoded_image = cv2.imencode('.jpg', image)  # Codifica a imagem em formato PNG
                if not success:
                    print("Error encoding the image")
                    sys.exit(1)

                byte_array = encoded_image.tobytes()  # Converte o array numpy em byte array

                result = alpr.recognize_array(byte_array)

                total_img_test += 1

                for plate in result["results"]:
                    total_img_seach += 1
                    if(plate['plate'] == plate_value.replace("-", "")):
                        print(sub_directory + " -> " + plate['plate'] + " = " + plate_value)
                        # exist = True
                        total_img_correct += 1

print("Total de imagens testadas: " + str(total_img_test))
print("Total de imagens corretas: " + str(total_img_correct))
print("Total de imagens pesquisadas: " + str(total_img_seach))


