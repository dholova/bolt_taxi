from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse

from .forms import SignupForm, UserLoginForm, PersonalInformationForm, PaymentDetailsForm, ForgotPasswordForm, \
    DocumentsForm
from .models import CustomUser


@login_required(login_url='/login/')
def my_profile(request):
    return render(request, 'menu/my_profile.html', {'title': 'My Profile'})


@login_required(login_url='/login/')
def order_panel(request):
    return render(request, 'menu/order_panel.html', {'title': 'Order panel'})


@login_required(login_url='/login/')
def orders_history(request):
    return render(request, 'menu/orders_history.html', {'title': 'Orders history'})


@login_required(login_url='/login/')
def live_map(request):
    return render(request, 'menu/live_map.html', {'title': 'Live map'})


@login_required(login_url='/login/')
def car_park(request):
    return render(request, 'menu/car_park.html', {'title': 'Car park'})


@login_required(login_url='/login/')
def drivers(request):
    return render(request, 'menu/drivers.html', {'title': 'Drivers'})


@login_required(login_url='/login/')
def cars(request):
    return render(request, 'menu/cars.html', {'title': 'Cars'})


@login_required(login_url='/login/')
def productivity_panel(request):
    return render(request, 'menu/productivity_panel.html', {'title': 'Productivity panel'})


@login_required(login_url='/login/')
def validity_documents(request):
    return render(request, 'menu/validity_documents.html', {'title': 'Validity documents'})


@login_required(login_url='/login/')
def payments(request):
    return render(request, 'menu/payments.html', {'title': 'Payments'})


@login_required(login_url='/login/')
def accounts(request):
    return render(request, 'menu/accounts.html', {'title': 'Accounts'})


@login_required(login_url='/login/')
def passenger_accounts(request):
    return render(request, 'menu/passenger_accounts.html', {'title': 'Passenger accounts'})


@login_required(login_url='/login/')
def bolt_accounts(request):
    return render(request, 'menu/bolt_accounts.html', {'title': 'Bolt accounts'})


@login_required(login_url='/login/')
def compensation_accounts(request):
    return render(request, 'menu/compensation_accounts.html', {'title': 'Compensation accounts'})


@login_required(login_url='/login/')
def generated_files(request):
    return render(request, 'menu/generated_files.html', {'title': 'Generated files'})


@login_required(login_url='/login/')
def actions(request):
    return render(request, 'menu/actions.html', {'title': 'Actions'})


def home(request):
    return render(request, 'menu/home.html', {'title': 'Home'})


@login_required(login_url='/login/')
def week_reports(request):
    return render(request, 'menu/week_reports.html', {'title': 'Тижневі звіти'})


@login_required(login_url='/login/')
def day_reports(request):
    return render(request, 'menu/day_reports.html', {'title': 'Щоденні звіти'})


def login_view(request):
    form = UserLoginForm()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password, backend='django.contrib.auth.backends.ModelBackend')

        # user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'login/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def forgot_password(request):
    form = ForgotPasswordForm()
    return render(request, 'login/forgot_password.html', {'form': form})


def documents(request):
       return render(request, 'signup/documents.html')


def signup(request):
    registration_id = request.session.get('registration_id')
    if not registration_id:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                registration_data = form.cleaned_data
                user = CustomUser.objects.create_user(
                    email=registration_data['email'],
                    password=registration_data['password'],
                    phone=registration_data['phone'],
                    car_in_fleet=registration_data['car_in_fleet'],
                    confirmed=registration_data['confirmed'],
                )
                user.save()
                registration_id = user.id
                request.session['registration_id'] = user.id

                # user = authenticate(request, email=registration_data['email'], password=registration_data['password'], backend='django.contrib.auth.backends.ModelBackend')
                # login(request, user, backend='django.contrib.auth.backends.ModelBackend')

                return redirect('personal_information')
        else:
            form = SignupForm()
        return render(request, 'signup/signup.html', {'form': form})
    else:
        return redirect('personal_information')


def personal_information(request):
    registration_id = request.session.get('registration_id')
    if not registration_id:
        return redirect('signup')

    registration = CustomUser.objects.get(id=registration_id)

    if request.method == 'POST':
        form = PersonalInformationForm(request.POST)
        if form.is_valid():
            registration_data = form.cleaned_data

            registration.first_name = registration_data['first_name']
            registration.last_name = registration_data['last_name']
            registration.city = registration_data['city']
            registration.language = registration_data['language']
            registration.save()
            return redirect('documents')

    else:
        form = PersonalInformationForm(initial={
                'first_name': registration.first_name,
                'last_name': registration.last_name,
                'city': registration.city,
                'language': registration.language
        })
    return render(request, 'signup/personal_information.html', {'form': form})


def payment_details(request):
    registration_id = request.session.get('registration_id')
    if not registration_id:
        return redirect('signup')

    registration = CustomUser.objects.get(id=registration_id)
    form = PaymentDetailsForm()

    if request.method == 'POST':
        form = PaymentDetailsForm(request.POST)

        if form.is_valid():
            billing_type = form.cleaned_data['billing_type']
            company_name = form.cleaned_data['company_name']
            person_name = form.cleaned_data['person_name']
            address = form.cleaned_data['address']
            registration_code = form.cleaned_data['registration_code']
            vat_liability = form.cleaned_data['vat_liability']
            vat_number = form.cleaned_data['vat_number']
            bank_acc_holder_name = form.cleaned_data['bank_acc_holder_name']
            bank_acc = form.cleaned_data['bank_acc']
            bic_swift = form.cleaned_data['bic_swift']
            language = form.cleaned_data['language']

            # update the user object with the payment details information
            registration.billing_type = billing_type
            registration.company_name = company_name
            registration.person_name = person_name
            registration.address = address
            registration.registration_code = registration_code
            registration.vat_liability = vat_liability
            registration.vat_number = vat_number
            registration.bank_acc_holder_name = bank_acc_holder_name
            registration.bank_acc = bank_acc
            registration.bic_swift = bic_swift
            registration.language = language
            registration.save()

            return redirect('login')

    return render(request, 'signup/payment_details.html', {'form': form})

