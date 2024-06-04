from django import forms
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control"},
        ),
        label="E-mail",
        required=True,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"},
        ),
        label="Password",
        required=True,
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        exist_email = get_user_model().objects.filter(email=email).exists()
        if not exist_email:
            raise forms.ValidationError(
                "This email is not exists in site. | Email is not found"
            )
        return email


class RegisterForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control"},
        ),
        label="E-mail",
        required=True,
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control"},
        ),
        label="Username",
        required=True,
        max_length=12,
        min_length=5,
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"},
        ),
        label="Password",
        required=True,
        min_length=6,
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control"},
        ),
        label="Password Confirm",
        required=True,
        min_length=6,
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        exists_email = get_user_model().objects.filter(email=email).exists()

        if exists_email:
            raise forms.ValidationError(
                "Email is not valid, please return another email."
            )
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        exists_username = get_user_model().objects.filter(username=username).exists()
        if exists_username:
            raise forms.ValidationError(
                "Username is not valid, please return another Username."
            )
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords in not match.")
        return password1
