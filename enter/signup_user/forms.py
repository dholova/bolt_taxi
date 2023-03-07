from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import CustomUser


COUNT_CARS =(
    ("1", "1 - 10"),
    ("2", "11 - 25"),
    ("3", "26 - 50"),
    ("4", "51 - 100"),
    ("5", "101 - 500"),
    ("6", "501+"),
)
LANGUAGES =[
    ('af', 'Afrikaans'),
     ('ar', 'Arabic'),
     ('ar-dz', 'Algerian Arabic'),
     ('ast', 'Asturian'),
     ('az', 'Azerbaijani'),
     ('bg', 'Bulgarian'),
     ('be', 'Belarusian'),
     ('bn', 'Bengali'),
     ('br', 'Breton'),
     ('bs', 'Bosnian'),
     ('ca', 'Catalan'),
     ('cs', 'Czech'),
     ('cy', 'Welsh'),
     ('da', 'Danish'),
     ('de', 'German'),
     ('dsb', 'Lower Sorbian'),
     ('el', 'Greek'),
     ('en', 'English'),
     ('en-au', 'Australian English'),
     ('en-gb', 'British English'),
     ('eo', 'Esperanto'),
     ('es', 'Spanish'),
     ('es-ar', 'Argentinian Spanish'),
     ('es-co', 'Colombian Spanish'),
     ('es-mx', 'Mexican Spanish'),
     ('es-ni', 'Nicaraguan Spanish'),
     ('es-ve', 'Venezuelan Spanish'),
     ('et', 'Estonian'),
     ('eu', 'Basque'),
     ('fa', 'Persian'),
     ('fi', 'Finnish'),
     ('fr', 'French'),
     ('fy', 'Frisian'),
     ('ga', 'Irish'),
     ('gd', 'Scottish Gaelic'),
     ('gl', 'Galician'),
     ('he', 'Hebrew'),
     ('hi', 'Hindi'),
     ('hr', 'Croatian'),
     ('hsb', 'Upper Sorbian'),
     ('hu', 'Hungarian'),
     ('hy', 'Armenian'),
     ('ia', 'Interlingua'),
     ('id', 'Indonesian'),
     ('ig', 'Igbo'),
     ('io', 'Ido'),
     ('is', 'Icelandic'),
     ('it', 'Italian'),
     ('ja', 'Japanese'),
     ('ka', 'Georgian'),
     ('kab', 'Kabyle'),
     ('kk', 'Kazakh'),
     ('km', 'Khmer'),
     ('kn', 'Kannada'),
     ('ko', 'Korean'),
     ('ky', 'Kyrgyz'),
     ('lb', 'Luxembourgish'),
     ('lt', 'Lithuanian'),
     ('lv', 'Latvian'),
     ('mk', 'Macedonian'),
     ('ml', 'Malayalam'),
     ('mn', 'Mongolian'),
     ('mr', 'Marathi'),
     ('ms', 'Malay'),
     ('my', 'Burmese'),
     ('nb', 'Norwegian Bokmål'),
     ('ne', 'Nepali'),
     ('nl', 'Dutch'),
     ('nn', 'Norwegian Nynorsk'),
     ('os', 'Ossetic'),
     ('pa', 'Punjabi'),
     ('pl', 'Polish'),
     ('pt', 'Portuguese'),
     ('pt-br', 'Brazilian Portuguese'),
     ('ro', 'Romanian'),
     ('ru', 'Russian'),
     ('sk', 'Slovak'),
     ('sl', 'Slovenian'),
     ('sq', 'Albanian'),
     ('sr', 'Serbian'),
     ('sr-latn', 'Serbian Latin'),
     ('sv', 'Swedish'),
     ('sw', 'Swahili'),
     ('ta', 'Tamil'),
     ('te', 'Telugu'),
     ('tg', 'Tajik'),
     ('th', 'Thai'),
     ('tk', 'Turkmen'),
     ('tr', 'Turkish'),
     ('tt', 'Tatar'),
     ('udm', 'Udmurt'),
     ('uk', 'Ukrainian'),
     ('ur', 'Urdu'),
     ('uz', 'Uzbek'),
     ('vi', 'Vietnamese'),
     ('zh-hans', 'Simplified Chinese'),
     ('zh-hant', 'Traditional Chinese')
]

NUMBERS =(
    ("1", "Україна"),
)
CITY =(
    ("1", 'Dnipro'),
    ("2", 'Kyiv'),
    ("3", 'Lviv'),
    ("4", 'Lutsk'),
    ("5", 'Zaporizhzhia'),
    ("6", 'Zhytomyr'),
)
ENG_LANGUAGES =(
    ("1", "Ukrainian"),
    ("2", "English"),
    ("3", "Germany"),
)
BILLING_TYPE =(
    ("1", "Company"),
    ("2", "Person"),
)
VAT_LIABILITY =(
    ("1", "Company is VAT liable"),
    ("2", "Company is not VAT liable"),
)


class SignupForm(forms.ModelForm):
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'placeholder': 'imya.prizvyshche@gmail.com'}))
    phone = forms.CharField(label='Phone', max_length=20, required=False, widget= forms.TextInput(attrs={'placeholder': '+380501234567'}))
    car_in_fleet = forms.ChoiceField(label='car_in_fleet', choices=COUNT_CARS, widget=forms.Select(choices=COUNT_CARS))
    confirmed = forms.BooleanField(label='confirmed', required=True, widget=forms.CheckboxInput())
    language = forms.ChoiceField(label='language', choices=LANGUAGES, required=False, widget=forms.Select(choices=LANGUAGES))
    password = forms.CharField(label='password', widget= forms.PasswordInput(attrs={'placeholder': '********'}))
    class Meta:
        model = CustomUser
        fields = ['email', 'phone', 'car_in_fleet', 'confirmed', 'language']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'imya.prizvyshche@gmail.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+380501234567'}),
            'car_in_fleet': forms.Select(choices=COUNT_CARS),
            'confirmed': forms.CheckboxInput(),
            'language': forms.Select(choices=LANGUAGES),
            'password': forms.PasswordInput()
        }
    # class Meta:
    #     model = CustomUser
    #     fields = ['email', 'phone', 'car_in_fleet', 'confirmed', 'language']


class UserLoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}), max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())
    language = forms.ChoiceField(label='language', choices=LANGUAGES, required=False, widget=forms.Select(choices=LANGUAGES))

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if not '@' in email:
    #         raise forms.ValidationError('Invalid email address')
    #     return email
    #
    # def clean_password(self):
    #     password = self.cleaned_data['password']
    #     # Add password validation here
    #     return password

class ForgotPasswordForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'phone']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'imya.prizvyshche@gmail.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+380501234567'}),
        }


class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'city', 'language']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Doe'}),
            'city': forms.Select(choices=CITY),
            'language': forms.Select(choices=LANGUAGES),
        }


# class PaymentDetailsForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['billing_type', 'company_name', 'address', 'registration_code', 'vat_liability',
#                   'vat_number', 'bank_acc_holder_name', 'bank_acc', 'bic_swift', 'language']
#         widgets = {
#             'billing_type': forms.Select(choices=BILLING_TYPE),
#             'company_name': forms.TextInput(attrs={'placeholder': 'ABC Taxis Ltd'}),
#             'address': forms.TextInput(attrs={'placeholder': 'Хрещатик 1, Київ, 02000'}),
#             'registration_code': forms.TextInput(attrs={'placeholder': '12345678'}),
#             'vat_liability': forms.RadioSelect(choices=VAT_LIABILITY),
#             'vat_number': forms.TextInput(attrs={'placeholder': '1122334'}),
#             'bank_acc_holder_name': forms.TextInput(attrs={'placeholder': 'ABC Taxis Ltd / John Doe'}),
#             'bank_acc': forms.TextInput(attrs={'placeholder': 'UA123456789098765432'}),
#             'bic_swift': forms.TextInput(attrs={'placeholder': 'HABALT22'}),
#             'language': forms.Select(choices=LANGUAGES),
#         }

class DocumentsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['billing_type', 'language']
        widgets = {
            'billing_type': forms.Select(choices=BILLING_TYPE, attrs={'class': 'billing-type'}),
            'language': forms.Select(choices=LANGUAGES),

        }
class PaymentDetailsForm(forms.ModelForm):
    billing_type = forms.ChoiceField(choices=BILLING_TYPE, widget=forms.RadioSelect)
    company_name = forms.CharField(required=False)
    person_name = forms.CharField(required=False)
    address = forms.CharField(required=True)
    registration_code = forms.CharField(required=False)
    vat_liability = forms.BooleanField(required=False)
    vat_number = forms.CharField(required=False)
    bank_acc_holder_name = forms.CharField(required=True)
    bank_acc = forms.CharField(required=True)
    bic_swift = forms.CharField(required=True)


    class Meta:
        model = CustomUser
        fields = ['billing_type', 'company_name', 'person_name', 'address', 'registration_code', 'vat_liability',
                  'vat_number', 'bank_acc_holder_name', 'bank_acc', 'bic_swift']
        widgets = {
            'billing_type': forms.Select(choices=BILLING_TYPE, attrs={'class': 'billing-type'}),
            'company_name': forms.TextInput(attrs={'class': 'company-name', 'placeholder': 'ABC Taxis Ltd', 'required': False}),
            'person_name': forms.TextInput(attrs={'class': 'person-name', 'placeholder': 'John Doe'}),
            'address': forms.TextInput(attrs={'placeholder': 'Хрещатик 1, Київ, 02000'}),
            'registration_code': forms.TextInput(attrs={'placeholder': '12345678'}),
            'vat_liability': forms.RadioSelect(choices=VAT_LIABILITY),
            'vat_number': forms.TextInput(attrs={'placeholder': '1122334'}),
            'bank_acc_holder_name': forms.TextInput(attrs={'placeholder': 'ABC Taxis Ltd / John Doe'}),
            'bank_acc': forms.TextInput(attrs={'placeholder': 'UA123456789098765432'}),
            'bic_swift': forms.TextInput(attrs={'placeholder': 'HABALT22'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        billing_type = cleaned_data.get('billing_type')
        if billing_type == "Company":
            for field_name in ['company_name', 'address', 'registration_code', 'vat_liability']:
                if not cleaned_data.get(field_name):
                    self.add_error(field_name, 'This field is required for companies')
            for field_name in ['person_name']:
                if cleaned_data.get(field_name):
                    self.add_error(field_name, 'This field is not required for companies')
        elif billing_type == "Person":
            for field_name in ['person_name', 'address', 'bank_acc_holder_name', 'bank_acc', 'bic_swift', 'language']:
                if not cleaned_data.get(field_name):
                    self.add_error(field_name, 'This field is required for persons')
            for field_name in ['company_name', 'registration_code', 'vat_liability', 'vat_number']:
                if cleaned_data.get(field_name):
                    self.add_error(field_name, 'This field is not required for persons')
        return cleaned_data

# class PaymentDetailsForm(forms.Form):
#
    # billing_type = forms.Select(choices=BILLING_TYPE, attrs={'class': 'billing-type'})
    # company_name = forms.TextInput(attrs={'class': 'company-name', 'placeholder': 'ABC Taxis Ltd'})
    # person_name = forms.TextInput(attrs={'class': 'person-name', 'placeholder': 'John Doe'})
    # address = forms.TextInput(attrs={'placeholder': 'Хрещатик 1, Київ, 02000'})
    # registration_code = forms.TextInput(attrs={'placeholder': '12345678'})
    # vat_liability = forms.RadioSelect(choices=VAT_LIABILITY)
    # vat_number = forms.TextInput(attrs={'placeholder': '1122334'})
    # bank_acc_holder_name = forms.TextInput(attrs={'placeholder': 'ABC Taxis Ltd / John Doe'})
    # bank_acc = forms.TextInput(attrs={'placeholder': 'UA123456789098765432'})
    # bic_swift = forms.TextInput(attrs={'placeholder': 'HABALT22'})
    # language = forms.Select(choices=LANGUAGES)

from django import forms

# class PaymentDetailsForm(forms.Form):
#     BILLING_CHOICES = (
#         ('Company', 'Company'),
#         ('Person', 'Person')
#     )
#
#
#     billing_type = forms.Select(choices=BILLING_CHOICES, attrs={'class': 'billing-type'})
#     company_name = forms.TextInput(attrs={'class': 'company-name', 'placeholder': 'ABC Taxis Ltd'})
#     person_name = forms.TextInput(attrs={'class': 'person-name', 'placeholder': 'John Doe'})
#     address = forms.TextInput(attrs={'placeholder': 'Хрещатик 1, Київ, 02000'})
#     registration_code = forms.TextInput(attrs={'placeholder': '12345678'})
#     vat_liability = forms.RadioSelect(choices=VAT_LIABILITY)
#     vat_number = forms.TextInput(attrs={'placeholder': '1122334'})
#     bank_acc_holder_name = forms.TextInput(attrs={'placeholder': 'ABC Taxis Ltd / John Doe'})
#     bank_acc = forms.TextInput(attrs={'placeholder': 'UA123456789098765432'})
#     bic_swift = forms.TextInput(attrs={'placeholder': 'HABALT22'})
#     language = forms.Select(choices=LANGUAGES)
#     def clean(self):
#         cleaned_data = super().clean()
#         billing_type = cleaned_data.get('billing_type')
#         if billing_type == "Company":
#             for field_name in ['company_name', 'address', 'registration_code', 'vat_liability']:
#                 if not cleaned_data.get(field_name):
#                     self.add_error(field_name, 'This field is required for companies')
#             for field_name in ['person_name']:
#                 if cleaned_data.get(field_name):
#                     self.add_error(field_name, 'This field is not required for companies')
#         elif billing_type == "Person":
#             for field_name in ['person_name', 'address', 'bank_acc_holder_name', 'bank_acc', 'bic_swift', 'language']:
#                 if not cleaned_data.get(field_name):
#                     self.add_error(field_name, 'This field is required for persons')
#             for field_name in ['company_name', 'registration_code', 'vat_liability', 'vat_number']:
#                 if cleaned_data.get(field_name):
#                     self.add_error(field_name, 'This field is not required for persons')
