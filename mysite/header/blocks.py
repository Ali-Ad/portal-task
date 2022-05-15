from wagtail.core import blocks


class HeaderBlock(blocks.StructBlock):
    headers = blocks.ListBlock(
        blocks.StructBlock([
            ("text", blocks.CharBlock(required=True)),
            ("page", blocks.PageChooserBlock(required=False, max_length=40)),
            ("page_url", blocks.URLBlock(required=False, max_length=60)),
        ])
    )

    class Meta:
        template = "header/header_block.html"
        icon = "edit"
        label = "Header"
