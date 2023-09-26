from django.shortcuts import render
from pyzbar.pyzbar import decode
import cv2
from numpy import *
from cv2 import *
from .models import Qr
from .forms import QrForm
import uuid
import os

def homepage(request):
    return render(request, 'homepage.html')

def read_qr(request):
    cap = cv2.VideoCapture(0)
    data = None

    while data is None:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

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

            if ret:
                media_folder = "media"
                cv2.imshow("saved", frame)
                file_name = os.path.join(media_folder, f"savedcv_{str(uuid.uuid4())[:8]}.png")
                cv2.imwrite(file_name, frame)
                img = Qr(image= file_name)
                img.save()
                cv2.waitKey(0)
                cv2.destroyWindow("saved")
                break
                return render(request, 'qr_reader.html')

        except Exception as e:
            print("Barkod okuma hatası:", str(e))



        if data is not None:
            break

    cap.release()
    cv2.destroyAllWindows()

    if data is not None:
        cv2.destroyAllWindows()

        qr = Qr(qr=data)
        qr.save()

        return render(request, 'qr_reader.html', {'data': data})

    if data is not None:
        cv2.destroyAllWindows()

        try:
            qr = Qr.objects.get(qr=data)
            return render(request, 'qr_reader.html', {'data': qr.qr})
        except Qr.DoesNotExist:
            return render(request, 'no_qr_found.html')
    else:
        cv2.destroyAllWindows()
        return render(request, 'no_qr_found.html')


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

