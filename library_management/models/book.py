from odoo import models, fields, api

class Book(models.Model):
    _inherit =  ['mail.thread','mail.activity.mixin']
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(required=True)
    image_1920 = fields.Image()
    author_id = fields.Many2one('library.author')
    isbn = fields.Char()
    category_id = fields.Char()
    copies_total = fields.Integer(required=True)
    copies_available = fields.Integer()
    published_date = fields.Date()
