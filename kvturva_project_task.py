from openerp import models, fields, api

class project_task(models.Model):
    _inherit='project.task'
    _name='project.task'

    product_id=fields.Many2one('product.product',
        ondelete='restrict', string="Product", index=True)
        #domain=[('type', '=', 'service')])

class product_product(models.Model):
    _inherit='product.product'
    _name='product.product'
    id = fields.One2many(
        'project.task', 'product_id', string="Tasks")