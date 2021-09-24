from django.urls import path

from account.views import rgisterLogin, logoutUser, profile, editProfilePersonalInfo, sendEmail, \
    resetPassword

app_name = 'account'
urlpatterns = [
    path('sign-in/', rgisterLogin, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit-personal-info/', editProfilePersonalInfo, name='edit-information'),
    # path('change-password/', changePassword, name='change-password'),
    path('send-email/<str:username>/', sendEmail, name='send-email'),
    path('reset-password/<str:token>/', resetPassword, name='reset-password'),
]
