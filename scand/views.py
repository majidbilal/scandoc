from django.contrib.messages.views import SuccessMessageMixin
from django.forms import Form
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from scand.utils import status_change
from .forms import ImageForm, SearchForm
from .models import ImageTag
from io import BytesIO
from .pdfs import MyPrint


class ImageCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, generic.CreateView):
    permission_required = 'scand.add_imagetag'
    permission_denied_message = "You don't have permission to visit this page."
    login_url = '/login/'
    model = ImageTag
    form_class = ImageForm
    success_url = '/create/'
    success_message = 'record added.'

    def form_valid(self, form):
        form.save(commit=False)
        form.instance.changed_by = self.request.user
        form.instance.status = 1
        return super().form_valid(form)


class ImageListView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    model = ImageTag
    template_name = 'scand/images.html'
    context_object_name = 'images'

    def get_queryset(self):
        queryset = ImageTag.objects.ordered_images()
        return queryset


class ImageDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.edit.FormMixin, generic.DetailView):
    permission_required = 'scand.can_approve'
    permission_denied_message = "You don't have permission to visit this page."
    login_url = '/login/'
    model = ImageTag
    template_name = 'scand/image-detail.html'
    form_class = ImageForm

    def get_form(self, form_class=None):
        form = Form(self.request.POST, None)
        return form

    def post(self, request, *args, **kwargs):
        image_id = self.request.POST.get('id')
        approve = None
        if self.request.POST.get('approve'):
            approve = True
        elif self.request.POST.get('revert'):
            approve = False

        next_page = status_change(request, approve=approve, image_id=image_id, model=ImageTag)

        # TODO: If everything works out well below code block needs to be deleted
        # if self.request.POST.get('approve'):
        #     if image_id:
        #         image = ImageTag.objects.filter(id=image_id)
        #         image.update(status='03')
        #         return redirect('dashboard')
        #     else:
        #         return render(request, '403.html', context={'exception': 'Bad request'})
        # elif self.request.POST.get('revert'):
        #     if image_id:
        #         image = ImageTag.objects.filter(id=image_id)
        #         image.update(status='01', is_reverted=True)
        #         return redirect('dashboard')
        #     else:
        #         return render(request, '403.html', context={'exception': 'Bad request'})

        return next_page


class ImageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    permission_required = 'scand.change_imagetag'
    permission_denied_message = "You don't have permission to visit this page."
    login_url = '/login/'
    model = ImageTag
    form_class = ImageForm
    prefix = 'img'
    template_name = 'scand/imagetag_form.html'
    success_url = '/dashboard/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'update'
        return context

    def form_valid(self, form):
        form.save(commit=False)
        if form.instance.is_reverted:
            form.instance.is_forwarded = True
        form.instance.changed_by = self.request.user
        form.instance.status = form.instance.status + 1
        return super().form_valid(form)

    # def form_invalid(self, form):
    #     image_id = self.request.POST.get('id')
    #     approve = None
    #     if self.request.POST.get('revert'):
    #         approve = False

    def post(self, request, *args, **kwargs):  # handling revert
        if request.is_ajax():
            print(request.POST)
            image_id = request.POST.get('id')
            next_url = status_change(request, approve=False, image_id=image_id, model=ImageTag)
            return next_url
        return super().post(request, *args, **kwargs)


class SearchFormView(LoginRequiredMixin, generic.FormView):
    login_url = '/login/'
    template_name = 'scand/search.html'
    form_class = SearchForm


# class SearchView(generic.View):
#     def get(self, request, *args, **kwargs):
#         print(ImageTag.objects.filter(pernum=request.GET.get('pernum')))
#         context = {
#             'results': ImageTag.objects.filter(pernum=request.GET.get('pernum'))
#         }
#         return render(request, 'scand/search_result.html', context)


class SearchView(LoginRequiredMixin, generic.ListView):
    login_url = '/login/'
    template_name = 'scand/search_result.html'
    context_object_name = 'images'

    def get_queryset(self):
        form = SearchForm(self.request.GET)
        query_dict = {}
        if form.is_valid():
            query_dict = form.cleaned_data
        # self.request.session['query_dict'] = query_dict
        queryset = ImageTag.objects.search(query_dict)
        return queryset


class SavePDF(LoginRequiredMixin, generic.View):
    login_url = '/login/'

    def post(self, request):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=some_file.pdf'
        buffer = BytesIO()
        query_dict = request.POST.getlist('id')
        # query_dict = request.session.get('query_dict')
        print(query_dict)
        results = ImageTag.objects.search(query_dict)  # receives queryset or False

        if not results:
            return HttpResponse("Your search returned 0 results")
        else:
            report = MyPrint(buffer, 'A4', results)
            pdf = report.generate_pdf()

        # response = FileResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = 'inline'

        # receipients = [
        #     '0hamidjunaid@gmail.com',
        #     'seimran@gmail.com',
        #     'yasin.munsif@gmail.com',
        #     'majidbilaly@gmail.com'
        # ]
        # EmailMsg = EmailMessage("Hello World", "This is the body", to=receipients)
        # EmailMsg.attach('scond.pdf', pdf, 'application/pdf')
        # print(EmailMsg)
        # EmailMsg.send(fail_silently=False)

        response.write(pdf)

        # request.session['response'] = response
        return response
