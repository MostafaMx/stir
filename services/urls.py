from django.urls import path
from .views import sign_in, home, sign_up, meetingtime_view, service_detail, services_view, faq

urlpatterns = [
    path('home/', home, name='home_url'),
    path('sign-in/', sign_in, name='sign_in_url'),
    path('sign-up/', sign_up, name='sign_up_url'),
    path('meetingtime/', meetingtime_view, name='meetingtime_url'),
    path('services/', services_view, name='service_url'),
    path('servicedetail/<int:pk>/', service_detail, name='service_detail_url'),
    path('faq/', faq , name='faq_url')
]

 
