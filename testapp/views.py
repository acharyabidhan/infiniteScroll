from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import os, base64, time, random
from pathlib import Path
#this is base directory of the entire project
baseDir = os.path.join(Path(Path(__file__).resolve().parent.parent))
#reading image data
def getImage():
    imagesList = os.listdir(f"{baseDir}/images")
    oneImage = random.choice(imagesList)
    imageData = open(f"{baseDir}/images/{oneImage}", "rb")
    imageData = imageData.read()
    imageData = base64.b64encode(imageData)
    imageData = imageData.decode("UTF-8")
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
