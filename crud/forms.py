from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['date_created']

class FilterListView(forms.Form):
    name = forms.CharField(required=False)
    order_by = forms.ChoiceField(choices = [('id', 'id')], label = 'Choose an order by option', required=False)


