from django.db import models
from modelcluster.fields import ParentalKey
from wagtail_blocks.blocks import HeaderBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel, InlinePanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from . import blocks


class FooterPageCarouse(Orderable):
    page = ParentalKey("footer.FooterPage" ,related_name="footer_carouse")
    title = models.CharField(max_length=40, blank=False, null=True)
    internal_url = models.ForeignKey("wagtailcore.Page", null=True, blank=True, on_delete=models.CASCADE,
                                     related_name="+")
    external_url = models.URLField(blank=True, null=True)


class FooterPage(Page):
    template = "footer/footer_page.html"
    content = StreamField(
        [
            ("footer", blocks.FooterBlock()),
        ],
        null=True,
        blank=True,

    )
    max_count = 1
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    content_panels = Page.content_panels + [

        # FieldPanel("sub_title"),
        InlinePanel("footer_carouse"),
        # StreamFieldPanel("content"),

    ]

    class Meta:
        verbose_name = "Footer Page"
        verbose_name_plural = "Footer Pages"
