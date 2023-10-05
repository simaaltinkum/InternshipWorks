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
    cap = cv2.VideoCapture(0)
    qr = None
    image = ''
    frame = None

    while qr is None:
        ret, frame = cap.read()

        if ret:
            image = os.path.join(f"qr_{str(uuid.uuid4())[:8]}.png")
            cv2.imwrite(MEDIA_ROOT + "/" + image, frame)
            break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    try:
        decoded_objects = decode(gray)

        for obj in decoded_objects:
            qr = obj.data.decode('utf-8')
            (x, y, w, h) = obj.rect
            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)

            if obj.qr != "":
                print(obj.qr)
                print(obj.type)

    except Exception as e:
        print("Barcode reading fault:", str(e))

    cap.release()
    cv2.destroyAllWindows()
    # return render(request,'read.html')

    if qr and image is not None:
        object = Qr.objects.create(qr =qr, image= image)
        return HttpResponseRedirect(reverse('save', args=[object.pk]))

    else:
        return HttpResponse('No QR or Barcode found')


def save(request, pk):
    if request.method == 'GET':
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
    if request.method == 'POST':
        form = QrForm(request.POST)

        if form.is_valid():
            pk = form.cleaned_data['pk']
            type = form.cleaned_data['type']

        object= Qr.objects.get(pk=pk)
        object.type = type
        object.save()
        context = {}

    return render(request, 'save.html', context)


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        qr = Qr.objects.filter(qr = searched)
        type = Qr.objects.filter(type = searched)
        return render(request, 'search.html', {'searched': searched, 'qr': qr, 'type': type})

    else:
        return render(request, 'search.html', {})


def list(request):
    qr_list = Qr.objects.all()

    context = {
        'qr_list': qr_list
    }
    return render(request, 'list.html', context)
