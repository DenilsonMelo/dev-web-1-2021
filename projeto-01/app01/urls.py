from django.urls import path
from .views import index, w3c, html, css, javascript, backend, frontend

urlpatterns = [
    path('', index, name="index"),
    path('w3c', w3c, name="w3c"),
    path('html', html, name="html"),
    path('css', css, name="css"),
    path('javascript', javascript, name="javascript"),
    path('backend', backend, name="backend"),
    path('frontend', frontend, name="frontend"),
]