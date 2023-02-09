# Email_Sender-
Emails sending using Django. covering how to configure Django SMTP connections .
Using Django Environ to Hide Sensitive Keys : 
Even if you’re just sending emails in development, you shouldn’t write passwords directly into source code. This becomes even more important when using a version control system along with GitHub to host your project. You don’t want people to access your data.

Let’s see how we can prevent this by using Django-environ.

Create a .env file inside the EmailProject directory (where the settings.py file is located)

Breaking down the contents of this file:

EMAIL_HOST: your email provider SMTP server address. See the email host table above for quick guidance. In this case, I’m using smtp.gmail.com, the Gmail SMTP address.
EMAIL_HOST_USER: your email address.
EMAIL_HOST_PASSWORD: the app password you just generated. Have in mind it doesn’t include any spaces.
RECIPIENT_ADDRESS: the email address in which you’ll receive the messages. This is a custom setting that we’ll create later to send all the emails to the same recipient.
To make use of these environmental variables, we’ll need to install Django-environ with : pip install django-environ

