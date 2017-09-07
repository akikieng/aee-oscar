from oscar.apps.checkout import config


class CheckoutConfig(config.CheckoutConfig):
    name = 'oscar_override_apps.checkout'

    # https://stackoverflow.com/a/22924754/4126114
    def ready(self):
      super(CheckoutConfig,self).ready()
      from .signals import send_mail_on_save
      from oscar.apps.order.signals import order_placed
      order_placed.connect(send_mail_on_save)
