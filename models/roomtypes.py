from odoo import models, fields

class RoomTypes(models.Model):
    _name = 'hotel.roomtypes'
    _description = 'Hotel Room Types'
    _order = "name"

    name = fields.Char("Room Type Name")
    description = fields.Char("Room Type Description")
    imageroom = fields.Image("Room")
    imagebathroom = fields.Image("Bathroom")
    dailycharges_ids = fields.One2many('hotel.dailycharges', 'roomtype_id', string='Daily Charges')
    room_ids = fields.One2many('hotel.rooms', 'roomtype_id', string='Rooms')

class DailyCharges(models.Model):
    _name = 'hotel.dailycharges'
    _description = 'Hotel Room Type Daily Charges'

    charge_id = fields.Many2one('hotel.charges', string="Charge Title")
    amount = fields.Float("Daily Amount", digits=(10, 2), options={'always_reload': True})
    roomtype_id = fields.Many2one('hotel.roomtypes', string="Room Type")


