from django.db import models

# Create your models here.
class QuoteCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    quote_category = models.ForeignKey(QuoteCategory, on_delete=models.CASCADE, related_name='quote')

    def __str__(self) -> str:
        if len(self.quote) > 30:
            return self.quote[:30] + '...'
        return self.quote

