from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Client
from .models import Pet

# class for sign up form that inherits user creation form
class SignUpForm(UserCreationForm):
    """
    Form for user sign up, inherits from UserCreationForm.

    Args:
        UserCreationForm (type): A built-in form for user registration.

    """
    # form fields
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
        )
    first_name = forms.CharField(
        label="", max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
        )
    last_name = forms.CharField(
        label="", max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
        )

    class Meta:
        """
        Metadata options for the SignUpForm.

        Attributes:
            model (Model): The model associated with this form.
            exclude (list): Fields to exclude from the form.

        """
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args: Any, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Repeat Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


# create new client form
class CreateClientForm(forms.ModelForm):
    """
    Form for creating a new client.

    Args:
        forms (type): The base class for Django forms.

    """
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
        attrs={"placeholder":"First Name", "class":"form-control"}), label="")
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
        attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.TextInput(
        attrs={"placeholder":"Email", "class":"form-control"}), label="")
    phone_number = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
        attrs={"placeholder":"Phone Number", "class":"form-control"}), label="")
    address = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
        attrs={"placeholder":"Address", "class":"form-control"}), label="")
    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
        attrs={"placeholder":"City", "class":"form-control"}), label="")
    state = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
        attrs={"placeholder":"State", "class":"form-control"}), label="")

    class Meta:
        """
        Metadata options for the CreateClientForm.

        Attributes:
            model (Model): The model associated with this form.
            exclude (list): Fields to exclude from the form.

        """
        model = Client
        exclude = ("user",)


# create pet form
class CreatePetForm(forms.ModelForm):
    """
    Form for creating a new pet.

    Args:
        forms (type): The base class for Django forms.

    """
    # choices for sex
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown')
    ]

    # choices for species
    SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Other', 'Other')
        # Add more species as needed
    ]

    # choices for breed (expand it)
    BREED_CHOICES = [
        ('Labrador Retriever', 'Labrador Retriever'),
        ('German Shepherd', 'German Shepherd'),
        ('Golden Retriever', 'Golden Retriever'),
        ('Mixed Breed', 'Mixed Breed'),
        ('Other', 'Other')
        # add more breeds
    ]

    name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Name", "class": "form-control"}),
        label="")
    birthday = forms.DateField(
        required=True,
        widget=forms.widgets.DateInput(attrs={"placeholder": "Birthday", "class": "form-control datepicker"}),
        label="")
    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Sex")
    species = forms.ChoiceField(
        choices=SPECIES_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Species")
    breed = forms.ChoiceField(
        choices=BREED_CHOICES,
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Breed")
    color = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(attrs={"placeholder": "Color", "class": "form-control"}),
        label="")


    class Meta:
        """
        Metadata options for the CreatePetForm.

        Attributes:
            model (Model): The model associated with this form.
            fields (list): Fields to include in the form.

        """
        model = Pet
        fields = ['name', 'birthday', 'species', 'breed', 'color', 'sex', 'pet_img']


# delete form
class DeleteForm(forms.Form):
    """
    Form for confirming deletion.

    Args:
        forms (type): The base class for Django forms.

    """
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your password'}), required=True)
    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm your password'}), required=True)

    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = ""
        self.fields['confirm_password'].label = ""
