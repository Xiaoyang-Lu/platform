from django.contrib import admin

# Register your models here.
from models import Matrix

class MatrixAdmin(admin.ModelAdmin):

	list_display = ['__unicode__','timestamp', 'updated', 'mx1', 'mx2','mx3', 'mx4']
	list_display_links = ['__unicode__','mx1', 'mx2','mx3', 'mx4']
	list_filter = ['timestamp', 'updated']
	
	search_fields = ['__unicode__']

	class Meta:
		model = Matrix
			

admin.site.register(Matrix, MatrixAdmin)