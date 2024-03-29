from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage
import cv2
import base64
import io
import matplotlib.pyplot as plt
from django.core.files.base import ContentFile
import numpy as np
import os
from ultralytics import YOLO



def opencv_image_upload_success(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            
            # Upload Image
            nparr = np.fromstring(image_file.read(), np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # Load image directly from memory


            # Perform OpenCV processing here (e.g., resizing)
            bollard_cascade = cv2.CascadeClassifier('./trained_haarscascade/haarcascade_bollardv3.xml')
            height, width = img.shape[:2]
            # Resize the image while preserving the aspect ratio
            resized_down = cv2.resize(img, (400, 200), interpolation=cv2.INTER_AREA)
            gray = cv2.cvtColor(resized_down,cv2.COLOR_BGR2GRAY)
            bollards = bollard_cascade.detectMultiScale(gray, 1.01, 5)
            #print(bollards)
            for(x,y,w,h) in bollards:
                cv2.rectangle(resized_down, (x,y),(x+w,y+h),(255,0,0),2)
                print (x, y, w, h)

            resized_up = cv2.resize(resized_down, (width, height))
            resized_up = cv2.resize(resized_up, (400, int(400 / (width/height)) ))
            # Convert processed image to a base64-encoded string
            _, buffer = cv2.imencode('.png', resized_up, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
            img_str = base64.b64encode(buffer).decode()

            return render(request, 'image_upload/opencv_success.html', {'processed_image': img_str})

    else:
        form = ImageUploadForm()

    return render(request, 'image_upload/opencv_upload.html', {'form': form})

def opencv_image_upload(request):
    return render(request, 'image_upload/opencv_upload.html')


model_path = './bollard_yolo/runs/detect/train/weights/last.pt'
model = YOLO(model_path)  # load a custom model
threshold = 0.5
 

def yolo_image_upload_success(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_file = request.FILES['image']
            
            # Upload Image
            nparr = np.fromstring(image_file.read(), np.uint8)
            raw_img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)  # Load image directly from memory
            height, width = raw_img.shape[:2]
            img = cv2.resize(raw_img,(640,640),interpolation=cv2.INTER_AREA)

            # Perform inference on the image
            results = model(img)[0]
            conf = 0
            for result in results.boxes.data.tolist():
                x1, y1, x2, y2, conf, class_id = result
                if conf > threshold:
                    conf_score = round(conf, 2)
                    label = f"{results.names[int(class_id)]}: {conf_score}"
                    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                    cv2.putText(img, label, (int(x1), int(y1 - 10)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

            
            resized_down = cv2.resize(img, (400, int(400 / (width/height)) ))
            # Convert processed image to a base64-encoded string
            _, buffer = cv2.imencode('.png', resized_down)
            img_str = base64.b64encode(buffer).decode()

            return render(request, 'image_upload/yolo_success.html', {'processed_image': img_str})
    else:
        form = ImageUploadForm()

    return render(request, 'image_upload/yolo_upload.html', {'form': form})
def yolo_image_upload(request):
    return render(request, 'image_upload/yolo_upload.html')


