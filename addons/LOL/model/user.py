from odoo import models, fields, api

class User (models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    isVoluntario = fields.Boolean(string = "Voluntario")
    isSocio = fields.Boolean(string = "Socio")