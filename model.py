from odoo import models, fields

class VehicleControl(models.Model):
    _name = "vehicle.vehicle"
    matricula = fields.Char(string='Matricula', requiered=True)
    tipo = fields.Char(string='Tipo')
    photo = field.Binary(string='Phioto')
    km = fields.Interger(string='Km')
    fecha_matriculacion = fields.Date(string='Fecha Matricula)
