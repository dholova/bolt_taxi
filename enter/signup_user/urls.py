from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.generic import RedirectView

from . import views
urlpatterns = [
    path('order_panel/', views.order_panel, name='order_panel'),
    path('orders_history/', views.orders_history, name='orders_history'),
    path('live_map/', views.live_map, name='live_map'),
    path('car_park/', views.car_park, name='car_park'),
    path('drivers/', views.drivers, name='drivers'),
    path('cars/', views.cars, name='cars'),
    path('productivity_panel/', views.productivity_panel, name='productivity_panel'),
    path('validity_documents/', views.validity_documents, name='validity_documents'),
    path('payments/', views.payments, name='payments'),
    path('accounts/', views.accounts, name='accounts'),
    path('passenger_accounts/', views.passenger_accounts, name='passenger_accounts'),
    path('bolt_accounts/', views.bolt_accounts, name='bolt_accounts'),
    path('compensation_accounts/', views.compensation_accounts, name='compensation_accounts'),
    path('generated_files/', views.generated_files, name='generated_files'),
    path('actions/', views.actions, name='actions'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('day_rep/', views.day_reports, name='day_reports'),
    path('week_rep/', views.week_reports, name='week_reports'),
    path('pay_det/', views.payment_details, name='payment_details'),
    path('documents/', views.documents, name='documents'),
    path('personal_information/', views.personal_information, name='personal_information'),
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('', RedirectView.as_view(url='/home/', permanent=False), name='home'),

    # path('signup/', views.signup , name='signup')
]
