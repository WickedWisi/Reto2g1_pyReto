from odoo import models, fields, api

class User (models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    isVoluntario = fields.Boolean(string = "Voluntario")
    isSocio = fields.Boolean(string = "Socio")

    voluntario_id = fields.Many2many("grupog1.Sede", string="Voluntario Id")
    socio_id = fields.Many2One("grupog1.Sede", string="Socio Id")
    evento_id = fields.One2Many("grupo1.Sede", string="Evento Id")