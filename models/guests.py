from odoo import models, fields, api

class Guest(models.Model):
    _name = 'hotel.guest'
    _description = 'Guest Information'
    _order='lastname, firstname, middlename'

    lastname = fields.Char(string="Lastname")
    firstname = fields.Char(string="Firstname")
    middlename = fields.Char(string="Middlename")
    address_streetno = fields.Char(string="Address/ Street & No.")
    address_area = fields.Char(string="Address/ Area, Unit&bldg, Brgy")
    address_city = fields.Char(string="Address/ City/Town")
    zipcode = fields.Char(string="ZIP code")
    contactno = fields.Char(string="Contact No.")
    email = fields.Char(string="Email")
    gender = fields.Selection([('FEMALE','Female'),('MALE','Male')],string="Gender")
    birthdate = fields.Date(string="Birthdate")
    photo = fields.Image(string="Guest Photo")

    name = fields.Char(string="Name", compute='_compute_name', store=True)
    
    @api.depends('lastname', 'firstname', 'middlename')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.lastname}, {rec.firstname} {rec.middlename}"
