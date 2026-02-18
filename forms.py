from wtforms import Form, PasswordField
from wtforms import IntegerField, StringField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id=IntegerField("id")
    nombre = StringField("Nombre",[
        validators.DataRequired("Ingresa tu nombre"),
        validators.length(min=4, max=10, message="Ingresa un nombre valido")
    ])
    apaterno = StringField("Apaterno",[
        validators.DataRequired("Ingresa tu Apellido Paterno"),
        validators.length(min=4, max=10, message="Ingresa un apellido Paterno valido")
    ])
    correo = EmailField("Correo",[
        validators.DataRequired("Ingresa tu Correo"),
        validators.Email(message="Ingresa un correo valido")
    ])

class UserForm2(Form):
    id=IntegerField("id")
    nombre = StringField("Nombre",[
        validators.DataRequired("Ingresa tu nombre"),
        validators.length(min=4, max=10, message="Ingresa un nombre valido")
    ])
    apaterno = StringField("Apaterno",[
        validators.DataRequired("Ingresa tu Apellido Paterno"),
        validators.length(min=4, max=10, message="Ingresa un apellido Paterno valido")
    ])
    email = EmailField("Correo",[
        validators.DataRequired("Ingresa tu Correo"),
        validators.Email(message="Ingresa un correo valido")
    ])