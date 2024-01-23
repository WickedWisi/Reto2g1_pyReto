from odoo import fields
from odoo import fields, exceptions, api
from odoo import models


class Evento(models.Model):
    _name = "grupog1.evento"

    id_evento = fields.Integer(required=True, string="id_Evento")
    nombre = fields.Char(required=True, string="Nombre")
    fechaEvento = fields.Date(required=True, string="Fecha del Evento")
    descripcion = fields.Text(required=True, string="descripcion")
    Aforo = fields.Integer(required=True, string="Aforo")

    evento_patrocinador_id = fields.Many2many('grupog1.patrocinador', 'patrocinador_evento_id', string="patrocinador")
    evento_sede_id = fields.Many2one('grupog1.sede', string="sede")
    evento_socio_id = fields.Many2one('res.users', string="socio")

    @api.onchange('nombre')
    def _onchange_name(self):
        if len(str(self.nombre)) > 15:
            return {
                'value': {
                    'nombre': '',  # Puedes limpiar el valor si no cumple con la condición
                },
                'warning': {
                    'title': "Error",
                    'message': "Has sobrepasado el máximo de caracteres permitidos en el nombre.",
                }
            }

    @api.constrains('fechaEvento')
    def _validate_date(self):
        for place in self:
            if fields.Date.from_string(place.fechaEvento) <= fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("La fecha debe ser posterior a la fecha actual")

    @api.onchange('descripcion')
    def _onchange_description(self):
        if len(str(self.descripcion)) > 100:
            return {
                'value': {
                    'descripcion': '',  # Puedes limpiar el valor si no cumple con la condición
                },
                'Warning': {
                    'Titulo': "Algo malo ha pasado",
                    'Mensaje': "Has sobrepasado el maximo de caracteres posibles"
                }
            }
