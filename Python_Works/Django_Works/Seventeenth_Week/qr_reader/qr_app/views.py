from django.shortcuts import render
from pyzbar.pyzbar import decode
import cv2
from numpy import *
from qr_reader.settings import  MEDIA_ROOT
from .models import Qr
from .forms import QrForm
import uuid
import os


def homepage(request):
    return render(request, 'homepage.html')

def read_qr(request):
    cap = cv2.VideoCapture(0)
    data = None

    frame2 = None
    object = Qr()

    while data is None:
        ret, frame = cap.read()
        if ret:
            frame2 = frame
            file_name = os.path.join(f"savedcv_{str(uuid.uuid4())[:8]}.png")
            cv2.imwrite(MEDIA_ROOT + "/" + file_name, frame)

            object.image = file_name
            object.save()
            break

    print("cikis")
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    try:
        decoded_objects = decode(gray)

        for obj in decoded_objects:
            data = obj.data.decode('utf-8')
            (x, y, w, h) = obj.rect
            cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
            print("barkod")

            if obj.data != "":
                print(obj.data)
                print(obj.type)

    except Exception as e:
        print("Barkod okuma hatası:", str(e))

    cap.release()
    cv2.destroyAllWindows()

    if data is not None:
        object.qr = data
        object.save()
        print("aaa")
        return render(request, 'qr_reader.html', {'data': data, 'object': object})
    else:
        print("bbb")
        return render(request, 'qr_reader.html')

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']

        return render(request, 'search.html', {'searched': searched})
def type(request):
    if request.method == 'POST':
        form = QrForm(request.POST)
        if form.is_valid():
            form.save()
            print("form kaydedildi")
            return render(request, 'type.html')
        else:
            print("form geçerli değil")
    else:
        form = QrForm()
        print("form kaydedilmedi")

    return render(request, 'type.html')

def list(request):
    qr_data = Qr.objects.all()
    context = {
        'qr_data': qr_data
    }
    return render(request, 'qr_data.html', context)

