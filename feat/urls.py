from django.urls import path, include

from feat import views

app_name = 'feat'

urlpatterns = [
    path('', views.FeatListView.as_view(), name='list'),
    path('<tags>', views.FeatListView.as_view(), name='list'),
]