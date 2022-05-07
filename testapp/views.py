from itertools import count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import os, base64, time, random
from pathlib import Path
#this is base directory of the entire project
baseDir = os.path.join(Path(Path(__file__).resolve().parent.parent))
#reading image data

count = 0

def getIndex():
    global count
    count = count + 1
    if count == 29:
        count = 0
    return count

def getImage():
    binImageList = []
    imagesList = os.listdir(f"{baseDir}/images")
    for image in imagesList:
        with open(f"{baseDir}/images/{image}", "rb") as img:
            imageData = img.read()
            imageData = base64.b64encode(imageData)
            imageData = imageData.decode("UTF-8")
        binImageList.append(imageData)
    imageData = binImageList[getIndex()]
    return imageData

def load(request):
    image = {
        "image":f"""
            <img src="data:image;charset=utf-8;base64,{getImage()}" alt="image" height=90% width=90%>
        """
    }
    return JsonResponse(image, safe=False)

def index(request):
    return render(request, "index.html")
