from django.contrib import admin
from .models import BookModel
class BookAdmin(admin.ModelAdmin):
	readonly_fields = ['slug']
	class Meta:
		model = BookModel		

admin.site.register(BookModel, BookAdmin)
