from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel
from . import blocks


# class HeaderPageCarouse(Orderable):
#     page = ParentalKey("header.HeaderPage", related_name="carousal_Header")
#     title = models.CharField(max_length=40, blank=False, null=True)
#     internal_url = models.ForeignKey("wagtailcore.Page", null=True, blank=True, on_delete=models.CASCADE,
#                                      related_name="+")
#     external_url = models.URLField(blank=True, null=True)
#     Panels = [
#         StreamFieldPanel("page"),
#         StreamFieldPanel("title"),
#         StreamFieldPanel("internal_url"),
#         StreamFieldPanel("external_url"),
#     ]

class HeaderPage(Page):
    template = "header/header_page.html"
    max_count = 1

    content = StreamField([
        ("Header", blocks.HeaderBlock())
    ],
        null=True,
        blank=True,
    )
    content_panels = Page.content_panels + [

        StreamFieldPanel("content"),

    ]

    class Meta:
        verbose_name = "Header Page"
        verbose_name_plural = "Header Pages"
