from django.forms import ModelForm
from .models import Quiz
from django.core.exceptions import ValidationError
from django import forms




class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ("gender", "age", "rating")

    def clean_rating(self):
        data = self.cleaned_data["rating"]

        # Проверка того, что рейтинг находится в пределах от 1 до 10
        if 1 > data or 10 < data:
            raise ValidationError('Введите число от 1 до 10')
        
        return data

      