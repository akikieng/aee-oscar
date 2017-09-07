# http://django-oscar.readthedocs.io/en/releases-1.1/topics/customisation.html
from oscar.apps.checkout.forms import ShippingAddressForm as CoreShippingAddressForm
from oscar.core.loading import get_model

class ShippingAddressForm(CoreShippingAddressForm):
  class Meta:
    model = get_model('order', 'shippingaddress')
    fields = [
        # 'title',
        'first_name', 'last_name',
        'country',
        'line4', # line4 = city
        'line1', # 'line2', 'line3',
        #'state', 'postcode',
        'phone_number',
        #'notes',
    ]

