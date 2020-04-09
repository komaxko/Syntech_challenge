from .models import Table

from django.contrib import admin


@admin.register(Table)
class ReportAdmin(admin.ModelAdmin):
    def save_model(self, request, instance, form, change):
        instance = form.save(commit=False)
        if not change or not instance.created_by:
            instance.created_by = request.user.pk
        instance.modified_by = request.user.pk
        instance.save()
        form.save_m2m()
        return instance
