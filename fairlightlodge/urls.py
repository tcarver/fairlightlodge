from django.conf.urls import url

urlpatterns = [
    # Examples:
    # url(r'^$', 'fairlightlodge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'fairlightlodge.views.home', name='home'),
    url(r'^accommodation/$', 'fairlightlodge.views.accommodation', name='accommodation'),
    url(r'^tariff/$', 'fairlightlodge.views.tariff', name='tariff'),
    url(r'^reviews/$', 'fairlightlodge.views.reviews', name='reviews'),
    url(r'^breakfast/$', 'fairlightlodge.views.breakfast', name='breakfast'),
    url(r'^gallery/$', 'fairlightlodge.views.gallery', name='gallery'),
    url(r'^links/$', 'fairlightlodge.views.links', name='links'),
    url(r'^location/$', 'fairlightlodge.views.location', name='location'),
]
