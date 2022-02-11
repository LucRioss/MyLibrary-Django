from unicodedata import name
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views

app_name = 'books'


urlpatterns = [
    path('', views.index, name='index'),
    path('livros/create', views.LivrosCreate.as_view(), name='create'),
    path('livros/update/<int:pk>', views.LivrosUpdate.as_view(), name='update'),
    path('livros/detail/<int:pk>', views.LivrosDetailView.as_view(), name='detail'),
    path('livros/list', views.LivrosList.as_view(), name='list'),
    path('livros/delete/<int:pk>', views.LivrosDelete.as_view(), name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)