from django.urls import path
from apirestfile.views import ReadFileView, UploadFileCSV


app_name = "api"

urlpatterns = [
    path('', ReadFileView.as_view({'get': 'list'}), name='read'),
    path('upload/', UploadFileCSV.as_view(), name='upload'),
    
    

]
