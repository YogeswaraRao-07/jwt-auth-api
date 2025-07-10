from django.shortcuts import render

# Create your views here.
import jwt, datetime
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)

    if user:
        expiry = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        payload = {
            'id': user.id,
            'username': user.username,
            'exp': expiry,
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
        return Response({'token': token, 'expires': expiry.isoformat() + 'Z'})

    return Response({'error': 'Invalid credentials'}, status=401)

@api_view(['POST'])
def verify_token(request):
    try:
        jwt.decode(request.data['token'], settings.SECRET_KEY, algorithms=['HS256'])
        return Response({'valid': True, 'message': 'Token is valid'})
    except jwt.ExpiredSignatureError:
        return Response({'valid': False, 'message': 'Token expired'})
    except jwt.InvalidTokenError:
        return Response({'valid': False, 'message': 'Invalid token'})

@api_view(['GET'])
def validate_token(request):
    auth_header = request.headers.get('Authorization', '')
    token = auth_header.split(' ')[-1] if ' ' in auth_header else ''
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return Response({'valid': True, 'user': payload['username'], 'expires': payload['exp']})
    except jwt.ExpiredSignatureError:
        return Response({'valid': False, 'message': 'Token expired'})
    except jwt.InvalidTokenError:
        return Response({'valid': False, 'message': 'Invalid token'})