import jwt,datetime
from rest_framework import exceptions
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def createAccessToken(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
        'ist': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    }, 'access_secret', algorithm='HS256')

def decodeAccessToken(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256' )

        return payload['user_id']

    except:
        raise exceptions.AuthenticationFailed('unauthenticated')

def createRefreshToken(id):
    return jwt.encode({
        'user_id': id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'ist': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    }, 'refresh_secret', algorithm='HS256')


def decodeRefreshToken(token):
    try:
        payload = jwt.decode(token, 'refresh_secret', algorithms='HS256' )
        return payload['user_id']

    except:
        raise exceptions.AuthenticationFailed('unauthenticated')
    

def send_otp_to_user(user):
    otp = generate_otp()  # generate a random OTP here
    subject = "Your One-Time Password (OTP)"
    message = f"Your OTP is: {otp}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    # store the OTP in the user's session or database for later verification