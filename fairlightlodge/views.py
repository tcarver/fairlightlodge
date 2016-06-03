''' Fairlight Lodge Views '''
from django.shortcuts import render


def home(request):
    ''' Renders a front page. '''
    return render(request, 'front_page.html', content_type='text/html')


def accommodation(request):
    ''' Renders a breakfast page. '''
    return render(request, 'accommodation.html', content_type='text/html')


def tariff(request):
    ''' Renders a tariff page. '''
    return render(request, 'tariff.html', content_type='text/html')


def reviews(request):
    ''' Renders a reviews page. '''
    return render(request, 'reviews.html', content_type='text/html')


def gallery(request):
    ''' Renders a gallery page. '''
    return render(request, 'gallery.html', content_type='text/html')


def breakfast(request):
    ''' Renders a breakfast page. '''
    return render(request, 'breakfast.html', content_type='text/html')


def links(request):
    ''' Renders a links page. '''
    return render(request, 'links.html', content_type='text/html')


def location(request):
    ''' Renders a location page. '''
    return render(request, 'location.html', content_type='text/html')
