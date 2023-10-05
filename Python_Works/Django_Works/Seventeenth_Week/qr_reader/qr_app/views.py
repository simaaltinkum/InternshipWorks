from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, reverse
from pyzbar.pyzbar import decode
from qr_reader.settings import  MEDIA_ROOT
from .models import Qr
from .forms import QrForm
from numpy import *
import cv2
import os
import uuid


def homepage(request):
    return render(request, 'homepage.html')


def read(request):
    cap = cv2.VideoCapture(0) # Open camera with openCV
    qr = None
    image = ''
    frame = None

    while qr is None: # If qr or barcode empty
        ret, frame = cap.read() # Returns boolean if the frame is read correctly, it will be true

        if ret:
            image = os.path.join(f"qr_{str(uuid.uuid4())[:8]}.png") # Naming the image which is photographed
            cv2.imwrite(MEDIA_ROOT + "/" + image, frame) # Saving the  image
            break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Conversion code

    try:
        decoded_objects = decode(gray) # Returns decoded string

        for obj in decoded_objects:
            qr = obj.data.decode('utf-8')
            (x, y, w, h) = obj.rect # Locating the barcode
            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2) #Highlight the barcode

            if obj.qr != "":
                print(obj.qr)
                print(obj.type)

    except Exception as e:
        print("Barcode reading fault:", str(e))

    cap.release() # Closing all windows
    cv2.destroyAllWindows()
    # return render(request,'read.html')

    if qr and image is not None:
        object = Qr.objects.create(qr =qr, image= image) # Saving decoded QR or Barcode code and image
        return HttpResponseRedirect(reverse('save', args=[object.pk])) # Directing saving page

    else:
        return HttpResponse('No QR or Barcode found')


def save(request, pk):
    if request.method == 'GET': # Informations comes when you in get request
        object = Qr(pk=pk)

        initial_dict = {
            'image': object.image,
            'qr': object.qr,
            'pk': pk
        }

        form = QrForm(initial= initial_dict)

        context = {
            'form': form,
            'image': object.image,
            'pk': pk
        }
    if request.method == 'POST': # Pk comes otomatically enter type
        form = QrForm(request.POST)

        if form.is_valid():
            pk = form.cleaned_data['pk']
            type = form.cleaned_data['type']

        object= Qr.objects.get(pk=pk)
        object.type = type
        object.save() # Type saving
        context = {}

    return render(request, 'save.html', context)


def search(request):
    if request.method == "POST":
        searched = request.POST['searched'] # Post what you want to search (qr, barcode or type)
        qr = Qr.objects.filter(qr = searched) # Qr query to equallity
        type = Qr.objects.filter(type = searched) # Type query to equallity
        return render(request, 'search.html', {'searched': searched, 'qr': qr, 'type': type})

    else:
        return render(request, 'search.html', {})


def list(request):
    qr_list = Qr.objects.all() #Retrieving data from database to list it

    context = {
        'qr_list': qr_list
    }
    return render(request, 'list.html', context)
