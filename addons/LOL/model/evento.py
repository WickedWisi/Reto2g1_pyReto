from odoo import fields
from odoo import models


class Evento(models.Model):
    _name = "grupoG1.evento"

    id_evento = fields.Integer(required=True, string="id_sede")
    nombre = fields.Char(required=True, string="Nombre")
    fechaEvento = fields.Date(required=True, string="Fecha del Evento")
    descripcion = fields.Text(required=True, string= "descripcion")
    Aforo = fields.Integer(required=True, string="Aforo")

    patrocinadores = fields.Many2many('id_patrocinador', string='patrocinadores')