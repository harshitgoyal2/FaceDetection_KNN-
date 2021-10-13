import cv2
from mtcnn.mtcnn import MTCNN

detector = MTCNN()
img = cv2.imread('test.jpeg')
faces = detector.detect_faces(img)
for result in faces:
    x, y, w, h = result['box']
    x1, y1 = x + w, y + h
    img = cv2.rectangle(img, (x, y), (x1, y1), (0, 0, 255), 2)
