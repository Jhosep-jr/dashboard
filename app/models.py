import datetime
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String, ForeignKey, Text
from sqlalchemy.orm import relationship

BOLIVIA_TZ = datetime.timezone(datetime.timedelta(hours=-4))

def now_bolivia():
    return datetime.datetime.now(BOLIVIA_TZ)

class Categoria(Model):
    __tablename__="categoria"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    imagen = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    estado = Column(Boolean, nullable=True)
    creado_en = Column(DateTime(timezone=True), default=now_bolivia, nullable=False)
    actualizado_en = Column(DateTime(timezone=True), default=now_bolivia, onupdate=now_bolivia, nullable=False)
    
    productos = relationship(
        "Producto",
        back_populates="categorias"
    )
    
    def __repr__(self):
        return self.nombre

class Producto(Model):
    __tablename__="producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric(10, 2), nullable=True)
    categoria_id = Column(Integer, ForeignKey("categoria.id"), nullable=False)
    imagen = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    estado = Column(Boolean, nullable=True)
    creado_en = Column(DateTime(timezone=True), default=now_bolivia, nullable=False)
    actualizado_en = Column(DateTime(timezone=True), default=now_bolivia, onupdate=now_bolivia, nullable=False)
    categorias = relationship(
        "Categoria",
        back_populates="productos"
    )
    
    def __repr__(self):
        return self.nombre