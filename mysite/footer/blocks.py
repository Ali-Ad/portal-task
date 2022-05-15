from wagtail.core import blocks
from wagtail.core.blocks import StructBlock, PageChooserBlock


class FooterBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        blocks.StructBlock([
            ("text", blocks.CharBlock(required=True)),
            ("page", blocks.PageChooserBlock(required=False, max_length=40)),
            ("page_url", blocks.URLBlock(required=False, max_length=60)),
        ])
    )

    class Meta:
        template = "footer/footer_block.html"
        icon = "edit"
        label = "Footer"
