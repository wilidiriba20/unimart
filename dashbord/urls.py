from django.urls import path
from dashbord.views import dashbord  # your view function

app_name = 'dashbord'  # ✅ This sets the namespace

urlpatterns = [
    path('', dashbord, name='dashboard'),  # dashboard view
]