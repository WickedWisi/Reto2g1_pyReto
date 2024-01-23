from odoo import fields, exceptions, api
from odoo import models


class User(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'

    isVoluntario = fields.Boolean(string="Voluntario")
    isSocio = fields.Boolean(string="Socio")

    socio_id = fields.Many2many("grupog1.sede", "socio_id", string="Socio")
    evento_id = fields.One2many("grupog1.evento", "evento_socio_id", string="Evento")
    voluntario_id = fields.Many2one("grupog1.sede", string="Voluntario")
