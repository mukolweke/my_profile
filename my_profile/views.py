from django.shortcuts import render


def index_page(request):
    return render(request, 'my_profile/home_page.html', context=None)

