from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from SOLIDIFY.accounts.models import Profile
from SOLIDIFY.utils import helptext_to_ul

UserModel = get_user_model()


from django import forms
from django.contrib.auth.forms import AuthenticationForm

class AppUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter your email address'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter your password'})


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        raw_help = (
            "Your password must contain at least 8 characters and can’t be too similar to your other personal information.\n"
            "Your password can’t be entirely numeric or a commonly used one."
        )
        raw_help2 = (
            "Enter the same password again for verification."
        )
        self.fields['password1'].help_text = helptext_to_ul(raw_help)
        self.fields['password2'].help_text = helptext_to_ul(raw_help2)


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel
        fields = '__all__'

from django import forms
from .models import Profile

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First name (optional)'
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last name (optional)'
            }),
            'age': forms.TextInput(attrs={
                'placeholder': 'Your age (optional, e.g. 28)',
            }),
            'profile_picture': forms.URLInput(attrs={
                'placeholder': 'Profile picture URL (optional, e.g. https://...)'
            }),
        }

