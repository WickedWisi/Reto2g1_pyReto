from odoo import fields, exceptions, api
from odoo import models


class Sede(models.Model):
    _name = "grupog1.sede"

    id_sede = fields.Integer(required=True, string="ID Sede")
    finContrato = fields.Date(required=True, string="Fin De Contrato")
    pais = fields.Char(required=True, string="País")
    numVoluntariosMax = fields.Integer(required=True, string="Número de voluntarios máximo")
    aforoMax = fields.Integer(required=True, string="Aforo máximo")
    ubicacion = fields.Char(required=True, string="Ubicación")

    sede_socio_id = fields.Many2many('res.users', 'socio_id', string="Socio")
    sede_voluntario_id = fields.One2many('res.users', 'voluntario_id', string='Voluntarios')
    sede_evento_id = fields.One2many('grupog1.evento', 'evento_sede_id', string='Evento')

    @api.onchange('finContrato')
    def _validate_date(self):
        for sede in self:
            if sede.finContrato and fields.Date.from_string(sede.finContrato) <= fields.Date.today():
                raise exceptions.ValidationError("La fecha debe ser posterior a la fecha actual")

    @api.constrains('aforoMax')
    def _check_aforo(self):
        for sede in self:
            if not 0 <= sede.aforoMax <= 250:
                raise exceptions.ValidationError("El aforo debe estar entre 0 y 250.")