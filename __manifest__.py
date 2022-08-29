# -*- coding: utf-8 -*-
# More info at https://www.odoo.com/documentation/master/reference/module.html

{
    "name": "Training Tasks",
    "depends": [
        "sale",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/discount_manager_group.xml",
        "views/sale_customization_views.xml",
        "report/sale_report_inherit.xml",
        "views/contact_customization_views.xml",
        "views/birthday_cron.xml",
    ],
    "application": True,
}
