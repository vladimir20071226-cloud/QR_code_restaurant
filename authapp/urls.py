from django.urls import path
import authapp.views as views
app_name='auth'
urlpatterns=[
    path('google/', views.google_auth, name='login_google'),
    path('google/callback/', views.google_callback, name='google_callback')
             ]