from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    template = "home/home_page.html"
    sub_tilte = models.CharField(max_length=100, blank=True, null=True)
    max_count = 1
    content_panels = Page.content_panels + [
        FieldPanel("sub_tilte")
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
