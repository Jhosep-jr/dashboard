from markupsafe import Markup
from .extensions import appbuilder
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Categoria, Producto

def imagen_thumbnail(value):
    if value:
        return Markup(
            f'<img src="/static/uploads/{value}" '
            f'style="max-height:50px; max-width:80px; object-fit:cover; border-radius:4px;">'
        )
    return Markup('<span style="color:#aaa;">Sin imagen</span>')

class CategoriaModelView(ModelView):
    datamodel = SQLAInterface(Categoria)
    label_columns = {
        "nombre": "Nombre",
        "descripcion": "Descripcion",
        "imagen": "Imagen",
        "estado": "Estado",
        "creado_en": "Creado en",
        "actualizado_en": "Actualizado en"
    }
    list_columns = ["imagen", "nombre", "descripcion", "estado", "creado_en"]
    add_columns = ["nombre", "descripcion", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion", "imagen", "estado"]
    show_columns = ["imagen", "nombre", "descripcion", "estado", "creado_en", "actualizado_en"]

    formatters_columns = {
        "imagen": imagen_thumbnail
    }

class ProductoModelView(ModelView):
    datamodel = SQLAInterface(Producto)
    label_columns = {
        "nombre": "Nombre",
        "descripcion": "Descripcion",
        "precio": "Precio",
        "categorias": "Categoria",
        "imagen": "Imagen",
        "estado": "Estado",
        "creado_en": "Creado en",
        "actualizado_en": "Actualizado en"
    }
    list_columns = ["imagen", "nombre", "precio", "categorias", "estado"]
    add_columns = ["nombre", "descripcion", "precio", "categorias", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion", "precio", "categorias", "imagen", "estado"]
    show_columns = ["imagen", "nombre", "descripcion", "precio", "categorias", "estado", "creado_en", "actualizado_en"]

    formatters_columns = {
        "imagen": imagen_thumbnail
    }

appbuilder.add_view(
    CategoriaModelView,
    "Categorias",
    icon="fa-info",
    category="Configuraciones",
    category_icon="fa-info"
)

appbuilder.add_view(
    ProductoModelView,
    "Productos",
    icon="fa-info",
    category="Configuraciones",
    category_icon="fa-info"
)