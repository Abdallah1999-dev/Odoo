from odoo import models, fields, api
from odoo.exceptions import  ValidationError


class Book(models.Model):
    _inherit =  ['mail.thread','mail.activity.mixin']
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(required=True)
    image_1920 = fields.Image()
    author_id = fields.Many2one('library.author')
    isbn = fields.Char()
    category_id = fields.Many2many('library.book.tag')
    copies_total = fields.Integer(required=True)
    copies_available = fields.Integer()
    published_year = fields.Char(default="19xx")
    description = fields.Text()


    @api.constrains('published_year')
    def check_published_year_val(self):
        for rec in self:
            year = rec.published_year
            if not year.isdigit() or len(year) != 4:
                raise ValidationError('Invalid Published Year! Please enter a 4-digit number.')
            else:
                pass
