
from odoo import fields
from odoo import models


class Patrocinador(models.Model):
    _name = "grupoG1.Patrocinador"

    id_patrocinador = fields.Integer(required=True, string="id_patrocinador")
    nombre = fields.Char(required=True, string="nombre")
    descripcion = fields.Text(required=True, string="Descripcion")
    email = fields.Char(required=True, string="Email")
    telefono = fields.Integer(required=True, string="Telefono")
    duracion = fields.Date(required=True, string="Duracion")

