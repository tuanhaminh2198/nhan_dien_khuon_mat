import cv2
import numpy as np
import os
from PIL import Image


recognizer =  cv2.face.LBPHFaceRecognizer_create()

path = r'C:\Users\Ha Minh Tuan\PycharmProjects\nhandien\nhan_dien_khuon_mat\luu_anh\dataSet'
def getImageWithId(path):
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for imagePath in imagePaths:
        faceImg = Image.open(imagePath).convert('L')
        faceNp = np.array(faceImg,'uint8')

        Id = int(imagePath.split('\\')[8].split('.')[1])
        faces.append(faceNp)
        IDs.append(Id)


        cv2.imshow('training', faceNp)
        cv2.waitKey(10)
    return faces, IDs
faces,IDs = getImageWithId(path)
recognizer.train(faces, np.array(IDs))
if not os.path.exists('recognizer'):
    os.mkdir('recognizer')
    recognizer.save('recognizer/trainingData.yml')
cv2.destroyAllWindows()