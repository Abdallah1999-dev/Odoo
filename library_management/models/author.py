from odoo import models, fields, api

class Author(models.Model):
    _inherit =  ['mail.thread','mail.activity.mixin']
    _name = 'library.author'
    _description = 'Author'

    name = fields.Char(required=True, tracking=True)
    image_1920 = fields.Image()
    biography = fields.Text()
    birth_date = fields.Date()
    nationality = fields.Char()
    book_ids = fields.One2many('library.book','author_id')