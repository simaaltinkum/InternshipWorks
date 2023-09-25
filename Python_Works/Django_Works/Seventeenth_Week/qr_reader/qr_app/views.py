from django.shortcuts import render
from pyzbar.pyzbar import decode
import cv2
from .models import Qr
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

                if obj.data != "":
                    print(obj.data)
                    print(obj.type)
                break

        except Exception as e:
            print("Barkod okuma hatası:", str(e))

        if data is not None:
            break

    cap.release()

    if data is not None:
        cv2.destroyAllWindows()

        qr = Qr(qr=data)
        qr.save()

        return render(request, 'qr_reader.html', {'data': data})

    else:
        cv2.destroyAllWindows()
        return render(request, 'no_qr_found.html')

def list(request):
    if request.method == 'POST':
        qr_data = Qr.objects.all()
        context = {
            'qr_data': qr_data
        }
        return render(request, 'qr_data.html', context)
    else:
        qr_data = Qr.objects.all()
        context = {
            'qr_data': qr_data
        }
        return render(request, 'qr_data.html', context)
