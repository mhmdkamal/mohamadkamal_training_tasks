# -*- coding: utf-8 -*-

from odoo import models, fields, api
from stdnum.exceptions import ValidationError


class SaleCustomization(models.Model):
    _inherit = 'sale.order'

    discount_amount = fields.Float(String="Disc%", default=0.0)
    total_amount_after_discount = fields.Float(compute='_compute_total_amount_after_discount', String="Disc Amount", default=0.0)

    @api.constrains("discount_amount")
    def _check_price_difference(self):
        for record in self:
            if record.discount_amount > 100.00:
                raise ValidationError("percantage should be below 100%")
            else:
                pass

    @api.onchange("state", "discount_amount")
    def _compute_total_amount_after_discount(self):
        for record in self:
            if record.state == 'sale':
                record.total_amount_after_discount = record.amount_total - (record.amount_total * (record.discount_amount/100))
            else:
                record.total_amount_after_discount = 0.0


                           # if you want to add the fields on the line #
# class SaleCustomizationLine(models.Model):
#     _inherit = 'sale.order.line'
#
#     discount_amount = fields.Float(String="Disc%", default=0.0)
#     total_amount_after_discount = fields.Float(String="Disc Amount")