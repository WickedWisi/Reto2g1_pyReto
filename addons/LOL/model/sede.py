from odoo import fields
from odoo import models


class Sede(models.Model):
    _name = "grupoG1.Sede"

    id_sede = fields.Integer(required=True, string="id_sede")
    finContrato = fields.Date(required=True, string="Fin De Contrato")
    pais = fields.Char(required=True, string="Pais")
    numVoluntariosMax = fields.Integer(required=True, string="Numero de voluntarios maximo")
    aforoMax = fields.Integer(required=True, string="Aforo maximo")
    ubicacion = fields.Integer(required=True, string= "Ubicacion")

