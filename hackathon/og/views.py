# og/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required # Ensure this is imported once
from .models import UserProfile # Ensure this is imported once and uncommented

def register_view(request):
    if request.method == 'POST':
        # You can remove these print statements now that we've debugged the password issue
        # print("--- Incoming POST Data ---")
        # print(request.POST)
        # print("--------------------------")

        form = UserCreationForm(request.POST)
        solana_wallet = request.POST.get('solana_wallet')
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user, solana_wallet_address=solana_wallet)
            login(request, user)
            messages.success(request, 'Registration successful! Welcome to Transify.')
            return redirect('dashboard')
        else:
            # You can remove these print statements now that we've debugged the password issue
            # print("--- Form Errors ---")
            # print(form.errors)
            # print("-------------------")

            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'commuter/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'commuter/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')

@login_required # This decorator ensures only logged-in users can access
def dashboard_view(request):
    # This line retrieves the UserProfile linked to the currently logged-in Django User
    user_profile = request.user.userprofile
    context = {
        'user_profile': user_profile, # This is the line that passes the data to the template
    }
    return render(request, 'commuter/dashboard.html', context)

def operator_scan_view(request):
    return render(request, 'operator/scan_user.html')
