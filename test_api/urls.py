from django.urls import path
from .views import CreateVieUser, FindVieUser

urlpatterns = [
    path('', CreateVieUser.as_view()),
    path('find/', FindVieUser.as_view())
]
