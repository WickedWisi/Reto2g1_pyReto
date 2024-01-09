from odoo import fields, exceptions, api
from odoo import models


class Sede(models.Model):
    _name = "grupog1.Sede"

    id_sede = fields.Integer(required=True, string="id_sede")
    finContrato = fields.Date(required=True, string="Fin De Contrato")
    pais = fields.Char(required=True, string="Pais")
    numVoluntariosMax = fields.Integer(required=True, string="Numero de voluntarios maximo")
    aforoMax = fields.Integer(required=True, string="Aforo maximo")
    ubicacion = fields.Integer(required=True, string= "Ubicacion")

    socio_id = fields.Many2many('res_users', string='socio')
    voluntario_id = fields.One2Many('res_users', string='voluntario')
    id_evento = fields.One2Many('grupog1.evento', string='evento')

    @api.constrains('finContrato')
    def _validate_date(self):
        for place in self:
            if fields.Date.from_string(place.finContrato) > fields.Date.from_string(fields.Date.today()):
                raise exceptions.ValidationError("La fecha debe ser posterior a la fecha actual")

    @api.constrains('aforoMax')
    def _check_aforo(self):
        for aforoMax in self:
            if not (0 <= (self.duration) <= 250):
                raise exceptions.ValidationError("La duracion no puede ser negativa ni superar los 90 minutos.")