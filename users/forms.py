from django import forms
from users.models import Outlet


class OutletForm(forms.ModelForm):
    class Meta:
        model = Outlet
        fields = [ 'outletname', 'foodtype', 'homedelivery', 'ownerfirstname',
                  'ownerlastname', 'address', 'addresslink', 'iframeaddress', 'email', 'phone', 'image']
