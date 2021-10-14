from django.urls import path

from account.views import rgisterLogin, logoutUser, profile, editProfilePersonalInfo, sendEmail, \
    resetPassword, deleteAddress, changeLang

app_name = 'account'
urlpatterns = [
    path('sign-in/', rgisterLogin, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit-personal-info/', editProfilePersonalInfo, name='edit-information'),
    path('send-email/<str:username>/', sendEmail, name='send-email'),
    path('reset-password/<str:token>/', resetPassword, name='reset-password'),

    path('change-lang/', changeLang, name='change-lang'),


    path('delete-address/<int:address_id>/', deleteAddress, name='delete-address')
]
