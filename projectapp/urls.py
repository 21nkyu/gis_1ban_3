from django.urls import path

from projectapp.views import ProjectCreateView, ProjectDetailView, ProjectListView

app_name = 'projectapp' #이걸 해줘야 자동완성이 되고 reverse에 사용한다

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path('list/', ProjectListView.as_view(), name='list'),
]