from django.http import HttpResponse 
from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect
from .forms import UploadFileForm

from .forms import *


def handle_uploaded_file(f,fname):
    with open('UploadedRetinaImages/%s' % fname , 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            print(fname)


def index(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'],request.FILES['file'].name)
            stage = predict_using_model(request.FILES['file'].name)
            print(request.FILES['file'].name)
            print(stage)
            return HttpResponseRedirect('result/%d/' % stage)
    else:
        form = UploadFileForm()
    return render(request, 'DRDetection/index.html', {'form': form})


def resultview(request,stage_id=-1):
	return render(request, 'DRDetection/result.html', {'stage_id':stage_id}) 


def samplewebpage(request):
	return HttpResponse("<h1>Diabetic Retinopathy Detection</h1>")


###################################################################################


from numpy import loadtxt
import tensorflow as tf
from keras.models import load_model
import cv2
import numpy as np


def predict_using_model(fname):
	model = tf.keras.models.load_model('tfkeras_model_01.h5')

	filepath = 'UploadedRetinaImages/%s'%fname
	image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
	newimage = cv2.resize(image,(64, 64),interpolation=cv2.INTER_AREA)
	X = newimage
	X = np.array(X).reshape(-1, 64, 64, 1)
	X = X/255.0
	classes = model.predict_classes(X)
	stage = classes[0][0]
	
	return stage