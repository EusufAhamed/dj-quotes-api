from django.contrib import admin
from quote_app.models import Quote, QuoteCategory

# Register your models here.
admin.site.register(Quote)
admin.site.register(QuoteCategory)