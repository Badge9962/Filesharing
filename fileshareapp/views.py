from django.shortcuts import render
from .models import MyModel
from datetime import date
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')  # Handle file uploads via request.FILES
        if not file_path:
            return HttpResponse("No file uploaded.")

        # Generate a unique secret key
        secret_key = str(random.randint(1000, 9000))
        while MyModel.objects.filter(secret_key=secret_key).exists():
            secret_key = str(random.randint(1000, 9000))

        # Save the file and secret key
        today = date.today()
        add = MyModel.objects.create(upload=file_path, secret_key=secret_key, date_time=today)
        add.save()

        return HttpResponse(f'Thank you for saving your files and your secret_key is {secret_key}!')
    elif request.method == 'GET':
        return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        file_name = request.POST.get('key')
        if not file_name:
            return HttpResponse("No secret key provided.")

        try:
            file_search = MyModel.objects.get(secret_key=file_name)
        except MyModel.DoesNotExist:
            return HttpResponse(f"Not found {file_name}")
        except MyModel.MultipleObjectsReturned:
            return HttpResponse(f"Multiple entries found for {file_name}")

        return render(request, 'file.html', {'data': file_search})
    elif request.method == 'GET':
        return render(request, 'index.html')
