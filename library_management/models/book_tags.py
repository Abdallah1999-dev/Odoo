from odoo import models, fields, api

class BookTags(models.Model):
    _name = 'library.book.tag'

    name = fields.Char(required=True)
    color = fields.Integer(default=1)

