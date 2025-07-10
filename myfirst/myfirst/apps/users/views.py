from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .serializers import RegisterSerializer, LoginSerializer
from .models import User
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

@csrf_protect
def register(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            messages.success(request, 'Регистрация успешна')
            return redirect('login')
        else:
            return render(request, 'users/register.html', {'errors': serializer.errors})
    return render(request, 'users/register.html')

@csrf_protect
def login(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.POST)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data['email'])
            except User.DoesNotExist:
                messages.error(request, 'Пользователь не найден')
                return render(request, 'users/login.html')

            if check_password(serializer.validated_data['password'], user.password):
                refresh = RefreshToken.for_user(user)
                response = redirect('profile_view')
                response.set_cookie('access_token', str(refresh.access_token), httponly=True, secure=True)
                messages.success(request, 'Вход выполнен успешно')
                return render(request, 'users/index.html')
            else:
                messages.error(request, 'Неверный пароль')
                return render(request, 'users/login.html')
        else:
            return render(request, 'users/login.html', {'errors': serializer.errors})
    return render(request, 'users/login.html')

def profile_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Пожалуйста, войдите в систему')
        return redirect('login')
    return render(request, 'users/profile.html', {'user': request.user})

def logout_view(request):
    response = redirect('login')
    response.delete_cookie('access_token')
    messages.success(request, 'Вы успешно вышли из системы')
    return response

def home(request):
    return render(request, 'users/index.html')
