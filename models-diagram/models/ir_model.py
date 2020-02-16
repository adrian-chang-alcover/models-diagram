# -*- coding: utf-8 -*-

from openerp import models, fields


class ir_model(models.Model):
    _name = 'ir.model'
    _inherit = 'ir.model'

    # model_id = fields.Many2one('ir.model')
