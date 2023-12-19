
from odoo import fields, exceptions, api
from odoo import models


class Patrocinador(models.Model):
    _name = "grupoG1.Patrocinador"

    id_patrocinador = fields.Integer(required=True, string="id_patrocinador")
    nombre = fields.Char(required=True, string="nombre")
    descripcion = fields.Text(required=True, string="Descripcion")
    email = fields.Char(required=True, string="Email")
    telefono = fields.Integer(required=True, string="Telefono")
    duracion = fields.Date(required=True, string="Duracion")

    eventos = fields.Many2many('id_evento', string='eventos')
    @api.constrains('duracion')
    def _validate_date(self):
        for place in self:
            if fields.Date.from_string(place.duracion) < fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("La fecha no puede ser anterior a la Actual")

    @api.onchange('descripcion')
    def _onchange_description(self):
        if len(str(self.descripcion)) > 100:
            return {
                'Aviso': {
                    'Titulo': "Algo malo ha pasado",
                    'Mensaje': "Has sobrepasado el maximo de caracteres posibles"
                }
            }

    @api.onchange('nombre')
    def _onchange_name(self):
        if len(str(self.nombre)) > 100:
            return {
                'Aviso': {
                    'Titulo': "Algo malo ha pasado",
                    'Mensaje': "Has sobrepasado el maximo de caracteres posibles"
                }
            }
