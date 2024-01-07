from django.urls import path
from .views import bloghtml, abouthtml, contact, home



urlpatterns = [
    path('blog/', bloghtml),
    path('', abouthtml),
    path('contact/', contact),
    path('home/', home)
]