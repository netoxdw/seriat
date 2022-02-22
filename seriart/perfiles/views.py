from django.shortcuts import redirect, render
from perfiles.forms import SignUpForm

def sign_up(request):
    if request.method == 'GET':
        form = SignUpForm()
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')

    return render(request, 'registration/signup.html', {'form': form})