from odoo import fields
from odoo import fields, exceptions, api
from odoo import models


class Evento(models.Model):
    _name = "grupog1.evento"

    id_evento = fields.Integer(required=True, string="id_sede")
    nombre = fields.Char(required=True, string="Nombre")
    fechaEvento = fields.Date(required=True, string="Fecha del Evento")
    descripcion = fields.Text(required=True, string= "descripcion")
    Aforo = fields.Integer(required=True, string="Aforo")

    patrocinadores = fields.Many2many('id_patrocinador', string='patrocinadores')
    sede = fields.Many2One('id_sede', string='sede')
    socio = fields.Many2One('id_socio', string='socio')

    @api.onchange('nombre')
    def _onchange_name(self):
        if len(str(self.nombre)) > 100:
            return {
                'Aviso': {
                    'Titulo': "Algo malo ha pasado",
                    'Mensaje': "Has sobrepasado el maximo de caracteres posibles"
                }
            }

    @api.constrains('fechaEvento')
    def _validate_date(self):
        for place in self:
            if fields.Date.from_string(place.fechaEvento) > fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("La fecha debe ser posterior a la fecha actual")

    @api.onchange('descripcion')
    def _onchange_description(self):
        if len(str(self.descripcion)) > 100:
            return {
                'Aviso': {
                    'Titulo': "Algo malo ha pasado",
                    'Mensaje': "Has sobrepasado el maximo de caracteres posibles"
                }
            }