from django.db import models
from django.urls import reverse
from payments.models import Order
from django.utils import timezone
from datetime import timedelta

class IndicatorDownload(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    file_url = models.URLField()
    expires_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(days=30)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Download for Order #{self.order.id}"

    class Meta:
        verbose_name = "Indicator Download"
        verbose_name_plural = "Indicator Downloads"


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    file_doc = models.FileField(upload_to='products/docs/', null=True, blank=True)
    file_pdf = models.FileField(upload_to='products/pdfs/', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def get_files(self):
        """Return a list of attached file paths (for emailing or downloads)."""
        files = []
        if self.file_doc:
            files.append(self.file_doc.path)
        if self.file_pdf:
            files.append(self.file_pdf.path)
        return files

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
