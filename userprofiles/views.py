from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic

from scand.models import ImageTag
from .forms import ProfileUpdateForm, UserUpdateForm


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.request
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        if self.request.user.groups.filter(name='qa'):
            context['new_tasks'] = ImageTag.objects.new_tasks(status=1)
            context['reverted_tasks'] = ImageTag.objects.reverted_tasks(status=1)
            context['forwarded_tasks'] = ImageTag.objects.forwarded_tasks(status=1)
        if self.request.user.groups.filter(name='approve'):
            context['new_tasks'] = ImageTag.objects.new_tasks(status=2)
            context['forwarded_tasks'] = ImageTag.objects.forwarded_tasks(status=2)
        if self.request.user.groups.filter(name='kpo'):
            context['reverted_tasks'] = ImageTag.objects.reverted_tasks(status=0)

        context['u_form'] = u_form
        context['p_form'] = p_form

        return context

    def post(self, request, *args, **kwargs):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'You have successfully updated your profile.')
            return redirect('dashboard')
