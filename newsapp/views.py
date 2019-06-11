from django.views.generic import *
from django.urls import reverse_lazy, reverse
from .models import Post, Tag, Photo
from .forms import AdminNewsForm
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import *
from django.views.generic.edit import FormView
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.template import RequestContext
from django.views import View
import json
from django.template.loader import render_to_string





class AdminNewsListView(ListView):
    model = Post
    template_name = 'admintemplates/newsapp/newslist.html'
    # context_object_name ='news'


class AdminNewsDetailView(DetailView):
    model = Post
    template_name = 'admintemplates/newsdetail.html'


class AdminNewsCreateView(CreateView):
    form_class = AdminNewsForm
    template_name = 'admintemplates/newsapp/newscreate.html'
    success_url = reverse_lazy('newsapp:adminnewslist')
    # form_class = modelformset_factory(
    #     models.Sample,
    #     fields=['name', 'collected', 'location'],
    #     extra=3
    # )


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['image'] = ImageForm
        # context['com'] = CommentForm
        return context

    def form_valid(self, form):
        user = self.request.user.id
        author = User.objects.get(id=user)
        form.instance.author = author
        form.instance.update_by = author
        return super().form_valid(form)


class AdminNewsUpdateView(UpdateView):
    model = Post
    form_class = AdminNewsForm
    success_url = reverse_lazy('newsapp:adminnewslist')
    template_name = 'admintemplates/newsapp/newsupdate.html'

    def form_valid(self, form):
        user = self.request.user.id
        author = User.objects.get(id=user)
        form.instance.author = author
        form.instance.update_by = author
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('newsapp:adminnewslist')


class AdminNewsDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse('newsapp:adminnewslist')


class ClientHomeView(ListView):
    template_name = 'clienttemplates/clienthome.html'
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(ClientHomeView, self).get_context_data(**kwargs)
        context['popularposts'] = Post.objects.filter().order_by('-post_count')[:5]
        context['latest'] = Post.objects.filter().order_by('-created_at')[0:1]
        context['latests'] = Post.objects.filter().order_by('-created_at')[0:4]
        context['random'] = Post.objects.filter().order_by('?')[0:4]
        return context


class ClientPostDetailView(DetailView):
    template_name = 'clienttemplates/clientnewsdetail.html'
    model = Post

    # def get_queryset(self):
    #     self.post_count = get_object_or_404(Post, pk=self.kwargs['pk'])
    #     self.post_count = self.post_count.values('post_count') + 1
    #     return Post.objects.filter(topic=self.post_count)

    def get_context_data(self, **kwargs):
        context = super(ClientPostDetailView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        obj = self.get_object()
        obj.post_count += 1
        obj.save()
        return context


class ClientPostTopic(ListView):
    model = Post
    template_name = 'clienttemplates/clientnewstopic.html'
    paginate_by = 1

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        return Post.objects.filter(topic=self.topic)

    def get_context_data(self, **kwargs):
        context = super(ClientPostTopic, self).get_context_data(**kwargs)
        context['topic'] = self.topic
        context['categories'] = Category.objects.all()
        return context


class ClientPostTag(ListView):
    model = Post
    template_name = 'clienttemplates/clientnewstag.html'
    paginate_by = 1

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, pk=self.kwargs['pk'])
        return Post.objects.filter(tag=self.tag)

    def get_context_data(self, **kwargs):
        context = super(ClientPostTag, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        context['categories'] = Category.objects.all()
        return context



class ClientPostCategory(ListView):
    model = Post
    template_name = 'clienttemplates/clientnewscategory.html'
    paginate_by = 2

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(topic__category=self.category)

    def get_context_data(self, **kwargs):
        context = super(ClientPostCategory, self).get_context_data(**kwargs)
        context['category'] = self.category
        context['categories'] = Category.objects.all()
        post__category = Category.objects.get(id=self.kwargs['pk']) #taking single category name
        context['cat'] = post__category
        return context


class AdminGalleryView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'admintemplates/newsapp/albumcreate.html', {'photos': photos_list})

    def post(self, request):
        form = AdminPhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid() and request.is_ajax():
            photo = form.save()
            data = {
            'is_valid': True, 
            'name': photo.file.name,
            'url': photo.file.url,
            'id': photo.id,
            }
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def adminDeleteImage(request, pk):
    data = dict()
    photo = get_object_or_404(Photo,id=pk)
    if request.method == "POST" and request.is_ajax():
        photo.delete()
        data['form_is_valid'] = True
        photos = Photo.objects.all()
        data['photo_list'] = render_to_string('admintemplates/newsapp/albumcreate.html',{'photos':photos})
    else:
        context = {'photo':photo}
        data['html_form'] = render_to_string('admintemplates/newsapp/albumcreate.html',context,request=request)

    return JsonResponse(data)




# class AdminImageDeleteView(DeleteView):
#     model = Photo
#     template_name = "admintemplates/newsapp/albumcreate.html"
#     success_url = "/"

#     # allow delete only logged in user by appling decorator
#     # @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         # maybe do some checks here for permissions ...

#         resp = super(AdminImageDeleteView, self).dispatch(*args, **kwargs)
#         if self.request.is_ajax():
#             response_data = {"result": "ok"}
#             return HttpResponse(json.dumps(response_data),
#                 content_type="application/json")
#         else:
#             # POST request (not ajax) will do a redirect to success_url
#             return resp


# class AdminImageDeleteView(DeleteView):
#     model = Photo


#     # def delete(self, request, *args, **kwargs):
#     #     self.get_object().delete()
#     #     payload = {'delete': 'ok'}
#     #     return HttpResponse(json.dumps(payload), mimetype='application/json')

#     def get_success_url(self):
#         return reverse('newsapp:adminalbumcreate')





# class AdminGalleryCreateView(FormView):
#     success_url = reverse_lazy('newsapp:adminalbumdetail')
#     template_name = 'admintemplates/adminalbumcreate.html'
#     form_class = ImageForm

#     # def get_form_kwargs(self):
#     #     kwargs = super(AdminGalleryCreateView, self).get_form_kwargs()
#     #     kwargs["queryset"] = Images.objects.none()
#     #     return kwargs

#     def form_valid(self, form):
#         user = self.request.user.id
#         author = User.objects.get(id=user)
#         form.instance.author = author
#         return super().form_valid(form)



# class AdminGalleryCreateView(FormView):
#     success_url = reverse_lazy('newsapp:adminalbumdetail')
#     form_class = modelformset_factory(
#         Images,
#         fields=['name', 'description', 'image'],
#         extra=3
#     )
#     template_name = 'admintemplates/adminalbumcreate.html'

#     def get_form_kwargs(self):
#         kwargs = super(AdminGalleryCreateView, self).get_form_kwargs()
#         kwargs["queryset"] = Images.objects.none()
#         return kwargs

#     def form_valid(self, form):
#         for sub_form in form:
#             if sub_form.has_changed():
#                 sub_form.save()

#         return super(AdminGalleryCreateView, self).form_valid(form)



# def album(request):

#     ImageFormSet = modelformset_factory(Images, form=ImageForm, extra=3)

#     if request.method == 'POST':

#         postForm = AlbumForm(request.POST)
#         formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())

#         if postForm.is_valid() and formset.is_valid():
#             post_form = postForm.save(commit=False)
#             post_form.user = request.user
#             post_form.save()

#             for form in formset.cleaned_data:
#                 image = form['image']
#                 photo = Images(post=post_form, image=image)
#                 photo.save()
#             messages.success(request, "Posted!")
#             return HttpResponseRedirect("/")
#         else:
#             print (postForm.errors, formset.errors)
#     else:
#         postForm = AlbumForm()
#         formset = ImageFormSet(queryset=Images.objects.none())
#     return render(request, 'admintemplates/newsapp/albumcreate.html',
#                   {
#                   'postForm': postForm, 
#                   'formset': formset},
#                  )

# class ClientPostCategory(ListView):
#     paginate_by = 2
#     model = Post
#     template_name = 'clienttemplates/clientnewscategory.html'
    

#     # def get_queryset(self):
#     #     self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
#     #     return Post.objects.filter(category=self.category)

#     def get_context_data(self, **kwargs):
#         context = super(ClientPostCategory, self).get_context_data(**kwargs)
#         # context['category'] = self.category
#         context['categories'] = Category.objects.all() #menu bar
#         # print(Post.objects.filter(topic__category=self.kwargs['pk']))
#         context['posts'] = Post.objects.filter(topic__category=self.kwargs['pk']).order_by('created_at')
#         post__category = Category.objects.get(id=self.kwargs['pk']) #taking single category name
#         context['cat'] = post__category
#         # print(context['posts'])
#         return context