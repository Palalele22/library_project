from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from library.forms import CustomUserCreationForm 
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_approved = False 
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# class CustomLoginView(LoginView):
#     def form_valid(self, form):
#         user = form.get_user()
#         if not user.is_approved:
#             messages.error(self.request, 'Your account is not activate yet. Please wait for an admin to activate your account.')
#             return self.form_invalid(form)
#         return super().form_valid(form)

# class CustomLogoutView(LogoutView):
#     def get_next_page(self):
#         return

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_approved:
                login(request, user)
                messages.success(request, "You have been logged in successfully")
                return redirect('profile')
            else:
                messages.error(request, 'Your account is not activated yet. Please wait for an admin to activate your account.')
                return redirect('login')
        else:
            messages.error(request, "There was an error, please try again.")
            return redirect('login')
    else:
        return render(request, 'registration/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('login')
    
def index(request):
    return HttpResponse("hello")

@login_required
def my_profile(request):
    return render(request, 'library/my_profile.html')
