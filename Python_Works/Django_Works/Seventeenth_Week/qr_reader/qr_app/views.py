from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from pyzbar.pyzbar import decode
import cv2
from numpy import *
from qr_reader.settings import  MEDIA_ROOT
from .models import Qr
from .forms import QrSavingForm
import uuid
import os

def homepage(request):
    return render(request, 'homepage.html')


def read_qr(request):

    cap = cv2.VideoCapture(0)
    qr = None
    frame2 = None
    image = ''

    while qr is None:
        ret, frame = cap.read()
        if ret:
            frame2 = frame
            image = os.path.join(f"savedcv_{str(uuid.uuid4())[:8]}.png")
            cv2.imwrite(MEDIA_ROOT + "/" + image, frame)
            break

    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

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

    print("qr", qr)
    print("image", image)

    if qr and image is not None:
        obje = Qr.objects.create(image=image, qr=qr)
        return HttpResponseRedirect(reverse('save-qr', args=[obje.pk]))

    else:
        return HttpResponse("No QR code found")


def save_qr(request, pk):
    if request.method == "GET":
        obje = Qr(pk=pk)

        initial_dict = {
            "image": obje.image,
            "qr": obje.qr,
            "pk": pk
        }

        form = QrSavingForm(initial=initial_dict)

        context = {
            'form': form,
            'image': obje.image,
            "pk": pk
        }

    if request.method == "POST":
        form = QrSavingForm(request.POST)

        if form.is_valid():
            pk = form.cleaned_data["pk"]
            type = form.cleaned_data["type"]

        obje = Qr.objects.get(pk=pk)
        obje.type = type
        obje.save()
        context = {}

    return render(request, 'save_qr.html', context)


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        qr = Qr.objects.filter(qr = searched)
        type = Qr.objects.filter(type = searched)
        return render(request, 'search.html', {'searched': searched, 'qr': qr, 'type': type})

    else:
        return render(request, 'search.html', {})


def list(request):
    qr_data = Qr.objects.all()
    context = {
        'qr_data': qr_data
    }
    return render(request, 'qr_data.html', context)
