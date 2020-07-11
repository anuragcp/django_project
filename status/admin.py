from django.contrib import admin

from .forms import StatusForm
from .models import Status

class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'image']
    form = StatusForm
    # we are not using model directly instead uses the forms
    # class Meta:
    #     model = Status


admin.site.register(Status, StatusAdmin)
