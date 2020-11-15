from django.contrib import admin
from .models import Post, Article, Quiz
from django.utils.safestring import mark_safe
from django import forms

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    full_text = forms.CharField(label="Полный текст", widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class AboutmeAdminForm(forms.ModelForm):
    content = forms.CharField(label="обо мне", widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("author", "created_date", "title", "id")
    form = PostAdminForm

class QuizAdmin(admin.ModelAdmin):
    list_display = ("id", "gender", "age", "rating")



class AboutmeAdmin(admin.ModelAdmin):
    list_display = ( "id", "img", "get_image")
    readonly_fields = ("get_image", )
    form = AboutmeAdminForm

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="80" height="60"')

    get_image.short_description = "Изображение"

admin.site.register(Post, CategoryAdmin)
admin.site.register(Article, AboutmeAdmin)
admin.site.register(Quiz, QuizAdmin)




admin.site.site_title = 'Django Portfolio'
admin.site.site_header = 'Django Portfolio'