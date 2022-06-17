from django_filters import FilterSet, CharFilter, NumberFilter, DateFilter
#import django.contrib.admin.ModelAdmin
from django.forms import DateInput
from .models import Post

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем, должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    text = CharFilter(
        field_name='text',
        lookup_expr='contains',
        label = 'Текст статьи содержит:',
    )

    title = CharFilter(
        field_name='title',
        lookup_expr='contains',
        label = 'Заголовок содержит:',
    )

    time_lt = DateFilter(
        field_name = 'datetime',
        lookup_expr = 'lt',
        label = 'Дата создания до:',
        widget = DateInput(attrs={'type': 'date'}),
    )

    time_gt = DateFilter(
        field_name = 'datetime',
        lookup_expr = 'gt',
        label = 'Дата создания после:',
        widget = DateInput(attrs={'type': 'date'}),
    )

    rating_gt = NumberFilter(
        field_name='rating',
        lookup_expr='gt',
        label = 'Рейтинг более:',
    )

    rating_lt = NumberFilter(
        field_name='rating',
        lookup_expr='lt',
        label = 'Рейтинг менее:',
    )

    # def __init__(self, *args, **kwargs):
    #     super(PostFilter, self).__init__(*args, **kwargs)
    #     # super().__init__(*args, **kwargs)
    #     self.filters['text'].label = "Текст содержит:"

    class Meta:
        model = Post # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        # В fields мы описываем по каким полям модели будет производиться фильтрация.
        #author = model.author.    #.user.username

        fields = {
           #author: ['icontains'],
           #'datetime': ['gt'],
           #'news_type':
           #'post_category': ['icontains'],
           #'text': ['contains'],
           #'title': ['contains'],   # 'icontains'
           # 'rating':[
           #     'lt',  # рейтинг должен быть меньше или равен указанному
           #     'gt',  # рейтинг должен быть больше или равен указанному
           # ],
        }
        # label = {
        #     'datetime': 'Время создания:',
        #     'text': 'Текст содержит:',
        #     'title': 'Заголовок:',
        # }




