
from odoo import fields, exceptions, api
from odoo import models


class Patrocinador(models.Model):
    _name = "grupog1.patrocinador"

    id_patrocinador = fields.Integer(required=True, string="ID Patrocinador")
    nombre = fields.Char(required=True, string="Nombre")
    descripcion = fields.Text(required=True, string="Descripción")
    email = fields.Char(required=True, string="Email")
    telefono = fields.Integer(required=True, string="Teléfono")
    duracion = fields.Date(required=True, string="Duración")

    patrocinador_evento_id = fields.Many2many("grupog1.evento", 'patrocinador_evento_id', string="Evento")

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
    @api.constrains('duracion')
    def _validate_date(self):
        for patrocinador in self:
            if patrocinador.duracion and fields.Date.from_string(patrocinador.duracion) < fields.Date.today():
                raise exceptions.ValidationError("La fecha no puede ser anterior a la actual")

    @api.onchange('descripcion')
    def _onchange_description(self):
        if len(str(self.descripcion)) > 100:
            return {
                'Aviso': {
                    'Titulo': "Algo malo ha pasado",
                    'Mensaje': "Has sobrepasado el maximo de caracteres posibles"
                }
            }

    @api.model
    def create(self, vals):
        # Aquí puedes agregar tu lógica personalizada antes de la creación
        record = super(Patrocinador, self).create(vals)

        # Aquí puedes agregar tu lógica personalizada después de la creación
        return record
