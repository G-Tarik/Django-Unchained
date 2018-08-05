from django.shortcuts import render
from coolsite.settings import COOLSITE_APPS


def index(request):
    apps = [app.split('.')[0] for app in COOLSITE_APPS]
    context = {'apps_list': apps}

    return render(request, 'pages/index.html', context)
