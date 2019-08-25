from django.shortcuts import render


def home_page(request):
    return render(request, 'job_app/home_page.html')
