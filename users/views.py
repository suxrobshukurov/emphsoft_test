from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView

from .models import Profile
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistraion, ProfileImage, UserUpdateForm

# def home(request):
#     data = {
#         'users': Profile.objects.all(),
#         'title': 'Список пользователей'
#     }
#
#     return render(request, 'users/list.html', data)


class ShowNewsView(ListView):
    model = Profile
    template_name = 'users/list.html'
    context_object_name = 'users'
    ordering = ['-id']

    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Список пользователей'
        return ctx


class NewsDetailView(DetailView):
    model = Profile
    template_name = 'users/list-detail.html'
    context_object_name = 'user_item'

    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = Profile.objects.get(pk=self.kwargs['pk'])
        return ctx


def register(request):
    if request.method == "POST":
        form = UserOurRegistraion(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                f'Аккаунт {username} был создан, введите имя пользователя и пароль для авторизации')
            return redirect('user')
    else:
        form = UserOurRegistraion()
    return render(request, 'users/registraion.html',
                  {'form': form, 'title': 'Регистрация пользователя'})


@login_required
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(
            request.POST,
            request.FILES,
            instance=request.user.profile)
        update_user = UserUpdateForm(
            request.POST, instance=request.user.profile)

        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен')
            return redirect('profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user.profile)

    data = {
        'img_profile': img_profile,
        'update_user': update_user
    }

    return render(request, 'users/profile.html', data)
