# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api, _


class ContactCustomization(models.Model):
    _inherit = 'res.partner'

    birthdate = fields.Date(String="Birth Date")

    @api.model
    def _check_birthdate(self):
        today = datetime.date.today()
        contacts = self.env['res.partner'].search([])
        birthday_contacts = []
        str = ""

        for record in contacts:
            if (record.birthdate):
                if (record.birthdate - today).days <= 3:
                    birthday_contacts.append(record.name)
                    birthday_contacts.append(' and ')

        if birthday_contacts is not None:
            birthday_contacts.pop()
            for ele in birthday_contacts:
                str += ele
            for c in contacts:
                mail = self.env['mail.mail'].create({
                    'subject': _('Birthday Reminder'),
                    'email_from': "odoobot@example.com",
                    'email_to': c.email,
                    'body_html': 'This email is to inform you that some of your colleagues have birthdays soon, please send your birthday wishes to '+str,
                   })
                mail.send()
