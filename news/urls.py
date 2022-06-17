from django.urls import path
# Импортируем созданное нами представление
from .views import NewsList, PostSearch, PostDetail, PostCreate, PostEdit, PostDelete


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
    path('', NewsList.as_view()),
    path('search/', PostSearch.as_view(), name='search'),
    path('<int:pk>', PostDetail.as_view()),
    path('create/', PostCreate.as_view(), name='post_create'),
    #path('create/', PostCreate, name='post_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]