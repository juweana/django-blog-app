from django.contrib import admin
from.models import Teacher,Course

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','description', 'is_active')
    list_filter = ('is_active',)
    search_fields =('title',)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = ('name', 'bio')

