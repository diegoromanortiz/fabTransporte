from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from app import app
from . import appbuilder, db

from .models import  ServicioTecnico,Camiones,Clientes,Saldos,Localidad,FormaDePago


class FormaDePagoView(ModelView):
    datamodel = SQLAInterface(FormaDePago)
    list_columns = ["tipoDePago "]

class SaldosView(ModelView):
    datamodel = SQLAInterface(Saldos)
    list_columns = ["fecha","cliente_id","saldo"]

class ServicioTecnicoView(ModelView):
    datamodel = SQLAInterface(ServicioTecnico)
    list_columns = ["fecha", "costo", "cliente_id","camion_id"]



class CamionesView(ModelView):
    datamodel = SQLAInterface(Camiones)
    list_columns = ["marca", "modelo", "cliente_id"]

class ClientesView(ModelView):
    datamodel = SQLAInterface(Clientes)
    list_columns = ["nombre", "apellido", "email"]


"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )




class LocalidadView(ModelView):
    datamodel = SQLAInterface(Localidad)
    add_columns = ["name"]
    edit_columns = ["name"]
    show_columns = ["name"]
    list_columns = ["name"]

class FormaDePagoView(ModelView):
    datamodel = SQLAInterface( FormaDePago)
    add_columns = [" tipoDePago"]
    edit_columns = ["tipoDePago"]
    show_columns = ["tipoDePago"]
    list_columns = ["tipoDePago"]

    
db.create_all()

appbuilder.add_view(
   ClientesView, "Clientes", icon="fa-folder-open-o", category="Clientes"
)

appbuilder.add_view(
    SaldosView, "Saldos", icon="fa-folder-open-o", category= "Clientes"
)
appbuilder.add_separator("Clientes")
appbuilder.add_view(
    CamionesView, "Camiones", icon="fa-folder-open-o", category="Camiones"
)
appbuilder.add_view(
    ServicioTecnicoView, "ServicioTecnico", icon="fa-folder-open-o", category= "ServicioTecnico"

)

appbuilder.add_view(
    LocalidadView, "Localidad", icon="fa-folder-open-o", category="Clientes"
)

appbuilder.add_view(
    FormaDePagoView, "Forma_de_pago", icon="fa-folder-open-o", category="ServicioTecnico"
)



