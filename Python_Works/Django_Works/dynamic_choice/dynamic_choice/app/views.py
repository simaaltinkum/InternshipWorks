from django.shortcuts import render
from django.http import JsonResponse
from .forms import MyForm, SaveForm
from .models import Category, SubCategory

def home(request):
    form = MyForm()
    context = {'form': form}
    return render(request, 'home.html', context)


def get_subcategories(request):
    if request.method == 'GET':
        category_id = request.GET.get('category_id')
        if category_id is not None:
            subcategories = SubCategory.objects.filter(category_id=category_id)
            subcategory_list = [{'id': sub.id, 'name': sub.name} for sub in subcategories]
            return JsonResponse({'subcategories': subcategory_list})
        else:
            return JsonResponse({'error': 'Category ID is missing'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET method is allowed'}, status=405)


def save_choices(request):
    if request.method == 'POST':
        form = SaveForm(request.POST)
        print("ssss")
        if form.is_valid():
            form.save()
            print("kaydedildi")
        else:
            print(form.errors)
    else:
        form = SaveForm()
        print("kkk")
    return render(request, 'home.html', {'form': form})
