from django.contrib import admin
from backend.models import Student, Teacher, Class, Diary, Gptassistance, Gptinteraction

class ClassAdmin(admin.ModelAdmin):
    list_display = ('id','class_name')
    ordering = ('id',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'gender', 'class_name', 'teacher_name')
    list_filter = ('gender',)
    ordering = ('id',)

    def user_id(self, obj):
        return obj.user.id if obj.user else None

    def class_name(self, obj):
        return obj.class_field.class_name if obj.class_field else "No Class"

    def teacher_name(self, obj):
        return obj.teacher.name if obj.teacher else "No Teacher"

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    ordering = ('id',)

class DiaryAdmin(admin.ModelAdmin):
    list_display = ('_student', 'date', 'title', 'content', 'mood', 'target', 'diary_type', 'is_favorite', 'last_modified_date')
    list_filter = ('is_favorite',)
    def _student(self, obj):
        return obj.student.name
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Diary, DiaryAdmin)
admin.site.register(Gptassistance)
admin.site.register(Gptinteraction)
