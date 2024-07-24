from odoo import fields, models


class LibraryProduct(models.Model):
    _name = "library.product"
    _description = "Library Book"

    product_image = fields.Image(max_width=128, max_height=128)
    product_name = fields.Char("Product Name: ", required=True)
    can_be_sold = fields.Boolean(string="Can be Sold")
    can_be_purchased = fields.Boolean(string="Can be Purchased")
    is_a_book = fields.Boolean(string="Is a Book")

    # Book Details------------------------------------------------------------------------------------

    # Basic Information------------------------------------------------------------------------------
    book_title = fields.Char(string="Book Title")
    # authors = fields.Many2one("author.model", string="Authors", required=True)
    page_numbers = fields.Integer(string="Page Numbers", default="0")
    isbn = fields.Char("ISBN: ")
    # publisher_information = fields.Many2one("publisher.model", string="Publisher Information")

    # Extra Information----------------------------------------------------------------------------------

    publication_date = fields.Date("Publication Date: ")
    genre = fields.Selection([
        ("fiction", "Fiction"),
        ("non_fiction", "Non-Fiction"),
        ("science", "Science"),
        ("history", "History")
    ],"Genre: ")
    language = fields.Char(string="Language")
    available = fields.Boolean("Available: ", default=True)

    # External Links--------------------------------------------------------------------------------------------

    web_link = fields.Char(string="Web Reader Link")
    preview_link = fields.Char(string="Preview Link")
