from django import template

register = template.Library()

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
   OBSCENE_WORDS = ['рож', 'ере', 'поп', 'плот', 'ее', 'java', 'skillbox']  # в нижнем регистре!

   chr_array = [char for char in value]
   low_value = value.lower()  # создаём для поиска копию текста в нижнем регистре
   end_pos = len(value)
   for word in OBSCENE_WORDS:
      start_pos = 0
      word_len = len(word)
      while start_pos < end_pos - word_len:
         position = low_value.find(word, start_pos, end_pos)
         if position == -1:   # искомое слово не найдено
            break
         else:
            chr_array[position:position + word_len] = '*' * word_len   # выполняем замену слова в рабочем массиве
            start_pos += position + word_len
   return ''.join(chr_array)   # создаём результирующую строку из массива
