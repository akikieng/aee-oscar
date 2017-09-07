# listen to checkout cart signal and send email to admin
# https://stackoverflow.com/a/39144765/4126114
from django.core.mail import send_mail
from django.conf import settings
def send_mail_on_save(order, user, **kwargs):
  # https://docs.djangoproject.com/en/1.11/topics/email/
  send_mail(
      'New order #'+str(order.number),
      'Made by user '+user.username,
      getattr(settings, 'OSCAR_FROM_EMAIL', 'from@example.com'),
      [getattr(settings, 'OSCAR_FROM_EMAIL', 'to@example.com')],
      fail_silently=False,
  )

