from django.urls import reverse_lazy
from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Author, User
from .forms import PostForm
from .filters import PostFilter


class NewsList(ListView):
    model = Post    # Указываем модель, объекты которой мы будем выводить
    ordering = '-datetime'    # Поле, которое будет использоваться для сортировки объектов    #ordering = 'rating'
    # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 1

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса, чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам. В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()        # К словарю добавим текущую дату в ключ 'time_now'.
        #context['next_sale'] = None        # Добавим ещё одну пустую переменную, чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['filterset'] = self.filterset
        return context


class PostSearch(DetailView):
    form_class = PostFilter
    model = Post
    template_name = 'search.html'
    # success_url = reverse_lazy('news')


class PostDetail(DetailView):
    model = Post    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    template_name = 'one_post.html'    # Используем другой шаблон
    context_object_name = 'one_post'    # Название объекта, в котором будет выбранная пользователем новость

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object.id)
        return context


# def PostCreate(request):
#     form = PostForm()
#     if request.method == 'POST':
#         new_form = PostForm(request.POST)
#         if new_form.is_valid():
#             new_form.save()
#             return HttpResponseRedirect('/news/')
#
#     # def post(self, request, *args, **kwargs):
#     #     #id = request.id
#     #     #user = User.objects.get(id=request.user.id)
#     #     user = User.objects.get(id=request.user.id)
#     #     author = Author.objects.get(user=user)
#     #
#     #     if self.form.is_valid():
#     #         post = self.form.save(commit=False)
#     #         #post.author = author
#     #         #NEWS_TYPES = [('AR', 'статья'), ('NW', 'новость')]
#     #         url_str = self.form.get_absolute_url()
#     #         #news_type = self.form.
#     #         post.post_category = 'AR'
#     #         post.datetime = datetime.utcnow()
#     #         post.save()
#
#     return render(request, 'post_edit.html', {'form': form})

class PostCreate(CreateView):
    form_class = PostForm    # Указываем нашу разработанную форму
    model = Post
    template_name = 'post_edit.html'    # и новый шаблон, в котором используется форма.

    def post(self, request, *args, **kwargs):
        #id = request.id
        #user = User.objects.get(id=request.user.id)
        #author = Author.objects.get(user=user)
        form = PostForm()

        def form_valid(self, form):
            post = form.save(commit=False)
            post.post_category = 'AR'
            return super().form_valid(form)

        if form.is_valid():
            post = form.save(commit=False)
            #post.author = author
            #NEWS_TYPES = [('AR', 'статья'), ('NW', 'новость')]
            #url_str = form.get_absolute_url()
            #news_type = self.form.
            post.post_category = 'AR'
            post.datetime = datetime.utcnow()
            post.save()

        return super(PostCreate, self).post(self, request, *args, **kwargs)

class PostEdit(UpdateView):    # Добавляем представление для изменения
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):    # Добавляем представление для удаления
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')

