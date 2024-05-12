# -*- coding: utf-8 -*-
# charges.py

from odoo import models, fields, api


class charges(models.Model):
    _name = 'hotel.charges'
    _description = 'hotel charges master list'

    title = fields.Char("Title")
    description = fields.Char("Description")

