from django.contrib import admin

from quora.models import Question, Answer, Like

admin.site.site_header = "Quora Clone"
admin.site.site_title = "Quora Clone"
admin.site.index_title = "Quora Clone"

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Like)
