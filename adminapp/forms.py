from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.forms import HiddenInput

from authapp.forms import ShopUserChangeForm


class AdminShopUserUpdateForm(ShopUserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'password',
                  'email', 'age', 'avatar',
                  'is_staff', 'is_superuser', 'is_active')
