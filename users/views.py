from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

def landing_page(request):
    return render(request, 'landing.html')

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required
def profile_view(request):
    profile = request.user
    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'users/edit_profile.html', {'form': form})
