from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import UploadedImage

import cv2
import base64
import io
import matplotlib.pyplot as plt
from django.core.files.base import ContentFile

def image_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Process the uploaded image using OpenCV 

            uploaded_image = UploadedImage.objects.latest('id')
            image_path = uploaded_image.image.path
            img = cv2.imread(image_path) #path of image file which we want to detect

            # Perform OpenCV processing here (e.g., resizing)
            bollard_cascade = cv2.CascadeClassifier('./trained_haarscascade/haarcascade_bollardv3.xml')
            resized = cv2.resize(img,(400,200))
            resized = img
            gray=cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
            bollards = bollard_cascade.detectMultiScale(gray,1.01, 10)
            #print(bollards)
            for(x,y,w,h) in bollards:
                cv2.rectangle(resized,(x,y),(x+w,y+h),(255,0,0),2)
                print (x, y, w, h)

            # cv2.imshow('img',resized)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            # Save the processed image
            # cv2.imwrite(image_path, img)
            
            # Convert processed image to a base64-encoded string
            _, buffer = cv2.imencode('.png', img)
            img_str = base64.b64encode(buffer).decode()

            return render(request, 'image_upload/success.html', {'processed_image': img_str})

            #return redirect('image_upload_success')
    else:
        form = ImageUploadForm()

    return render(request, 'image_upload/upload.html', {'form': form})

def image_upload_success(request):
    return render(request, 'image_upload/success.html')


