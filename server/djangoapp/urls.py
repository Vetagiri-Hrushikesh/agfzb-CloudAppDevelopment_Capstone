from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
        path('static-template/', views.static_template_view, name='static_template'),
        path('about/', views.about_template_view, name='about'),
        path('contact/', views.contact_template_view, name='contact'),
        path(route='', view=views.get_dealerships, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


