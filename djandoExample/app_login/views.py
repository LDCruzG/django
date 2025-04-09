from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        return redirect('welcome', nombre=nombre, apellido=apellido)
    return render(request, 'app_login/login.html')

def welcome_view(request, nombre, apellido):
    return render(request, 'app_login/welcome.html', {
        'nombre': nombre,
        'apellido': apellido
    })