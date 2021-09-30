import datetime

from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey,Float,Date,Table
from sqlalchemy.orm import relationship



class Saldos(Model):

    sid = Column(Integer,primary_key=True)
    fecha = Column(Date)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    Clientes = relationship("Clientes")
    saldo = Column(Float)
    
def today():
    return datetime.datetime.today().strftime('%d/%m/%Y')

class FormaDePago(Model):
    id = Column(Integer, primary_key=True)
    tipoDePago = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.tipoDePago

assoc_forma_de_pago_servicio_tecnico = Table(
    "forma_de_pago_servicio_tecnico",
    Model.metadata,
    Column("id", Integer, primary_key=True),
    Column("forma_de_pago_id", Integer, ForeignKey("forma_de_pago.id")),
    Column("servicio_tecnico_id", Integer, ForeignKey("servicio_tecnico.id")),
)

class ServicioTecnico(Model):
      
    stid = Column(Integer, primary_key=True)
    fecha = Column(String,default=today)
    costo = Column(Float)
    formaPago = relationship(
        "Forma de pago", secondary=assoc_forma_de_pago_servicio_tecnico, backref="ServicioTecnico"
    )
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    Clientes = relationship("Clientes")
    camion_id = Column(Integer, ForeignKey("camiones.cid"), nullable=False)
    camiones = relationship("Camiones")
    

class Camiones(Model):

    cid = Column(Integer, primary_key=True)
    marca = Column(String(75), nullable=False)
    modelo = Column(String(75), nullable=False)
    cliente_id = Column(Integer , ForeignKey("clientes.id"),nullable=False)
    clientes = relationship("Clientes")

    def __repr__(self):
        return f"Camiones('{self.marca}', '{self.modelo}')"

class Localidad(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


assoc_localidades_clientes = Table(
    "localidades_clientes",
    Model.metadata,
    Column("id", Integer, primary_key=True),
    Column("localidad_id", Integer, ForeignKey("localidad.id")),
    Column("cliente_id", Integer, ForeignKey("clientes.id")),
)

class Clientes(Model):
   
    id = Column(Integer, primary_key=True)
    nombre = Column(String(75), nullable=False)
    apellido = Column(String(75),nullable=False)
    telefono = Column (String(25),nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    direccion =Column(String(120), unique=True, nullable=False)
    localidad = relationship(
        "Localidad", secondary=assoc_localidades_clientes, backref="cliente"
    )

    def __repr__(self):
        return f"Clientes('{self.nombre}', '{self.apellido}')"




