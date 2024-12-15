import cv2
import time
#open cv либа для работы с изображениями
#чтение изображения
image_path = 'zazu.jpg'
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError("Файл zazu.jpg не найден")

#вывод изображения
cv2.imshow('Zazu', image)
cv2.waitKey() #Команда которая ждёт пока мы не нажмём какую то кнопку
print("wait")

time.sleep(3)

print("DESTROY")
cv2.destroyAllWindows()

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface.xml')

if cat_face_cascade.empty():
    raise FileNotFoundError("Файл haarcascade_frontalcatface не найден")

cat_faces = cat_face_cascade.detectMultiScale(gray_image)
print("Cat face coordinates :", cat_faces)

for(x,y,w,h) in cat_faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 3)

cv2.imshow("Прямоугольник", image)
cv2.waitKey()

from PIL import Image

cat = Image.open(image_path)
glasses = Image.open('glasses.png')
cat = cat.convert('RGBA')
glasses = glasses.convert('RGBA')

for (x,y,w,h) in cat_faces:
    glasses_recised = glasses.resize((w,int(h/3)))
    cat.paste(glasses_recised, (x,y + int(h/4)), glasses_recised)

output_path = "cat_with_glasses.png"
cat.save(output_path)
result = cv2.imread("cat_with_glasses.png")
cv2.imshow("O II A I AA OO II A I", result)
cv2.waitKey()

